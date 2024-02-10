#pip install qdrant-client
#pip install -U sentence-transformers

#start qdrant server
#docker pull qdrant/qdrant
#docker run -p 6333:6333 qdrant/qdrant
import os, uuid
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
#https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
load_dotenv()
encoder = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(host=os.getenv("QDRANT_HOST"), port=os.getenv("QDRANT_PORT"))

# Create collection
try:
    client.create_collection(
        collection_name="fake_data",
        vectors_config=models.VectorParams(
            size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
            distance=models.Distance.COSINE,
        ),
    )
except:
    pass


# Upload documents
def upload_documents(document):
    client.upsert(
    collection_name="fake_data",
    points=[
        models.PointStruct(
            id = str(uuid.uuid4()),
            payload=document,
            vector=encoder.encode(document["filename"]).tolist(),
        ),
    ],
    )


# Search
def search_by_vector(vector):
    hits = client.search(
        collection_name="fake_data",
        query_vector=encoder.encode(vector).tolist(),
        limit=1,
        score_threshold=0.500,
    )
    for hit in hits:
        return hit.payload
    return None

