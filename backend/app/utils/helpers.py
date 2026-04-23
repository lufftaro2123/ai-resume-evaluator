import json
import re

def clean_json_response(text):
    try:
        # remove ```json ``` wrappers
        text = re.sub(r"```json|```", "", text).strip()
        return json.loads(text)
    except Exception as e:
        return {"error": "Invalid JSON", "raw": text}