# mba-usp-final-project

## Setup

Create `.env` file

```
cp .env.example .env
```

Fill in the variables. Then

```
pip install python-dotenv
pip install detoxify
pip install pandas
pip install google-cloud-translate
pip install plotly-express
pip install -U kaleido
```

[black](https://github.com/psf/black) is used for code formatting.

## Run

To generate test results

```
python3 run_pipeline.py
```

Results appear in the `/results` folder as CSV files.

To plot graphs from the results

```
python3 plot_results.py
```

Graphs are saved in `/results/images` as PNGs.
