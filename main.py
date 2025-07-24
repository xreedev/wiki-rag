from faiss_processor import FaissProcessor
from wikipedia_api import get_wikipedia_text
from preprocessor import create_chunks
from embedder import embed_chunks,embed_query
from warehouse import EmbeddingDB
from gemini_agent import generate_evaluation

#get text from API
text = get_wikipedia_text("Large_language_model")
text=text[:5000]

# #convert to chunks
docs = create_chunks(text)
chunks = [doc.page_content for doc in docs]
# #vectorise the chunks
embeddings = embed_chunks(chunks)

#store in SQLite
db_path = 'database/new.db'
database = EmbeddingDB(db_path)
# database.insert_vector_data(chunks, embeddings)

#create faiss index using id and vectors
data = database.get_vectors_and_ids()
faiss_pc = FaissProcessor(data)

#embed query and perform FAISS search
user_query = input('Enter your query about LLMs')
query = embed_query(user_query)
required_ids = faiss_pc.search_vectors(query)
rows = database.get_text_by_id(required_ids)

eval = generate_evaluation(user_query, rows)
print(eval)