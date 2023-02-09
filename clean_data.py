import pandas as pd


def clean_dataset_offensive():
    input = "./data/offensive_full.csv"  # Download from: https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-language-dataset
    output = "./data/offensive.csv"
    df = pd.read_csv(input, usecols=["offensive_language", "tweet"], index_col=False)
    df = df[df["offensive_language"] >= 4]  # Only high offensiveness
    df.to_csv(output, index=False)


def clean_dataset_sentiment():
    input = "./data/sentiment_full.csv"  # Download from: https://www.kaggle.com/datasets/kazanova/sentiment140
    output = "./data/positive.csv"
    df = pd.read_csv(
        input,
        usecols=[0, 5],
        index_col=False,
        skiprows=800000,
        nrows=1650,
        encoding="latin-1",
    )
    df.columns = ["target", "tweet"]
    df = df[df["target"] == 4]  # Only positive polarity
    df.to_csv(output, index=False)


clean_dataset_offensive()
clean_dataset_sentiment()
