# ArtifactSentry

> **Artifact Quality Validator** — catch issues before they reach review.

ArtifactSentry is an automated artifact validation pipeline that enforces naming
conventions, metadata completeness, and structural consistency reducing manual
review time from **4+ hours to under 10 seconds**.

---

## Features

- **Naming Validation** — enforces consistent naming patterns via regex rules
- **Metadata Completeness** — ensures all required fields are present and valid
- **Structural Consistency** — checks required files, size limits, and allowed extensions
- **LLM-Assisted Analysis** — intelligent error explanation and fix suggestions
- **Automated Report Generation** — every validation run produces a full audit trail
- **Webhook-Driven** — trigger validations instantly via REST API
- **n8n Workflow Orchestration** — visual, rule-based pipeline management

---

## Architecture

```text
Artifact Upload
      │
      ▼
 Webhook Trigger (n8n)
      │
      ▼
 Python Validator (FastAPI)
      │
      ├─── Naming Check
      ├─── Metadata Check
      └─── Structure Check
                │
                ▼
         All checks passed?
          │             │
         YES            NO
          │             │
          ▼             ▼
    ✅ Notify      🤖 LLM Analysis
      Success      (explains errors +
                    suggests fixes)
                        │
                        ▼
               📄 Audit Report Saved
```
<img width="2347" height="822" alt="image" src="https://github.com/user-attachments/assets/1a35fb14-750b-4766-ae7c-7db4593ee65e" />

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Workflow Orchestration | [n8n](https://n8n.io) |
| Validation API | Python + FastAPI |
| Rule Configuration | JSON |
| LLM Analysis | OpenAI / compatible API |
| Containerization | Docker + Docker Compose |
| Notifications | Slack / Email (via n8n) |

---

## Configuration Reference

### Naming Rules

| Field | Description |
|-------|-------------|
| `pattern` | Regex pattern artifact names must match |
| `max_length` | Maximum allowed character length |
| `forbidden_chars` | Characters not allowed in names |

### Metadata Rules

| Field | Description |
|-------|-------------|
| `required_fields` | List of fields that must exist and be non-empty |
| `version_format` | Regex for valid version strings (e.g. semver) |

### Structure Rules

| Field | Description |
|-------|-------------|
| `required_files` | Files that must exist in the artifact root |
| `max_size_mb` | Maximum total artifact size in MB |
| `allowed_extensions` | Whitelist of allowed file extensions |

---
