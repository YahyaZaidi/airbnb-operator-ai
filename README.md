# AI-Assisted Airbnb Guest Reply Tool

## Overview
This project is a lightweight operator tool that assists Airbnb hosts or co-hosts by drafting guest replies.
It does not send messages automatically. All replies are reviewed and sent manually by the operator.

The goal is to reduce repetitive communication work while keeping humans in control.

## What the tool does
- Accepts a guest message as input
- Allows the operator to select a reply tone (Professional or Friendly)
- Generates a draft reply based on predefined rules
- Displays the reply in an editable text area

## What the tool does NOT do
- It does not integrate directly with Airbnb
- It does not send messages automatically
- It does not make decisions without human approval

## How it works
- Streamlit is used to build the user interface
- Business logic is separated into a service module
- User input is passed to a reply generator function
- The generated reply is stored in session state so it can be edited

## Tech stack
- Python
- Streamlit

## Why this project exists
Many short-term rental operators claim full automation through AI.
This project intentionally focuses on human-in-the-loop design to keep communication safe, explainable, and controllable.

## Future improvements
- Replace rule-based replies with AI-generated suggestions
- Add tone suggestions instead of manual selection
- Add simple analytics for message types