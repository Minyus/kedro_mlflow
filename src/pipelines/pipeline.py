from kedro.pipeline import Pipeline, node

from ..nodes.my_module import my_func


pipelines_dict = {
    "__default__": Pipeline(
        [node(func=my_func, inputs=None, outputs="my_output_dataset"),]
    )
}
