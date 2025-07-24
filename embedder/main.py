from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import numpy as np

load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07")

def embed_chunks(chunks) -> [] :
    vectors = []
    for chunk in chunks:
        vector = embeddings.embed_query(chunk)
        vectors.append(vector)
    return vectors

def embed_query(query) :
    vector_query = embeddings.embed_query(query)
    return np.array([vector_query]).astype('float32')

