# tools/processing_tools.py
from agents import function_tool
import pandas as pd


@function_tool
def run_pandas_query(dataframe: dict, code: str) -> dict:
    """
    Execute LLM-generated Pandas code on a DataFrame.
    Example code: 'df[df["sales"] < 1000]'
    """
    df = pd.DataFrame(dataframe["data"], columns=dataframe["columns"])
    local_vars = {"df": df, "pd": pd}
    try:
        result = eval(code, {"__builtins__": {}}, local_vars)

        if isinstance(result, pd.DataFrame):
            return {"columns": result.columns.tolist(), "data": result.values.tolist()}
        elif isinstance(result, pd.Series):
            return {"columns": [result.name], "data": [[v] for v in result.tolist()]}
        else:
            return {"result": result}
    except Exception as e:
        return {"error": str(e)}
