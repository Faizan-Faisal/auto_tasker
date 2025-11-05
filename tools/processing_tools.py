# # tools/processing_tools.py
# from agents import function_tool
# import pandas as pd


# @function_tool
# def run_pandas_query(dataframe: dict, code: str) -> dict:
#     """
#     Execute LLM-generated Pandas code on a DataFrame.
#     Example code: 'df[df["sales"] < 1000]'
#     """
#     df = pd.DataFrame(dataframe["data"], columns=dataframe["columns"])
#     local_vars = {"df": df, "pd": pd}
#     try:
#         result = eval(code, {"__builtins__": {}}, local_vars)

#         if isinstance(result, pd.DataFrame):
#             return {"columns": result.columns.tolist(), "data": result.values.tolist()}
#         elif isinstance(result, pd.Series):
#             return {"columns": [result.name], "data": [[v] for v in result.tolist()]}
#         else:
#             return {"result": result}
#     except Exception as e:
#         return {"error": str(e)}


# tools/processing_tools.py
from agents import function_tool
from pydantic import BaseModel
import pandas as pd

class DataFrameInput(BaseModel):
    columns: list[str]
    data: list[list]

class DataFrameOutput(BaseModel):
    columns: list[str] | None = None
    data: list[list] | None = None
    result: str | None = None
    error: str | None = None


@function_tool
def run_pandas_query(dataframe: DataFrameInput, code: str) -> DataFrameOutput:
    """Execute LLM-generated Pandas code on a DataFrame."""
    df = pd.DataFrame(dataframe.data, columns=dataframe.columns)
    local_vars = {"df": df, "pd": pd}

    try:
        result = eval(code, {"__builtins__": {}}, local_vars)

        if isinstance(result, pd.DataFrame):
            return DataFrameOutput(columns=result.columns.tolist(), data=result.values.tolist())
        elif isinstance(result, pd.Series):
            return DataFrameOutput(columns=[result.name], data=[[v] for v in result.tolist()])
        else:
            return DataFrameOutput(result=str(result))
    except Exception as e:
        return DataFrameOutput(error=str(e))
