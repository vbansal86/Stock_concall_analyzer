from dotenv import load_dotenv
import os
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain_community.vectorstores.pinecone import Pinecone as Pineconelangchain 
from typing import List,Dict,Any

load_dotenv()
def run_llm(query:str,chat_history:List[Dict[str,Any]]=[]) -> str:
    llm = ChatOpenAI(temperature=0,verbose=True)

    docsearch=Pineconelangchain.from_existing_index(os.environ["PINECONE_INDEX_NAME"],embedding=OpenAIEmbeddings())

    qa = ConversationalRetrievalChain.from_llm(llm=llm,retriever=docsearch.as_retriever(),return_source_documents=False)


    return qa({"question":query,"chat_history":chat_history})



if __name__=='__main__':
    print(run_llm(query="What are the latest financial results of the company?"))

