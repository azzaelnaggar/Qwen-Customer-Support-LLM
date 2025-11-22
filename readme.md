# Qwen Customer Support LLM – Fine-Tuned Large Language Model

This project showcases the complete deployment pipeline of a fine-tuned Qwen2.5-3B-Instruct model using LoRA adapters for customer support automation.
The system includes:

A Flask backend running the model locally

An Ngrok tunnel exposing the API publicly

A lightweight HTML/JavaScript frontend for real-time chat interaction

This implementation follows concepts inspired by Andrew Ng’s course:
👉 [Fine-Tuning Large Language Models](https://learn.deeplearning.ai/courses/finetuning-large-language-models?startTime=0)


![UI Preview](assets/Screenshot%202025-11-22%20230226.png)

1. Project Structure
Qwen Customer Support LLM/


├── Ngrok_app/           # Flask backend + model loading + API

├── qwen_model/          # Base model + LoRA adapter files

├── assets/              # Screenshots and UI previews

├── index.html           # Frontend interface

├── download_qwen.py     # Script to download base Qwen model

└── readme.md

3. Model Setup & Environment
2.1 Download the Base Model

Before running the backend, you must download the Qwen2.5-3B-Instruct base model.

Run:

python download_qwen.py


The script automatically downloads:

Model weights (pytorch_model.bin or equivalent)

Tokenizer files (tokenizer.json, vocab.txt, merges, etc.)

These will be stored in:

qwen_model/

2.2 Download the LoRA Adapter (Fine-Tuned Model)

⚠️ Important
The fine-tuned LoRA adapter is too large for GitHub.

You can download it from Google Drive:

👉 Download LoRA Adapter
(https://drive.google.com/file/d/1ASbXlvDlRufgntohmwPFM1u1vIu3g1Ui/view?usp=sharing)

After downloading, extract and place the contents into:
qwen_model/


This ensures the backend loads both the base model + LoRA fine-tuning.

3. Run the Backend (Flask + Ngrok)

The backend script:

Installs needed dependencies

Loads the quantized Qwen2.5-3B-Instruct model

Applies LoRA fine-tuning

Starts a Flask server on port 5000

Opens a public Ngrok tunnel

After running the backend, you will see:

-----------------------------------------------------
Public URL: https://YOUR-SUBDOMAIN.ngrok-free.dev/chat
-----------------------------------------------------


You will use this URL in the frontend.

4. Frontend Setup

The frontend is a minimal UI built using plain HTML + CSS + JavaScript.

4.1 Set the API Endpoint

Open index.html and replace the Ngrok URL:

const API_ENDPOINT = "https://YOUR-SUBDOMAIN.ngrok-free.dev/chat";

4.2 Launch the Frontend

Open folder in VS Code

Right-click index.html

Select Open with Live Server

Your local browser will open the chat interface instantly.

5. Using the System

Once everything is running:

Start the Flask backend

Confirm the Ngrok URL is active

Launch the frontend with Live Server

Type a message into the chat box

Press Enter or click Send

Receive real-time responses from your fine-tuned LLM

6. Output Preview

   ![UI Preview](assets/Screenshot%202025-11-22%20232427.png)
