FROM ubuntu:20.04

# Update & Upgrade Ubuntu
RUN apt-get update -y
RUN apt-get upgrade -y

# Install Python3
RUN apt-get install -y python3 python3-pip

# Install Python3 Library for OpenCALM
RUN pip install prompt_toolkit numpy torch tokenizers
RUN pip install transformers accelerate sentencepiece colorama

# Install Python3 Library for API
RUN pip install fastapi "uvicorn[standard]" 

