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



# Now we will create a Flask application.

# First of all, we need to initialize the Flask application. 
    # Flask is a framework in python that allows us to build web applications.
        # HTML and CSS code is used to design the web pages and Flask is used to connect the web pages to the python code.
            # HTML and CSS code we can easily find on the internet and we can use it to design our web pages.

app = Flask(__name__)   # create a Flask application and pass the name of the module to the Flask constructor and store it in the variable 'app'.


# Now we need to load our api environment variables from the .env file.

load_dotenv()                            # load the environment variables
api_key = os.getenv('PINECONE_API_KEY')   # get the value of PINECONE_API_KEY









