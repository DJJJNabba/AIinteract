# AI Console Client

This project is a Python-based console application that interacts with an AI model server using an API. The program allows users to send messages to the AI model, switch between available models, toggle streaming on and off, and manage the system prompt.

## Features

- **Command-based Interface**: Interact with the AI model using various commands such as `/help`, `/models`, `/usemodel`, `/assistant`, `/system`, and more.
- **Model Selection**: List available models and switch between them dynamically.
- **Stream Toggle**: Option to toggle streaming for responses.
- **System Prompt Customization**: Change the system prompt during the conversation.
- **Easy Reset**: Clear both the terminal and conversation context with a simple command.

## Requirements

- Python 3.11 or higher
- Dependencies listed in `requirements.txt`:
  - `certifi==2024.8.30`
  - `charset-normalizer==3.4.0`
  - `idna==3.10`
  - `requests==2.32.3`
  - `urllib3==2.2.3`

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/DJJJNabba/AIinteract.git
cd AIinteract
```

### 2. Set Up the Virtual Environment

Create and activate a virtual environment (optional but recommended):

- **Windows**:
  ```bash
  python -m venv AIenv
  AIenv\Scripts\activate
  ```

- **Linux/Mac**:
  ```bash
  python3 -m venv AIenv
  source AIenv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Directly via Python

To run the main application after activating the virtual environment, use:

```bash
python AIconsoleClient.py
```

## Available Commands

Once the application is running, you can use the following commands:

- **/help**: View available commands
- **/models**: List available models
- **/usemodel [number]**: Change the current model by number
- **/system [prompt]**: Set a new system prompt
- **/assistant [message]**: Send a message as the assistant
- **/stream**: Toggle streaming on and off
- **/clear**: Clear the terminal
- **/reset**: Clear both the terminal and conversation context
- **/info**: View current settings (streaming, system prompt, current model)
- **/exit**: Exit the chat

## Example Usage

```bash
You: /models
Available Models:
1. llama-3.2-1b-instruct
2. l3-evil-stheno-v3.2-8b

You: /usemodel 1
Current model set to: llama-3.2-1b-instruct

You: Hello, how are you?
Llama 3.2: I'm doing great, how can I assist you today?
```

## Troubleshooting

- If you encounter issues with dependencies, ensure you are using the correct Python version and that all dependencies in `requirements.txt` are installed correctly.

## Contributing

Feel free to submit pull requests or open issues to improve this project. Contributions are welcome!
