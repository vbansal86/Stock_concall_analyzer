# Stock_concall_analyzer
AI based chatbot /QA tool to analyze transcript of conference call held to release financial results of a company.

## Steps to run this tool :
1. Before running this repo, there are few pre-reqs:
    - Create free account on assembly ai and generate API key and save it
    - Create free account on pinecone database,create an index , note its region/environment and an API key. Save them for later use.
    - Create account on open ai and add few credits (minimum allowed : 5$) to query llm through API. Also generate API key and save it. 
2. Clone repo on local
3. Create a new file name .env  and add it to repo. In the file add following keys 

    ASSEMBLYAI_API_KEY= <your-key-here>
    OPENAI_API_KEY = <your-key-here>
    PINECONE_API_KEY = <your-key-here>
    PINECONE_INDEX_NAME = <index-name>
    PINECONE_ENVIRONMENT_REGION=<region-name>

4. Install all python packages as per requirement.txt
5. Ensure streamlit is up and running on your system.
6. Run command:- streamlit run app.py  OR python -m streamlit run app.py
