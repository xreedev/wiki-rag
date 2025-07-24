import faiss
import numpy as np

class FaissProcessor :
    def __init__(self,data):
        sentence_embeddings = np.array(data['vectors']).astype('float32')
        d = sentence_embeddings.shape[1]
        index = faiss.IndexFlatL2(d)
        self.db_index = faiss.IndexIDMap(index)
        self.db_index.add_with_ids(sentence_embeddings, data["ids"])

    def search_vectors(self,query):
        k = 4
        I, D = self.db_index.search(query, k)
        return D[0].tolist()