import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def draft_reply(guest_message: str, tone: str) -> str:
    guest_message = guest_message.strip()
    if not guest_message:
        return "Please paste a guest message before generating a reply."

    system_prompt = (
        "You are an assistant helping Airbnb hosts draft guest replies. "
        "The host always reviews and edits the reply before sending. "
        "Be concise, helpful, and answer the guest's question directly."
    )

    user_prompt = (
        f"Guest message:\n{guest_message}\n\n"
        f"Tone: {tone}\n\n"
        "Write the best possible reply. If the guest asks a specific question, answer it directly. "
        "If key info is missing, ask one clear follow-up question."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.6,
        )
        return response.choices[0].message.content.strip()

    except Exception:
        return "AI generation failed. Please try again."