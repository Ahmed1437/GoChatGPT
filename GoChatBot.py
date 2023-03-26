# imports

import json
import openai
import gradio as gr

# API_Key
openai.api_key = "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"

# Load File
with open('prompts.json', 'r') as f:
    messages = json.load(f)

# ChatBot Function    
def chatbot(input, history = []):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, temperature = 0
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        history.append((input, reply))
        return history, history

# inputs = gr.Textbox(label="Input")
# outputs = gr.Textbox(label="Chat")

gr.Interface(fn=chatbot, inputs=["text",'state'], outputs=["chatbot",'state'], title="GoChatGPT").launch(debug = True)