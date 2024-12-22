from typing import Optional
from google import genai
from config.default import Default

from dotenv import load_dotenv
load_dotenv(override=True)


class ModelSetup:

    @staticmethod
    def init(project_id: Optional[str] = None, 
                    location: Optional[str] = None, 
                    model_id: Optional[str] = None):
        config = Default()
        if not project_id:
            project_id = config.PROJECT_ID
        if not location:
            location = config.LOCATION
        if not model_id:
            model_id = config.MODEL_ID
        if None in [project_id, location, model_id]:
            raise ValueError("All parameters must be set.")
        print(f"initiating genai client with {project_id} in {location}")
        client = genai.Client(
            vertexai=config.INIT_VERTEX,
            project=project_id,
            location=location,
        )
        return client, model_id
        

