"""Validate a worker receipt's shape and candidate readiness, never acceptance."""
import argparse
import json
import math
from pathlib import Path


def validate(receipt):
    errors = []
    if not isinstance(receipt, dict):
        return ["receipt must be an object"]
    def text(obj, key, path):
        if not isinstance(obj.get(key), str) or not obj[key].strip():
            errors.append(f"{path}{key}: expected nonempty string")
    for key in ("outcome", "tracker", "worker", "topology", "routing_id",
                "executor", "execution_profile", "repository", "branch",
                "worktree", "base", "target", "rationale", "next_action"):
        text(receipt, key, "")
    if receipt.get("version") != 1 or type(receipt.get("version")) is not int:
        errors.append("version must be integer 1")
    if receipt.get("state") not in ("candidate", "incomplete"):
        errors.append("state must be candidate or incomplete; workers cannot accept")
    for key in ("changed_files", "risks", "blockers", "owner_actions"):
        value = receipt.get(key)
        if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
            errors.append(f"{key}: expected array of nonempty strings")
    for key, fields in (("checks", ("command", "result", "evidence", "target")),
                        ("dod", ("criterion", "result", "evidence"))):
        rows = receipt.get(key)
        if not isinstance(rows, list):
            errors.append(f"{key}: expected array")
            continue
        if receipt.get("state") == "candidate" and not rows:
            errors.append(f"{key}: candidate requires evidence")
        for index, row in enumerate(rows):
            prefix = f"{key}[{index}]."
            if not isinstance(row, dict):
                errors.append(prefix + "expected object")
                continue
            for field in fields:
                text(row, field, prefix)
            if row.get("result") not in ("pass", "fail", "not-run"):
                errors.append(prefix + "result must be pass, fail, or not-run")
            if receipt.get("state") == "candidate":
                if row.get("result") != "pass":
                    errors.append(prefix + "candidate requires pass")
                if key == "checks" and row.get("target") != receipt.get("target"):
                    errors.append(prefix + "target differs from candidate")
    if receipt.get("state") == "candidate":
        if receipt.get("blockers"):
            errors.append("candidate cannot have unresolved blockers")
        if receipt.get("target") in ("none", "unavailable"):
            errors.append("candidate requires an immutable target")
    telemetry = receipt.get("telemetry")
    if not isinstance(telemetry, dict):
        errors.append("telemetry: expected object")
    else:
        for key in ("tokens", "elapsed_seconds"):
            value = telemetry.get(key)
            if key not in telemetry or (value is not None and
                    (type(value) not in (int, float) or value < 0 or
                     (isinstance(value, float) and not math.isfinite(value)))):
                errors.append(f"telemetry.{key}: expected nonnegative number or null")
    return errors


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def invalid_constant(value):
    raise ValueError(f"non-JSON numeric constant: {value}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path)
    args = parser.parse_args()
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8-sig"),
                             object_pairs_hook=unique_object,
                             parse_constant=invalid_constant)
        errors = validate(receipt)
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    print(json.dumps({"valid": not errors, "errors": errors,
                      "acceptance_verified": False}, ensure_ascii=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
