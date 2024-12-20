## Description: This file contains the code to create a Flask application that serves as the API for the retrieval QA chain.  

## Import the necessary packages and modules.

# To create a Flask application, we need to import the Flask class from the flask package and other necessary classes.
from flask import Flask, render_template, jsonify, request        # import Flask, render_template, jsonify, request from flask package to create a Flask application.

# For accessing the environment variables, we need to import the load_dotenv function from the dotenv package.
from dotenv import load_dotenv  # import load_dotenv function from dotenv package to load the environment variables from the .env file.

# To interact with the Pinecone API, we need to import the following classes from the pinecone package.
import os                      # import os package to access the environment variables  and to interact with the operating system . 
from pinecone import Pinecone, ServerlessSpec              # import Pinecone package to interact with the Pinecone API and ServerlessSpec from pinecone package and ServerlessSpec is a class that represents a serverless Pinecone vector database
from langchain_huggingface import HuggingFaceEmbeddings   # import HuggingFaceEmbeddings from langchain_huggingface package for downloading the embeddings from Hugging Face model hub .

# Convert Pinecone index to Langchain vector store and import the following classes from langchain.vectorstores package.
from langchain_community.vectorstores import Pinecone as LangchainPinecone   # import Pinecone from langchain.vectorstores package to convert Pinecone index to Langchain vector store

# To create retrieval QA chain, we need to import the following classes from langchain package.

from langchain.chains import RetrievalQA         # funciton called chains and import retrieval Question answer
from langchain_core.prompts import PromptTemplate            # function is prompts and import PromptTemplate
from langchain_community.llms import CTransformers              # function is llms and import CTransformers  

# import everything from src.prompt file  to use the prompt template for LLM and generate the correct answer with the help of LLM.
from src.prompt import *     # '*' means import everything from src.prompt file to use the prompt template for LLM and generate the correct answer with the help of LLM.

from src.helper import download_hugging_face_embeddings         # import download_hugging_face_embeddings function from src.helper file to download the embeddings from Hugging Face model hub.



## ---------- this is the code to create a Flask application that serves as the API for the retrieval QA chain.-------------


# First of all, we need to initialize the Flask application. 
    # Flask is a framework in python that allows us to build web applications.
        # HTML and CSS code is used to design the web pages and Flask is used to connect the web pages to the python code.
            # HTML and CSS code we can easily find on the internet and we can use it to design our web pages.
## Now we will create a Flask application.

app = Flask(__name__)   # create a Flask application and pass the name of the module to the Flask constructor and store it in the variable 'app'.


# Now First of all we need to load our embedding model. 
## calling the download_hugging_face_embeddings function and store the result in embeddings variable .
embeddings = download_hugging_face_embeddings() 


## 1. Now we need to load our api environment variables from the .env file.
load_dotenv()                            # load the environment variables
api_key = os.getenv('PINECONE_API_KEY')   # get the value of PINECONE_API_KEY


## 2. Validate API key
if not api_key:                # if PINECONE_API_KEY is not found in environment variables  
    raise ValueError("PINECONE_API_KEY not found in environment variables")  # raise an error

# Initialize embeddings
embeddings = HuggingFaceEmbeddings()  # HuggingFaceEmbeddings is a class that represents Hugging Face embeddings and embeddings is the HuggingFaceEmbeddings object

## Now we need to initialize the Pinecone with the API key. 
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
    
    
    # 5. Convert Pinecone index to Langchain vector store

    # Convert Pinecone index to Langchain vector store and store it in a variable called vectorstore
    vectorstore = LangchainPinecone(   # LangchainPinecone is a class that represents a Langchain vector store and vectorstore is the LangchainPinecone object
        index=index,         # index is the Pinecone index and index is the default value
        embedding=embeddings, # embedding_function is a function that returns the embeddings of the query and embeddings.embed_query is the function that returns the embeddings of the query
        text_key="text"    # text_key is a string that specifies the key in the document dictionary that contains the text and 'text' is the default value
    )
    

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

## Load the existing index and vectors from the Pinecone index
index_name = os.getenv("PINECONE_INDEX_NAME")      # get the value of the index name from the environment variables and store it in the variable called "index_name"
index = pc.Index(index_name)        # loading the existing index and vectors from the Pinecone index and store it in the variable called "index"


## Now we will define the prompt template for LLM and generate the correct answer with the help of LLM.

# Define prompt template for LLM and this is the template that we will give to our LLM 
PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])  # PromptTemplate is a class that represents a prompt template and template is a string that specifies the template and input_variables is a list of input variables

# Above is our prompt template and we are reading our prompt template from the prompt.py file and I have already imported ' from src.prompt import * ' so that I can use the prompt template here.
# input_variable , user will give us question and it will return us the response.

# chain type arguments because we will be using retable question answering chain
chain_type_kwargs={"prompt": PROMPT}    # chain_type_kwargs is a dictionary that stores the chain type arguments



# we can see the top one results but it's not readable becasue 
        # pinecone VD can give us rank results but it's not readable
            # the answer we are looking for it should be neat and clear , it should be correct answer 
            # and to get this response actually we will take the help from our LLM .
                # we will give our rank results to our llm and we will tell LLM this is our 
                # question and these three top answer , 
                # now give me the correct answer with respect to that.
                    # Let's generate our correct answer with help of our LLM ,
                    # For this we need to write the code.
# Let's generate our correct answer with help of our LLM .

## Let's load our llama model which is in our model folder 
    # with the help of C Transformer library

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",    # CTransformers is a class that represents a LLM and model is a string that specifies the path to the model 
                model_type="llama",     # model_type is a string that specifies the model type and llama is the default value 
                config={'max_new_tokens':512,    # config is a dictionary that specifies the configuration of the model and max_new_tokens is the maximum number of new tokens that can be generated by the model and 512 is the default value .
                        'temperature':0.8})  # temperature is a float that specifies the temperature of the model and 0.8 is the default value . 0.8 will give us a more creative answer and 0.0 will give us a more deterministic answer or a more accurate answer.



## We will create our retrieval question answering object which is from langchain library


# Create QA chain with vectorstore
qa = RetrievalQA.from_chain_type(   # RetrievalQA is a class that represents a retrieval question answering chain and from_chain_type is a function that creates a QA chain from a chain type
    llm=llm,                 # llm is the LLM object 
    chain_type="stuff",     # chain_type is a string that specifies the chain type 
    retriever=vectorstore.as_retriever(search_kwargs={'k': 2}), # vectorstore is the vector store object and as_retriever is a function that converts a vector store to a retriever and search_kwargs is a dictionary that specifies the search arguments and 'k' is the number of results to return
    return_source_documents=True, # return_source_documents is a boolean that specifies whether to return the source documents
    chain_type_kwargs={         # chain_type_kwargs is a dictionary that stores the chain type arguments
        'verbose': True        # verbose is a boolean that specifies whether to print verbose output
    }
)


## [flask code] Now I need to create the default route for the Flask application. 
        # The default route is the URL path that corresponds to the root of the application.
            # When a user visits the root URL of the application, the default route is triggered.
                # In this case, we will return a welcome message to the user when they visit the root URL of the application.

# I need to give the decorator called app.route and if user or host open the root URL then,
    # it will open one particular HTML file called "chat.html" file . 
        # which is present inside the 'templates' folder. 
        # Inside the 'chat.html' file, I have to write HTML code 
            # as UI(User Interface ) of the chatbot .  
                # I have to write the HTML code to take the input from the user and 
                    # display the output to the user.

# create a default route for the Flask application and pass the URL path to the route decorator and the URL path is "/" which corresponds to the root of the application .
@app.route("/")     # create a default route for the Flask application and pass the URL path to the route decorator and the URL path is "/" which corresponds to the root of the application .
def index():            # define a function called index that will be executed when the default route is triggered and the function will return the rendered template 'chat.html'.
    return render_template('chat.html')    # render the template 'chat.html' and return it to the user when they visit the root URL of the application.


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])


## Now I will initialize the Flask application and run it on the local server.
    # This code will (execute) run the Flask application on the local server with the host as " 

if __name__ == '__main__':         # check if the script is being run directly or not . If the script is being run directly, then execute the following code.    
    app.run(host="0.0.0.0", port= 8080, debug= True)  # run the Flask application on the local server with the host as " 










