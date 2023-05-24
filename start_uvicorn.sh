#!/bin/bash

cd /root
uvicorn --host 0.0.0.0 fastapi_calm3b:app
