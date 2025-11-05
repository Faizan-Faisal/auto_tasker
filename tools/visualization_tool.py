

# tools/visualization_tools.py
# from agents import function_tool
# from pydantic import BaseModel
# import pandas as pd
# import matplotlib.pyplot as plt
# import io, base64

# class ChartResponse(BaseModel):
#     image_base64: str


# @function_tool
# def generate_chart(dataframe: dict, chart_type: str, x: str, y: str | None = None) -> ChartResponse:
#     """Generate a chart (bar, line, pie, hist) from a dataframe and return as base64 image."""
#     df = pd.DataFrame(dataframe["data"], columns=dataframe["columns"])
#     fig, ax = plt.subplots()
    
#     if chart_type == "bar":
#         df.plot(kind="bar", x=x, y=y, ax=ax)
#     elif chart_type == "line":
#         df.plot(kind="line", x=x, y=y, ax=ax)
#     elif chart_type == "pie":
#         df.set_index(x)[y].plot(kind="pie", ax=ax, autopct="%1.1f%%")
#     else:
#         df[x].plot(kind="hist", ax=ax)

#     buf = io.BytesIO()
#     plt.savefig(buf, format="png")
#     buf.seek(0)
#     encoded = base64.b64encode(buf.read()).decode("utf-8")
#     plt.close(fig)

#     return ChartResponse(image_base64=encoded)

from agents import function_tool
from typing import Literal
from pydantic import BaseModel, Field
import matplotlib.pyplot as plt
import io
import base64


class ChartData(BaseModel):
    """Defines chart data with labels and values."""
    labels: list[str] = Field(..., description="List of labels for the chart")
    values: list[float] = Field(..., description="List of corresponding numeric values")


@function_tool
def generate_chart(chart_type: Literal["bar", "line", "pie"], data: ChartData, title: str = "Chart") -> str:
    """
    Generates a simple chart based on the type and data provided.
    Args:
        chart_type: The type of chart to generate ("bar", "line", "pie").
        data: ChartData object containing labels and values.
        title: The title of the chart.
    Returns:
        A base64-encoded PNG image of the generated chart.
    """
    labels = data.labels
    values = data.values

    plt.figure(figsize=(6, 4))
    if chart_type == "bar":
        plt.bar(labels, values)
    elif chart_type == "line":
        plt.plot(labels, values)
    elif chart_type == "pie":
        plt.pie(values, labels=labels)
    plt.title(title)

    # Save chart to buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode("utf-8")
    plt.close()
    return img_str
