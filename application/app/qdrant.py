#pip install qdrant-client
#pip install -U sentence-transformers

#start qdrant server
#docker pull qdrant/qdrant
#docker run -p 6333:6333 qdrant/qdrant
import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

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
def upload_documents(documents):
    client.upload_records(
        collection_name="fake_data",
        records=[
            models.Record(
                id=idx, vector=encoder.encode(doc["filename"]).tolist(), payload=doc
            )
            for idx, doc in enumerate(documents)
        ],
    )

# Search
def search_by_vector(vector):
    hits = client.search(
        collection_name="fake_data",
        query_vector=encoder.encode(vector).tolist(),
        limit=1,
        score_threshold=0.100,
    )
#    for hit in hits:
#        print(hit.payload, "score:", hit.score)
    return hits[0].payload

