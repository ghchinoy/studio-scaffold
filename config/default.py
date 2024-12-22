import os 
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv(override=True)


@dataclass
class Default:
    PROJECT_ID: str = field(default_factory=lambda: os.environ.get("PROJECT_ID"))
    LOCATION: str = os.environ.get("LOCATION", "us-central1")
    MODEL_ID: str = os.environ.get("MODEL_ID", "gemini-1.5-flash")
    INIT_VERTEX: bool = True