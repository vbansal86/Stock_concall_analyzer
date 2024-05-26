import streamlit as st 

from streamlit_chat import message

from main import run_llm

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []
    
if "chat_answer_history" not in st.session_state:
    st.session_state["chat_answer_history"] = []
    
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.header("Concall Analyzer")



prompt =  st.text_input("Prompt",placeholder="Enter your prompt here")

if prompt:
    with st.spinner("Generating response..."):
        generated_response = run_llm(query=prompt , chat_history=st.session_state["chat_history"])
        formatted_response = (f"{generated_response['answer']}")
        
        st.session_state["user_prompt_history"].append(prompt) 
        st.session_state["chat_answer_history"].append(formatted_response) 
        st.session_state["chat_history"].append((prompt,generated_response["answer"]))
        
if st.session_state["chat_answer_history"]: 
    for user_query , generated_response in zip(st.session_state["user_prompt_history"],st.session_state["chat_answer_history"]):
        message(user_query,is_user=True)
        message(generated_response) 