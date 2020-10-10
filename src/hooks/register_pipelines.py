from typing import Dict

from kedro.pipeline import Pipeline

try:
    from kedro.framework.hooks import hook_impl
except ModuleNotFoundError:

    def hook_impl(func):
        return func


class RegisterPipelinesHook:
    """Hook to register Pipelines."""

    def __init__(
        self,
        pipeline_dict: Dict[str, Pipeline],
    ):
        self._pipeline_dict = pipeline_dict

    @hook_impl
    def register_pipelines(self) -> Dict[str, Pipeline]:
        """Register the project's pipeline.

        Returns:
            A mapping from a pipeline name to a ``Pipeline`` object.

        """

        return self._pipeline_dict
