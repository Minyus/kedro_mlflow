from kedro.pipeline import Pipeline, node

from ..nodes.sklearn_demo import train_model, evaluate_model, run_inference
from ..nodes.init_model import init_model


pipelines_dict = {
    "__default__": Pipeline(
        [
            node(func=init_model, inputs=None, outputs="init_model"),
            node(
                func=train_model,
                inputs=[
                    "init_model",
                    "train_df",
                    "params:cols_features",
                    "params:col_target",
                ],
                outputs="model",
            ),
            node(
                func=evaluate_model,
                inputs=[
                    "model",
                    "train_df",
                    "params:cols_features",
                    "params:col_target",
                ],
                outputs="score",
            ),
            node(
                func=run_inference,
                inputs=["model", "test_df", "params:cols_features"],
                outputs="pred_df",
            ),
        ]
    )
}
