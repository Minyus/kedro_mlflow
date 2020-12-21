# Kedro MLflow (Basic limited-YAML example of PipelineX)

## This project works with Kedro 0.16.x only.
## Please use [kedro-starters-sklearn](https://github.com/Minyus/kedro-starters-sklearn) which works with Kedro 0.17.0 or later.

A simple example project using Kedro, MLflow, and [PipelineX](https://github.com/Minyus/pipelinex) to run Scikit-learn tasks.
If you are a YAML lover, you may prefer [full-YAML version](https://github.com/Minyus/pipelinex_sklearn).

<p align="center">
<img src="img/kedro_pipeline.png">
Pipeline visualized by Kedro-viz
</p>

## How to run:


### 1. Install dependencies

```bash
$ pip install kedro scikit-learn pandas pipelinex mlflow plotly kedro-viz 
```

Note: `plotly` and `kedro-viz` are for visualization.

### 2. Clone this repository and cd into it

```bash
$ git clone https://github.com/Minyus/kedro_mlflow.git
$ cd kedro_mlflow
```

### 3. Go to next step to use the Iris datasets included in this project. 

Optionally, you may dowonload another dataset such as [Kaggle Titanic](https://www.kaggle.com/c/titanic/data), replace  `train.csv` and `test.csv` in `data/input` directory, and modify `base/parameters.yml` to set parameters appropriate for the dataset.

### 4. Run `main.py`

```bash
$ python main.py
```

Alternatively, Kedro CLI can be used to run.

```bash
$ kedro run
```

### 5. [Optional] View the experiment logs in MLflow's UI 

```bash
$ mlflow server --host 0.0.0.0 --backend-store-uri sqlite:///mlruns/sqlite.db --default-artifact-root ./mlruns/experiment_001
```

<p align="center">
<img src="img/mlflow_ui.png">
Experiment logs in MLflow's UI
</p>

## MLflw logging configuration

In this example project, MLflow logging is configured in Python code at `src/hooks/mlflow_hooks.py` so users can get benefit from linting/auto-completion by the Python IDE. It is also possible to configure in `parameters.yml` as demonstrated [here](https://github.com/Minyus/pipelinex_sklearn).

Regarding MLflow logging options, please see [here](https://github.com/Minyus/pipelinex#integration-with-mlflow-by-kedro-hooks-callbacks)

## Kedro catalog configuration

In this example project, the Kedro catalog is configured in Python code at `src/catalogs/catalog.py` using a hook at `src/hooks/add_catalog_dict.py` so users can get benefit from linting/auto-completion by the Python IDE. It is also possible to configure in `catalog.yml` as well.


## Simplified Kedro project template

This project was created from the GitHub template repository at https://github.com/Minyus/kedro_template

To use for a new project, fork the template repository and hit `Use this template` button next to `Clone or download`.

<p align="center">
<img src="https://help.github.com/assets/images/help/repository/use-this-template-button.png">
</p>
