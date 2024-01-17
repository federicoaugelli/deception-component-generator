#pip install qdrant-client
#pip install -U sentence-transformers

#start qdrant server
#docker pull qdrant/qdrant
#docker run -p 6333:6333 qdrant/qdrant

from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(host="localhost", port=6333)

documents = [
    {   
        "username": "user1",
        "password": "123456",
        "api_key": "123456",
        "address": "123456",
    },
    {
        "username": "user2",
        "password": "123456",
        "api_key": "123456",
        "address": "123456",
    },
    {
        "username": "user3",
        "password": "123456",
        "api_key": "123456",
    },
]

# Create collection
client.recreate_collection(
    collection_name="users",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)

client.upload_records(
    collection_name="users",
    records=[
        models.Record(
            id=idx, vector=encoder.encode(doc["username"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)

hits = client.search(
    collection_name="users",
    query_vector=encoder.encode("user1").tolist(),
    limit=1,
)
for hit in hits:
    print(hit.payload, "score:", hit.score)
