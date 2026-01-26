def draft_reply(guest_message: str, tone: str = "Professional") -> str:
    """
    Takes the guest's message and returns a drafted host reply.
    For now this is a simple template (no AI yet).
    """
    guest_message = guest_message.strip()

    if not guest_message:
        return "Paste a guest message first, then click Generate."

    if tone == "Friendly":
        return (
            "Hey, thanks for your message 😊\n\n"
            "Yes, absolutely, happy to help. Could you please share a little more detail "
            "so I can confirm the best option for you?\n\n"
            "Kind regards,\nYour Host"
        )

    # Default: Professional
    return (
        "Hi there,\n\n"
        "Thanks for your message. I’m happy to help.\n\n"
        "Could you please share a bit more detail so I can assist you accurately?\n\n"
        "Best regards,\nYour Host"
    )