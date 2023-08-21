from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from ricai_codestore_helper import RicaiCodestoreHelper

class RicaiCodestoreReadAllSchema(BaseModel):
    repository: str = Field(..., description="The Github repository to use for testing")

class RicaiCodestoreReadAllTool(BaseTool):
    """
    RicAI retrieve all code from repo tool

    Attributes:
        name : The name.
        description : The description.
        args_schema : The args schema.
    """
    name = "RicaiCodestoreReadAll"
    description = (
        "A tool for retrieving all the code from database by specific repository."
    )
    args_schema: Type[BaseModel] = RicaiCodestoreReadAllSchema

    class Config:
        arbitrary_types_allowed = True    

    def _execute(self, repository: str):
        """
        Execute the RicAI retrieve all code from repo tool.

        Args:
            repository: The Github repository to use for testing

        Returns:
            List of files if successful. or error message.
        """
        try:
            weaviate_url = self.get_tool_config("WEAVIATE_URL")
            weaviate_key = self.get_tool_config("WEAVIATE_API_KEY")
            openai_key = self.get_tool_config("OPENAI_API_KEY")
            ghub_auth = self.get_tool_config("GITHUB_ACCESS_TOKEN")
            ghub_user = self.get_tool_config("GITHUB_USERNAME")
            
            ricai_codestore_helper = RicaiCodestoreHelper(
                weaviate_url=weaviate_url,
                weaviate_key=weaviate_key,
                openai_key=openai_key,
                github_token=ghub_auth,
                github_user=ghub_user
            )
            result = ricai_codestore_helper.retrieve_all_code(repository)
            return result
        except Exception as err:
            return f"Error: Unable to search codebase - {err}"