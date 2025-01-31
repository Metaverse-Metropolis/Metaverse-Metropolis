# Step 19: Create `docs/installation_guide.md` file

1. File: `docs/installation_guide.md`
2. Instructions:
   1. Open your GitHub repository.
   2. Click on "Add file" → "Create new file".
   3. In the filename field, enter `docs/installation_guide.md`.
   4. Copy and paste the following content into the text editor.

---

# Installation Guide

This document explains how to install and set up the Metaverse Metropolis AI Agent on your local machine or server.

## 1. Prerequisites

Before installing the AI Agent, ensure you have the following installed:

- Python 3.8+
- Git
- Virtual environment tools (e.g., venv or virtualenv)

## 2. Cloning the Repository

To get started, clone the repository to your local machine by running the following command:

git clone https://github.com/your-repository/metaverse-metropolis-ai-agent.git  
cd metaverse-metropolis-ai-agent

## 3. Setting Up the Virtual Environment

It is recommended to use a virtual environment to manage project dependencies. To set up the environment:

python3 -m venv env  
source env/bin/activate  # On Windows: .\env\Scripts\activate

## 4. Installing Dependencies

Once the virtual environment is activated, install the necessary dependencies:

pip install -r requirements.txt

## 5. Running the AI Agent

After the dependencies are installed, you can run the AI Agent using the following command:

python src/main.py

## 6. Optional: Setting Up Docker

If you prefer to run the AI Agent in a Docker container, follow these steps:

1. Create a `Dockerfile` in the root directory:

FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]

2. Build and run the Docker container:

docker build -t metaverse-metropolis-ai-agent .  
docker run -p 5000:5000 metaverse-metropolis-ai-agent

## 7. Troubleshooting

If you encounter any issues during installation, refer to the `docs/setup_guide.md` and `docs/user_guide.md` for additional setup instructions. For more specific errors, consult the relevant troubleshooting section in the user guide.
