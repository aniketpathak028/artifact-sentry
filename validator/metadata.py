import re

def validate_metadata(metadata: dict, rules: dict) -> dict:
    errors = []
    required = rules["metadata"]["required_fields"]
    version_pattern = rules["metadata"]["version_format"]

    for field in required:
        if field not in metadata or not metadata[field]:
            errors.append(
                f"Missing or empty required field: '{field}'"
            )

    if "version" in metadata:
        if not re.match(version_pattern, str(metadata["version"])):
            errors.append(
                f"Version '{metadata['version']}' is not valid. "
                f"Expected format: 1.2.3"
            )

    return {"passed": len(errors) == 0, "errors": errors}