# Kedro MLflow

A simple example project using Kedro, MLflow, and Scikit-learn

<p align="center">
<img src="img/kedro_pipeline.png">
Pipeline visualized by Kedro-viz
</p>

## How to run:

### 0: Download `train.csv` and `test.csv` from [Kaggle Titanic](https://www.kaggle.com/c/titanic/data) to `data/input` directory

### 1. Install dependencies

```bash
$ pip install kedro scikit-learn pandas pipelinex mlflow plotly kedro-viz 
```

Note: `plotly` and `kedro-viz` are for visualization.

### 2. Clone this repository and run `main.py`

```bash
$ git clone https://github.com/Minyus/kedro_mlflow.git
$ cd kedro_mlflow
$ python main.py
```

Alternatively, Kedro CLI can be used to run.

```bash
$ kedro run
```

## 3. [Optional] View the experiment logs in MLflow's UI 

```bash
$ mlflow server --host 0.0.0.0 --backend-store-uri sqlite:///mlruns/sqlite.db --default-artifact-root ./mlruns/experiment_001
```

<p align="center">
<img src="img/mlflow_ui.png">
Experiment logs in MLflow's UI
</p>

## MLflw logging configuration

In this example project, MLflow logging is configured in Python code at `src/hooks/mlflow_hooks.py` so users can get benefit from linting/auto-completion by the Python IDE. It is also possible to configure in `parameters.yml` as demonstrated [here](https://github.com/Minyus/pipelinex_sklearn).

Regarding MLflow logging options, please see [here](https://github.com/Minyus/pipelinex#define-kedro-hooks-using-hooks-key)

## Kedro catalog configuration

In this example project, the Kedro catalog is configured in Python code at `src/catalogs/catalog.py` using a hook at `src/hooks/add_catalog_dict.py` so users can get benefit from linting/auto-completion by the Python IDE. It is also possible to configure in `catalog.yml` as well.


## Simplified Kedro project template

This project was created from the GitHub template repository at https://github.com/Minyus/kedro_template

To use for a new project, fork the template repository and hit `Use this template` button next to `Clone or download`.

<p align="center">
<img src="https://help.github.com/assets/images/help/repository/use-this-template-button.png">
</p>
