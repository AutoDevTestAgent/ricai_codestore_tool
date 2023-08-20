from abc import ABC
from typing import List

from superagi.tools.base_tool import BaseToolkit, BaseTool
from ricai_codestore_classic_search import RicaiCodestoreClassicSearchTool
from ricai_codestore_read_all import RicaiCodestoreReadAllTool
from ricai_codestore_read_latest import RicaiCodestoreReadLatestTool
from ricai_codestore_semantic_search import RicaiCodestoreSemanticSearchTool
from ricai_codestore_update import RicaiCodestoreUpdateTool

class RicaiCodestoreToolkit(BaseToolkit, ABC):
    name: str = "RicAI Codestore Toolkit"
    description: str = "Toolkit containing tools for code storage and retrieval from a vector database (Weaviate only!)."

    def get_tools(self) -> List[BaseTool]:
        return [
            RicaiCodestoreClassicSearchTool(),
            RicaiCodestoreReadAllTool(),
            RicaiCodestoreReadLatestTool(),
            RicaiCodestoreSemanticSearchTool(),
            RicaiCodestoreUpdateTool(),
            ]

    def get_env_keys(self) -> List[str]:
        return [
            "WEAVIATE_URL",
            "WEAVIATE_API_KEY",
            "OPENAI_API_KEY",
            "GITHUB_USERNAME",
            "GITHUB_ACCESS_TOKEN",
            ]