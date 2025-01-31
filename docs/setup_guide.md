# Setup Guide

This document explains how to set up the Metaverse Metropolis AI Agent locally for development and testing.

## 1. Prerequisites

Before you start, make sure you have the following installed:

- Python 3.8+
- Git
- Virtual environment tools (e.g., venv or virtualenv)

Make sure you have the necessary Python version and Git installed by running:

python --version  
git --version

## 2. Clone the Repository

Run the following command to clone the repository to your local machine:

git clone https://github.com/your-repository/metaverse-metropolis-ai-agent.git  
cd metaverse-metropolis-ai-agent

Note: Replace `your-repository` with your actual GitHub repository name.

## 3. Create a Virtual Environment

Create a virtual environment to keep your project dependencies isolated:

python3 -m venv env  
source env/bin/activate  # On Windows: .\env\Scripts\activate

On Windows, use `.\env\Scripts\activate` to activate the virtual environment.

## 4. Install Dependencies

After activating your virtual environment, install the required dependencies:

pip install -r requirements.txt

If you encounter issues during installation, make sure your environment is set up correctly and check the `requirements.txt` file for the necessary dependencies.

## 5. Run the Application

Once the dependencies are installed, run the AI Agent:

python src/main.py

The AI Agent should begin running and making decisions as described in the system architecture.

## Additional Information

For more detailed instructions, refer to the following documents in the `docs/` folder:

- [API Reference](api_reference.md)
- [Roadmap](roadmap.md)
