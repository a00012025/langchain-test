from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter

loader = DirectoryLoader(
    './data/', # my local directory
    glob='**/*.epub',     # we only get pdfs
    show_progress=True
)
docs = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=0
)

docs_split = text_splitter.split_documents(docs)
print(len(docs_split))
print(docs_split[200])