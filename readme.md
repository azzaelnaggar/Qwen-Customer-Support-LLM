# Qwen Customer Support LLM – Fine-Tuned Large Language Model

This project demonstrates the full deployment of a fine-tuned Large Language Model (LLM) for customer support using Qwen2.5-3B-Instruct, fine-tuned with LoRA adapters. The system is built with a Flask backend, exposed through Ngrok, and a minimal HTML/JavaScript frontend for real-time chat interaction.

## Project Structure

- **Ngrok_app/** – Flask server responsible for model loading, inference, and API deployment.
- **qwen_model/** – Contains the fine-tuned model weights (LoRA adapters) and the downloaded base model.

This implementation is inspired by Andrew Ng’s course: [Fine-Tuning Large Language Models](https://learn.deeplearning.ai/courses/finetuning-large-language-models?startTime=0)

![UI Preview](assets/Screenshot%202025-11-22%20230226.png)

---

## 1. Load Model & Environment

### 1.1 Download Base Model

Before running the backend, you need to download the base Qwen2.5-3B-Instruct model and save it locally in `qwen_model/`. This ensures compatibility with the LoRA adapters.

Run the script provided:

python download_qwen.py
The script will download:

Base model files (pytorch_model.bin or equivalent)

Tokenizer files (tokenizer.json, vocab.txt, etc.)

# Note:
The fine-tuned LoRA adapter used in this project is too large to be hosted on GitHub.
You can download it from Google Drive here: Download LoRA Adapter
After downloading, please place the files in the qwen_model/ folder to use with the backend.

1.2 Start the Flask Server (Ngrok_app.py)
The backend script performs the following:

Installs required libraries

Loads the quantized base Qwen2.5-3B-Instruct model

Applies LoRA adapters from qwen_model/

Starts a Flask server on port 5000

Opens a public Ngrok tunnel

Once running, you will see a public API endpoint:

->->-> Public URL: https://[YOUR-NGROK-SUBDOMAIN].ngrok-free.dev/chat

You will use this URL in the frontend.

2. Frontend Setup (Local Machine)
The frontend is a minimal HTML/JavaScript interface that interacts with the Flask backend.

2.1 Configure API Endpoint
In index.html, update:
const API_ENDPOINT = 'https://[YOUR-NGROK-SUBDOMAIN].ngrok-free.dev/chat';

2.2 Run the Frontend
Open the project in VS Code

Right-click index.html

Select Open with Live Server

3. How to Use the System
Ensure the Flask backend is running and the Ngrok URL is active.

Open the frontend via Live Server.

Type a message in the chat box.

Press Enter or click Send.

4. Output Preview

![UI Preview](assets/Screenshot%202025-11-22%20232427.png)

