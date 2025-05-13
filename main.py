import json
from pathlib import Path
from ollama_client import generate_signature_prompt


EMAILS_PATH = Path("emails/test_emails.json")
PROMPT_TEMPLATE_PATH = Path("prompts/signature_prompt.txt")
OUTPUT_PATH = Path("tests/signatures.json")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with PROMPT_TEMPLATE_PATH.open(encoding="utf-8") as f:
    prompt_template = f.read()


with EMAILS_PATH.open(encoding="utf-8") as f:
    emails = json.load(f)

results = []

for item in emails:
    email_id = item.get("id")
    email_text = item.get("email", "")

    prompt = prompt_template.replace("{{email_content}}", email_text)

    try:
        response = generate_signature_prompt(prompt)
    except Exception as e:
        response = f"Error: {e}"

    results.append({
        "id": email_id,
        "signature": response
    })

with OUTPUT_PATH.open("w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Signatures extracted and saved to tests/signatures.json.")
