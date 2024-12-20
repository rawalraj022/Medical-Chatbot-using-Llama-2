# Description: This file contains the code to create a Flask application that serves as the API for the retrieval QA chain.  

# Import the necessary packages and modules.

# To create a Flask application, we need to import the Flask class from the flask package and other necessary classes.
from flask import Flask, render_template, jsonify, request        # import Flask, render_template, jsonify, request from flask package to create a Flask application.
from src.helper import download_hugging_face_embeddings         # import download_hugging_face_embeddings function from src.helper file to download the embeddings from Hugging Face model hub.

# To interact with the Pinecone API, we need to import the following classes from the pinecone package.
import os                      # import os package to access the environment variables  and to interact with the operating system . 
import pinecone                # import pinecone package to interact with the Pinecone API . 
from langchain_huggingface import HuggingFaceEmbeddings   # import HuggingFaceEmbeddings from langchain_huggingface package for downloading the embeddings from Hugging Face model hub .
from pinecone import Pinecone, ServerlessSpec              # import Pinecone and ServerlessSpec from pinecone package and ServerlessSpec is a class that represents a serverless Pinecone vector database

# To create retrieval QA chain, we need to import the following classes from langchain package.
from langchain import PromptTemplate             # so first thing we need prompt templates
from langchain.chains import RetrievalQA         # funciton called chains and import retrieval Question answer
from langchain.prompts import PromptTemplate            # function is prompts and import PromptTemplate
from langchain_community.llms import CTransformers              # function is llms and import CTransformers  

# For accessing the environment variables, we need to import the load_dotenv function from the dotenv package.
from dotenv import load_dotenv  # import load_dotenv function from dotenv package to load the environment variables from the .env file.

# import everything from src.prompt file  to use the prompt template for LLM and generate the correct answer with the help of LLM.
from src.prompt import *     # '*' means import everything from src.prompt file to use the prompt template for LLM and generate the correct answer with the help of LLM.


# ---------- this is the code to create a Flask application that serves as the API for the retrieval QA chain.-------------


# First of all, we need to initialize the Flask application. 
    # Flask is a framework in python that allows us to build web applications.
        # HTML and CSS code is used to design the web pages and Flask is used to connect the web pages to the python code.
            # HTML and CSS code we can easily find on the internet and we can use it to design our web pages.
# Now we will create a Flask application.

app = Flask(__name__)   # create a Flask application and pass the name of the module to the Flask constructor and store it in the variable 'app'.

# Now First of all we need to load our embedding model. 
# calling the download_hugging_face_embeddings function and store the result in embeddings variable .
embeddings = download_hugging_face_embeddings() 

# 1. Now we need to load our api environment variables from the .env file.
load_dotenv()                            # load the environment variables
api_key = os.getenv('PINECONE_API_KEY')   # get the value of PINECONE_API_KEY

# 2. Validate API key
if not api_key:                # if PINECONE_API_KEY is not found in environment variables  
    raise ValueError("PINECONE_API_KEY not found in environment variables")  # raise an error


# Now we need to initialize the Pinecone with the API key. 
# 3. Initialize Pinecone with new syntax 

try:
    pc = Pinecone(api_key=api_key)       # initialize Pinecone 

    # 4. Setup index
    index_name = "medical-chatbot"      # name of the index
    if index_name not in pc.list_indexes().names():    # check if index exists or not 
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


# Now if we have existing index and vectors inside the index of Pinecone then, 
    # instead of creating a new index and uploading the vectors again, 
        # we can directly use the existing index and vectors because we 
        # have already executed our "store_index.py" file and we have 
        # uploaded the vectors in the Pinecone index and we have stored it in the variable called "index".
        
# Now we just need to load the existing index and vectors from the Pinecone index.

# Load the existing index and vectors from the Pinecone index













