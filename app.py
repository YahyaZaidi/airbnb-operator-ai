import streamlit as st
from services.message_assistant import draft_reply

st.title("AI-Assisted Airbnb Guest Reply")

guest_message = st.text_area(
    "Paste guest message here:",
    placeholder="Hi, what time is check-in?"
)

tone = st.selectbox(
    "SelectTone",
    ["Professional", "Friendly"]
    )

#Store the reply in sessions state so it persists across reruns
if "reply" not in st.session_state:
    st.session_state.reply = ""

if st.button("Generate Reply"):
    st.session_state.reply = draft_reply(guest_message, tone)

st.subheader("Draft reply (editable)")
st.session_state.reply = st.text_area(
    "Edit the reply before sending:",
    value=st.session_state.reply,
    height=180
)

if st.button("Clear"):
    st.session_state.reply = ""