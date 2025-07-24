from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=20)
    docs = splitter.create_documents([text])
    return docs