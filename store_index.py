# Import librarys and functions from helper.py and store_index.py 
# to be able to use them in the main.py file   

from src.helper import load_pdf, text_split, download_hugging_face_embeddings     # import load_pdf, text_split, download_hugging_face_embeddings from helper.py

from dotenv import load_dotenv    # import load_dotenv from dotenv package and load the .env file because it contains the API key . 
import os                      # import os package to access the environment variables  and to interact with the operating system . 
import pinecone                # import pinecone package to interact with the Pinecone API 
from langchain_huggingface import HuggingFaceEmbeddings   # import HuggingFaceEmbeddings from langchain_huggingface package
from pinecone import Pinecone, ServerlessSpec              # import Pinecone and ServerlessSpec from pinecone package 


# we need to load our pdf which is present inside our data folder .   

extracted_data = load_pdf("data/")


# calling the text_split function
text_chunks = text_split(extracted_data)             # extracted_data is the list of documents and text_chunks is the list of chunks


# calling the download_hugging_face_embeddings function and store the result in embeddings variable
embeddings = download_hugging_face_embeddings()  


# Create embeddings for chunks 

def batch_upsert(index, vectors, batch_size=100):              # batch_upsert is a function that upserts vectors in batches and batch_size is the size of each batch  
    """Upsert vectors in batches"""
    total_vectors = len(vectors)                               # len is a function that returns the length of the list
    for i in (range(0, total_vectors, batch_size)):             # range is a function that returns a list of numbers
        batch = vectors[i:i + batch_size]                       # batch is a list of vectors
        try:                                                   # try is a function that tries to execute a block of code
            index.upsert(                                      # upsert is a function that upserts vectors in batches
                vectors=batch,                                 # vectors is a list of vectors
                namespace="medical-book"                       # namespace is a string that specifies the namespace
            )                                                
        except Exception as e:                                  # Exception is a class that represents an error
            print(f"Error upserting batch {i//batch_size}: {str(e)}")    
            continue                                           # continue is a function that skips the rest of the loop


# 1. Load environment variables from .env file
load_dotenv()                            # load the environment variables
api_key = os.getenv('PINECONE_API_KEY')   # get the value of PINECONE_API_KEY

# 2. Validate API key
if not api_key:                # if PINECONE_API_KEY is not found in environment variables  
    raise ValueError("PINECONE_API_KEY not found in environment variables")  # raise an error

# 3. Initialize Pinecone with new syntax 

try:
    pc = Pinecone(api_key=api_key)       # initialize Pinecone 

    # 4. Setup index
    index_name = "medical-chatbot"      # name of the index
    if index_name not in pc.list_indexes().names():    # check if index exists 
        pc.create_index(            # create index
            name=index_name,        # name of the index
            dimension=384,          # dimension of embeddings = 384 because we are using all-MiniLM-L6-v2
            metric='cosine',       # cosine similarity is the default
            spec=ServerlessSpec(    # serverless spec is the default 
                cloud='aws',        # aws is free to use
                region='us-east-1'   # us-east-1 is free to use and default
            )
        )
    index = pc.Index(index_name)    # store it in a variable called index and index_name is the name of the index and pc is the Pinecone object
    
except Exception as e:     # if there is any error 
    print(f"Pinecone initialization error: {str(e)}")     # print the error
    raise                  # raise the error

# 5. Process and upsert extracted_data to index

def create_embeddings(text_chunks, embeddings):    # create_embeddings is a function that creates vectors from extracted data and text_chunks is the list of chunks and embeddings is the embeddings object 
    vectors = []                               # vectors is an empty list and used to store vectors
    for i, chunk in enumerate(text_chunks):    # enumerate is a function that returns an enumerate object and i is the index and chunk is the chunk
        embedding = embeddings.embed_query(chunk.page_content)    # embed_query is a function that returns the embeddings of the query and chunk.page_content is the text content of the chunk
        vector = {                                       # vector is a dictionary that stores the vector data 
            'id': f'chunk_{i}',                        # id is a string that specifies the id of the vector and i is the index and chunk is the chunk
            'values': embedding,                      # values is a list that stores the embeddings of the chunk
            'metadata': {                            # metadata is a dictionary that stores the metadata of the chunk
                'text': chunk.page_content,         # text is a string that stores the text content of the chunk and chunk is the chunk
                **chunk.metadata 
            }
        }
        vectors.append(vector)                   # append is a function that adds the vector to the list of vectors
    return vectors                            # return is a function that returns the list of vectors and vectors is the list of vectors

# Initialize HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(           # HuggingFaceEmbeddings is a class that represents HuggingFace embeddings
    model_name="sentence-transformers/all-MiniLM-L6-v2"  # model_name is a string that specifies the model name
    
)

# create vectors from extracted data
vectors = create_embeddings(text_chunks, embeddings)     # create_embeddings is a function that creates vectors from extracted data

# Upsert in batches
batch_upsert(index, vectors, batch_size=50)      # batch_size is the number of vectors to upsert in each batch and vectors is the list of vectors and index is the index

# we have build our knowledge base [ store the vector data of our medical book in pinecone DB ]







