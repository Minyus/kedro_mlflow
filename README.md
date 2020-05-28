# Kedro Scikit-learn

A simple example project using Kedro and Scikit-learn

<p align="center">
<img src="img/kedro_pipeline.png">
Pipeline visualized by Kedro-viz
</p>

## How to run:

### 0: Download `train.csv` and `test.csv` from [Kaggle Titanic](https://www.kaggle.com/c/titanic/data) to `data/input` directory

### 1. Install dependencies

```bash
$ pip install kedro scikit-learn pandas kedro-viz 
```

Note: `kedro-viz` is optional.

### 2. Clone this repository and run `main.py`

```bash
$ git clone https://github.com/Minyus/kedro_sklearn.git
$ cd kedro_sklearn
$ python main.py
```

Alternatively, Kedro CLI can be used to run.

```bash
$ kedro run
```

## Kedro catalog configuration

In this example project, the Kedro catalog is configured in Python code at `src/catalogs/catalog.py` using a hook at `src/hooks/add_catalog_dict.py` so users can get benefit from linting/auto-completion by the Python IDE. It is also possible to configure in `catalog.yml` as well.
