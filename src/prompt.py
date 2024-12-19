# prompt.py is the file where we will define our prompt template for LLM and generate the correct answer with the help of LLM. 

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

# First of all we will define one prompt template and prompt template is telling our LLM what he need to do .

# Define prompt template for LLM and this is the template that we will give to our LLM

prompt_template="""                    
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}  
Question: {question} 

Only return the helpful answer below and nothing else.
Helpful answer: 
"""



