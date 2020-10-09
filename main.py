from pathlib import Path
from typing import Dict

from src.pipelines.pipeline import pipelines_dict
import kedro
from kedro.framework.context import KedroContext
from kedro.pipeline import Pipeline

from src.catalogs.catalog import catalog_dict
from src.hooks.add_catalog_dict import AddCatalogDictHook
from src.hooks.mlflow_hooks import mlflow_hooks


class ProjectContext(KedroContext):

    project_name = "KedroProject"
    project_version = kedro.__version__
    package_name = "nodes"
    hooks = (AddCatalogDictHook(catalog_dict),) + mlflow_hooks

    def _get_pipelines(self) -> Dict[str, Pipeline]:
        return pipelines_dict


if __name__ == "__main__":
    project_context = ProjectContext(Path.cwd())
    project_context.run()
