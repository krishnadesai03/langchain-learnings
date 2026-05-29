# this code is for generating embeddings for a single query

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

result = embeddings.embed_query("Delhi is the capital of India")

print(str(result))

# ***************************************************************************************

# this code is for generating embeddings for a multiple queries or "docs"

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India.",
    "Mumbai is the capital of Maharashtra.",
    "Indianapolis is the capital of Indiana."
]

result = embeddings.embed_documents(documents)

print(str(result))