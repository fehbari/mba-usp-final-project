import os
import pandas as pd
import plotly.express as px


def make_path(result):
    return "./results/images/{}".format(result)


def plot_graph(df, x_row, y_row, title, h_line, result, filename):
    fig = px.scatter(df, x=x_row, y=y_row, title=title)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(rangemode="tozero")
    fig.add_hline(y=h_line)
    fig.write_image("{}/{}.png".format(make_path(result), filename))


def plot_result(result):
    df = pd.read_csv("./results/{}.csv".format(result))
    os.makedirs(make_path(result), exist_ok=True)

    # Toxicity predictions
    plot_graph(
        df,
        "text",
        "toxicity",
        "Predicted Toxicity of Input Values",
        0.7,
        result,
        "toxicity",
    )

    # Time spent in the pipeline
    plot_graph(df, "text", "time", "Elapsed Time", 1.0, result, "time")

    # Time spent running predictions
    plot_graph(
        df,
        "text",
        "time_prediction",
        "Elapsed Time in Prediction",
        0.2,
        result,
        "time_prediction",
    )


plot_result("offensive")
plot_result("positive")
