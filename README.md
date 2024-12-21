# Medical Chatbot using Llama-2 

![Medical Chatbot Logo](images/logo.png)

The development of the Medical Chatbot using Llama 2 signifies a significant advancement in AI-driven healthcare solutions. By providing accurate and timely medical information, the chatbot aims to empower users in navigating their health concerns while improving overall accessibility to healthcare services . 

## Steps to run the project 

### Clone the repository 

```bash
Project repo: https://github.com/
```
### STEP 01- Create a conda environment after opening the repository

```bash  
conda create -n mchatbot2 python=3.9 -y   
```

```bash
conda activate mchatbot2  
```
### STEP 02- install the requirements

```bash
pip install -r requirements.txt   
```

### Create a .env file in the root directory and add your Pinecone credentials as follows:

```bash
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```bash
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python app.py
```
Now, 

```bash
open up localhost:
```

### Techstack Used : 

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone




