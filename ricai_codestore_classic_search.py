from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from ricai_codestore_helper import RicaiCodestoreHelper

class RicaiCodestoreClassicSearchSchema(BaseModel):
    repository: str = Field(..., description="The Github repository to use for testing")
    location: str = Field(..., description="The path to file(s) to be found")

class RicaiCodestoreClassicSearchTool(BaseTool):
    """
    RicAI Search code by location tool

    Attributes:
        name : The name.
        description : The description.
        args_schema : The args schema.
    """
    name = "RicaiCodestoreClassicSearch"
    description = (
        "A tool for searching the code database by specific location."
    )
    args_schema: Type[BaseModel] = RicaiCodestoreClassicSearchSchema

    class Config:
        arbitrary_types_allowed = True
    
    def _execute(self, repository: str, location: str):
        """
        Execute the RicAI Search code by location tool.

        Args:
            repository: The Github repository to use for testing
            location: The path to file(s) to be found

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
            result = ricai_codestore_helper.retrieve_code_by_location(repository, location)
            return result
        except Exception as err:
            return f"Error: Unable to search codebase - {err}"