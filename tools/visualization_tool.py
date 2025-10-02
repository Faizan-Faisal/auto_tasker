from agents import Agent, function_tool
import pandas as pd
import matplotlib.pyplot as plt
import io, base64

@function_tool
def generate_chart(dataframe: dict, chart_type: str, x: str, y: str | None = None) -> str:
    """Generate a chart (bar, line, pie, hist) from a dataframe and return as base64 image."""
    df = pd.DataFrame(dataframe["data"], columns=dataframe["columns"])
    fig, ax = plt.subplots()
    
    if chart_type == "bar":
        df.plot(kind="bar", x=x, y=y, ax=ax)
    elif chart_type == "line":
        df.plot(kind="line", x=x, y=y, ax=ax)
    elif chart_type == "pie":
        df.set_index(x)[y].plot(kind="pie", ax=ax, autopct="%1.1f%%")
    else:
        df[x].plot(kind="hist", ax=ax)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")
