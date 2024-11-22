import streamlit as st
import google.generativeai as genai
import os
#import config
import time

st.title("Book Discussion bot!")
st.caption("A chatbot for discussing books of your choice powered by Gemini!")

gemini_key = st.secrets["gemini_api_key"]
genai.configure(api_key=gemini_key)



prompt_template = '''
You are a helpful assistant with vast knowledge in Books. You have the ability to answer most if not all questions related to
countless various successfull books (from many different genres) in a clear and detailed fashion.
You only answer questions related to novels/books. (An important execption is holy books. No need to delve into them as you may make mistakes). Otherwise, end the conversation with this is not my domain
You may respond to the user in arabic if the query is in the arabic language
'''

# Chat/Convo History
if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.model =  genai.GenerativeModel("gemini-1.5-pro")
st.session_state.chat = st.session_state.model.start_chat(
    history = [ {"role": m["role"], "parts": m["content"]}
                for m in st.session_state.messages
               ]

)
# Display chat messages from history

for message in st.session_state.messages:
    with st.chat_message(
            message["role"]):
        st.markdown(message["content"])

# user input

if prompt :=  st.chat_input("Lets chat!" + prompt_template) :
    # display user message in chat msg box
    with st.chat_message("user"):
        st.markdown(prompt)
    # add user msgs to chat history
    st.session_state.messages.append({"role": "user", "content": prompt_template + '\n' + prompt})

    # send msg to gemini assistant

    response = st.session_state.chat.send_message(
        prompt,
        stream=True,
    )

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ''

        for chunk in response:
            for ch in chunk.text.split(' '):
                full_response +=ch + ' '
                time.sleep(0.05)
                message_placeholder.write(full_response + '▌')
        # Write full message with placeholder

        message_placeholder.write(full_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": st.session_state.chat.history[-1].parts[0].text}
    )


#    with st.chat_message("assistant"):
#        chat = model.start_chat(
#            history=[
#                {"role": m["role"], "parts": m["parts"]}
#                for m in st.session_state.messages
#            ]
#        )
#        gemini_response = chat.send_message(prompt, stream=True)
#        response_stream = st.write_stream(gemini_response)
#
#    st.session_state.messages.append({"role": "assistant", "parts": response_stream})
#'''
