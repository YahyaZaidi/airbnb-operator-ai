import streamlit as st
from services.message_assistant import draft_reply

st.title("AI-Assisted Airbnb Guest Reply")

guest_message = st.text_area(
    "Paste guest message here:",
    placeholder="Hi, what time is check-in?"
)

tone = st.selectbox("Tone", ["Professional", "Friendly"])

if st.button("Generate Reply"):
    reply = draft_reply(guest_message, tone)
    st.subheader("Draft reply")
    st.write(reply)