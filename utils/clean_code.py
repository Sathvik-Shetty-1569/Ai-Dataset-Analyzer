import re

def clean_ai_code(code: str):
    # remove ```python and ``` blocks
    code = re.sub(r"```python", "", code)
    code = re.sub(r"```", "", code)

    return code.strip()