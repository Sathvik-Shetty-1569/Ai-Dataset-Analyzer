import io
import sys
from utils.security import validate_code
import pandas as pd
import matplotlib.pyplot as plt

def run_code(code, df):
    validate_code(code)

    output = io.StringIO()
    sys.stdout = output

    safe_globals = {
    "df": df,
    "pd": pd,
    "plt": plt,
    "__builtins__": {
        "print": print,
        "len": len,
        "range": range,
        "min": min,
        "max": max,
        "sum": sum
    }
}

    try:
        exec(code, safe_globals)
        result = output.getvalue()
    except Exception as e:
        result = str(e)

    sys.stdout = sys.__stdout__

    return result