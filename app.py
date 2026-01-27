import streamlit as st
from services.message_assistant import draft_reply

st.title("AI-Assisted Airbnb Guest Reply")

st.markdown("### 1. Guest message")

guest_message = st.text_area(
    "Paste the guest's message here:",
    placeholder="Hi, what time is check-in?"
)

st.markdown("### 2. Reply settings")

tone = st.selectbox(
    "SelectTone",
    ["Professional", "Friendly"]
    )

# Initialize session state
if "reply" not in st.session_state:
    st.session_state.reply = ""

st.markdown("### 3. Generate reply")

if st.button("Generate Reply"):
    st.session_state.reply = draft_reply(guest_message, tone)

st.markdown("### 4. Draft reply (editable)")

st.session_state.reply = st.text_area(
    "Edit the reply before sending:",
    value=st.session_state.reply,
    height=180
)

if st.button("Clear draft"):
    st.session_state.reply = ""