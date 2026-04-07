import json
import os
import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from naming import validate_naming
from metadata import validate_metadata
from structure import validate_structure

app = FastAPI(title="ArtifactSentry", version="1.0.0")

# Load rules once at startup
RULES_PATH = os.path.join(os.path.dirname(__file__), "config/rules.json")
with open(RULES_PATH) as f:
    RULES = json.load(f)

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "../reports")


class ArtifactPayload(BaseModel):
    artifact_name: str
    artifact_path: str
    metadata: dict


@app.get("/")
def root():
    return {"message": "ArtifactSentry is running 🛡️"}


@app.post("/validate")
def validate_artifact(payload: ArtifactPayload):
    timestamp = datetime.datetime.utcnow().isoformat()

    # Run all checks
    results = {
        "artifact": payload.artifact_name,
        "timestamp": timestamp,
        "checks": {
            "naming": validate_naming(payload.artifact_name, RULES),
            "metadata": validate_metadata(payload.metadata, RULES),
            "structure": validate_structure(payload.artifact_path, RULES),
        },
    }

    # Overall pass/fail
    results["overall_passed"] = all(
        v["passed"] for v in results["checks"].values()
    )

    # Save audit report
    os.makedirs(REPORTS_DIR, exist_ok=True)
    safe_name = payload.artifact_name.replace("/", "_")
    timestamp_str = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    report_path = os.path.join(REPORTS_DIR, f"{safe_name}_{timestamp_str}.json")

    with open(report_path, "w") as f:
        json.dump(results, f, indent=2)

    return results