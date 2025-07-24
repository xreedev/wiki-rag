import sqlite3
import pickle
import numpy as np

class EmbeddingDB:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS embeddings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            vector BLOB
        )
        ''')
        self.connection.commit()

    def insert_vector_data(self, chunks, embeddings):
        for chunk, vector in zip(chunks, embeddings):
            vector_blob = pickle.dumps(vector)
            self.cursor.execute(
                "INSERT INTO embeddings (text, vector) VALUES (?, ?)",
                (chunk, vector_blob)
            )
        self.connection.commit()

    def get_vectors_and_ids(self):
        self.cursor.execute("SELECT id,vector FROM embeddings")
        rows = self.cursor.fetchall()
        ids = []
        vectors = []

        for id_, blob in rows:
            ids.append(id_)
            vectors.append(pickle.loads(blob))

        ids = np.array(ids)
        vectors = np.array(vectors).astype('float32')
        return { 'ids' : ids, 'vectors' : vectors}

    def get_vector_data(self):
        self.cursor.execute("SELECT text, vector FROM embeddings")
        rows = self.cursor.fetchall()

        texts= []
        vectors = []
        for text, blob in rows:
            texts.append(text)
            vectors.append(pickle.loads(blob))
        vector_embeddings = np.array(vectors).astype('float32')
        return { 'texts' : texts, 'vectors' : vector_embeddings }

    def get_text_by_id(self,ids):
        new_ids = []
        for id in ids:
            if id != 0 :
                new_ids.append(id - 1)
            new_ids.append(id + 1)
            new_ids.append(id)
        placeholders = ','.join('?' for _ in new_ids)  # "?,?,?"
        self.cursor.execute(f"SELECT text FROM embeddings WHERE id IN ({placeholders})",new_ids)
        rows = self.cursor.fetchall()
        return rows

    def get_data(self):
        self.cursor.execute(f"SELECT text FROM embeddings")
        rows = self.cursor.fetchall()
        return rows

