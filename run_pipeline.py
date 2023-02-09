import pandas as pd
import six
import time
from detoxify import Detoxify
from google.cloud import translate_v2 as translate
from dotenv import load_dotenv

load_dotenv()

sentences = 500  # Up to 1600
model = Detoxify("original", device="cuda")


def run_prediction(input_text):
    results = model.predict(input_text)
    # print(pd.DataFrame(results, index=[input_text]).round(5))
    return float(results["toxicity"])


def translate_text(target, text):
    translate_client = translate.Client()
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")
    result = translate_client.translate(text, target_language=target)
    translated = result["translatedText"]
    return translated


def read_inputs(dataset, column):
    input = "./data/{}.csv".format(dataset)
    df = pd.read_csv(input, usecols=[column], index_col=False, nrows=sentences)
    return df.values.tolist()


def write_results(dataset, lines):
    with open("./results/{}.csv".format(dataset), "w") as csv_file:
        headers = [
            "text",
            "translation",
            "in_toxic",
            "toxicity",
            "time",
            "time_prediction",
            "time_translation",
        ]
        print(",".join(headers), file=csv_file)
        for line in lines:
            print(line, file=csv_file)


def execute_pipeline(dataset):
    inputs = read_inputs(dataset, "tweet")
    lines = []

    for input in inputs:
        text = "".join(input)
        start_time = time.time()
        result = run_prediction(text)
        time_prediction = time.time() - start_time
        start_time_translation = time.time()
        translated = translate_text("es", text)
        time_translation = time.time() - start_time_translation
        time_total = time.time() - start_time
        is_toxic = result >= 0.7

        line = "{},{},{},{},{},{},{}".format(
            text.replace(",", ""),
            translated.replace(",", ""),
            is_toxic,
            result,
            time_total,
            time_prediction,
            time_translation,
        )
        print(line)
        lines.append(line)

    write_results(dataset, lines)


execute_pipeline("offensive")
execute_pipeline("positive")
