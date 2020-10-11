from typing import Dict

from kedro.framework.hooks import hook_impl
from kedro.io import AbstractDataSet, DataCatalog
from kedro.pipeline import Pipeline


class AddCatalogDictHook:
    """Hook to add data sets."""

    def __init__(
        self,
        catalog_dict: Dict[str, AbstractDataSet] = {},
    ):
        """
        Args:
            catalog_dict: catalog_dict to add.
        """
        assert isinstance(catalog_dict, dict), "{} is not a dict.".format(catalog_dict)
        self._catalog_dict = catalog_dict

    @hook_impl
    def after_catalog_created(self, catalog: DataCatalog) -> None:
        catalog.add_feed_dict(self._catalog_dict)


class RegisterPipelinesHook:
    """Hook to register Pipelines."""

    def __init__(
        self,
        pipeline_dict: Dict[str, Pipeline] = {},
    ):
        self._pipeline_dict = pipeline_dict

    @hook_impl
    def register_pipelines(self) -> Dict[str, Pipeline]:
        """Register the project's pipeline.

        Returns:
            A mapping from a pipeline name to a ``Pipeline`` object.

        """

        return self._pipeline_dict
