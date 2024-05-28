import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, chat_models
from langchain_community.vectorstores import pinecone as PineconeLangchain
from pinecone import Pinecone
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import AssemblyAIAudioTranscriptLoader
from langchain_community.document_loaders.assemblyai import TranscriptFormat
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()


def ingest_transcript(audio_file: str) -> None:
    
    print("loading transcript...")
    loader = AssemblyAIAudioTranscriptLoader(
        file_path=audio_file,
        assemblyai_api_key=os.environ.get("ASSEMBLYAI_API_KEY")
    )
    raw_docs = loader.load()


    print("splitting")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    
    documents = text_splitter.split_documents(raw_docs)
    
    print(f"Splitted into {len(documents)} documents")   
    embeddings = OpenAIEmbeddings()
    Pineconelangchain.from_documents(documents,embeddings,index_name=os.environ["PINECONE_INDEX_NAME"])
    

if __name__ == "__main__":
    ingest_transcript("https://khazanchi.co.in/files2/Khazanchi%20Jewellers%20Limited%20Earning%20Call%20Audio%20-%20H2%20FY24%20(1).mp3")
