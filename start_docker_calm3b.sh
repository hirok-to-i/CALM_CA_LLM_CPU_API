#!/bin/bash

docker run -p 8000:8000 -it -v $(pwd):/root ubuntu:CALM_CA_LLM_CPU_API bash /root/start_uvicorn.sh
