import streamlit as st
from streamlit_chat import message as st_message
import aiohttp
import asyncio
import json

if "history" not in st.session_state:
    st.session_state.history = []

st.title("chat with zaraa 😊")

# One more thing: Please note that zaraa is still in demo mode and might take a little bit more time to obtain your answer.
original_title = '<p style="color:Green; font-size: 20px;">Type your question in the textbox below</p>'
st.markdown(original_title, unsafe_allow_html=True)



async def get_answer(user_message):
    async with aiohttp.ClientSession(headers={'Connection': 'keep-alive'}) as session:
        url = 'http://zaraa.fusure.africa:5000/ensers'
        payload = {'query': user_message}
        headers = {'content-type': 'application/json'}
        async with session.post(url,data=json.dumps(payload),headers=headers) as resp:
            print(resp)
            res = await resp.json()
            return res['answer']
        await asyncio.sleep(10)


def generate_answer():
    user_message = st.session_state.input_text
    message_bot = asyncio.run(get_answer(user_message))

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})

st.text_input("Talk to the bot", key="input_text", on_change=generate_answer)

for chat in st.session_state.history:
    st_message(**chat)  # unpacking
