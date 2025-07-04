## Getting Started to set up Ollama using Mistral model inside local device (CLI)

1. Install Ubuntu WSL using Powershell as admin:

```cmd
wsl --install -d Ubuntu
```

2. Create username and password
3. Download Ollama through WSL

```cmd
sudo apt update && sudo apt install curl -y
curl -fsSL https://ollama.com/install.sh | sh
```

4. Then, try run Mistral

```cmd
ollama run mistral
```

## Simple Chat with Ollama

This repository consists of:

1. Python backend using FastAPI
2. Frontend using Index and javascript
3. Connect to Ollama using API

### Run the command inside Ubuntu (WSL)

1. Make sure the project is inisde WSL home directory. If not, just copy the file and move the folder like the code below:

```cmd
cp -r /mnt/d/git-testing/<project_folder_name> ~/<project_folder_name>
cd ~/<project_folder_name>
```

2. Create virtual environment. If you already done it and your venv folder does not contain like this 'venv/bin/activate'. Delete that folder and redo again.

```cmd
python3 -m venv venv
```

3. Activate it and install required packages

```cmd
source venv/bin/activate
pip install fastapi uvicorn requests
```

4. Run your FASTAPI app

```cmd
uvicorn main:app --reload --port 8000
```

5. To run the model again, just simple run the FASTAPI app through you WSL


