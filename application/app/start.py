from .config import AppConfig
import os
from dotenv import load_dotenv
from .qdrant import *
from .lang import *


load_dotenv()


def generate(endpoint):
    result = search_by_vector(endpoint)
    if not result:
        result = generate_random_data(endpoint)
        result = json.loads(result)
        upload_documents({"filename": endpoint, "data": result})
    else:
        result = result["data"]
    return result

def start():
    print("Starting generate data")
    if os.getenv("GENERATE_AT_START") == "True":
        for endpoint in AppConfig.endpoints:
            print(f"Generating data for {endpoint}")
            generate(endpoint)
