# this code is for generating embeddings for a single query

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=32)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))

# ***************************************************************************************

# this code is for generating embeddings for a multiple queries or "docs"

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India.",
    "Mumbai is the capital of Maharashtra.",
    "Indianapolis is the capital of Indiana."
]

result = embedding.embed_documents(documents)

print(str(result))