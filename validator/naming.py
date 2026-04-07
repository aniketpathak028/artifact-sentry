import re

def validate_naming(artifact_name: str, rules: dict) -> dict:
    errors = []
    pattern = rules["naming"]["pattern"]
    max_len = rules["naming"]["max_length"]
    forbidden = rules["naming"]["forbidden_chars"]

    if not re.match(pattern, artifact_name):
        errors.append(
            f"Name '{artifact_name}' doesn't match required pattern: {pattern}"
        )

    if len(artifact_name) > max_len:
        errors.append(
            f"Name is too long. Max allowed: {max_len} characters"
        )

    for char in forbidden:
        if char in artifact_name:
            errors.append(
                f"Forbidden character '{char}' found in name"
            )

    return {"passed": len(errors) == 0, "errors": errors}