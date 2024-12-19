from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader   # function called document_loaders and import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter 
from langchain_huggingface import HuggingFaceEmbeddings  # import HuggingFaceEmbeddings from langchain_huggingface package

# Extract data from pdf

def load_pdf(data):                    # data is the function 
    loader = DirectoryLoader(data,       # DirectoryLoader is a class that loads documents from a directory
                            glob="*.pdf",      # glob is a pattern that matches any file with a .pdf extension
                            loader_cls=PyPDFLoader)   # PyPDFLoader is a class that loads documents from a PDF file
    documents = loader.load()                       # load is a function that returns a list of documents
    return documents                   # return is a function that returns a list of documents


# upto now I have done extraction of data from the PDF, now let's go back to our architecture 
    # Now we have to do chunks implemention because we need to 
        # convert our Corpus(whole extracted text) to text chunks because of the model input token limit.

# Split text into chunks    

def text_split(extracted_data):                                   # extracted_data is the function and text_split is the function 
    text_splitter = CharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)      # CharacterTextSplitter is a class that splits text into chunks and chunk_size is the size of each chunk and chunk_overlap is the overlap between chunks .
    text_chunks = text_splitter.split_documents(extracted_data)            # split_documents is a function that splits documents into chunks and extracted_data is the list of documents and text_chunks is the list of chunks

    return text_chunks              # return is a function that returns a list of chunks 


# download embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings







