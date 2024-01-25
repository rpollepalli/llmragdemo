from dotenv import load_dotenv
import os
import streamlit as st
import requests



def init():
    load_dotenv()


def startUI():
    st.session_state["user_input"] = st.text_input(label="Enter a prompt :")
    st.button("Submit", on_click=my_callback, args=(st.session_state["user_input"],))

def my_callback(prompt):
    hf_api_token = os.environ["API_KEY"]
    hf_api_url = os.environ["API_URL"]
    headers = {"Authorization": f"Bearer {hf_api_token}"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_length": 200}
    }
    response = requests.post(hf_api_url, headers=headers, json=payload)
    
    size =len(response.json())
    answer="No response"
    if (size  > 0 ):
        answer= response.json()[0]['generated_text']
   
    st.write(str(answer))



if __name__ == "__main__":
    init()
    startUI()