import os

def validate_structure(artifact_path: str, rules: dict) -> dict:
    errors = []
    required_files = rules["structure"]["required_files"]
    max_size = rules["structure"]["max_size_mb"] * 1024 * 1024
    allowed_ext = rules["structure"]["allowed_extensions"]

    # Check required files exist
    for f in required_files:
        full_path = os.path.join(artifact_path, f)
        if not os.path.exists(full_path):
            errors.append(f"Required file missing: '{f}'")

    # Check file extensions and total size
    total_size = 0
    if os.path.exists(artifact_path):
        for root, _, files in os.walk(artifact_path):
            for file in files:
                fp = os.path.join(root, file)
                ext = os.path.splitext(file)[1]
                if ext not in allowed_ext:
                    errors.append(
                        f"Disallowed file type: '{ext}' (file: {file})"
                    )
                total_size += os.path.getsize(fp)

        if total_size > max_size:
            errors.append(
                f"Artifact too large. "
                f"Max: {rules['structure']['max_size_mb']}MB"
            )
    else:
        errors.append(f"Artifact path does not exist: '{artifact_path}'")

    return {"passed": len(errors) == 0, "errors": errors}