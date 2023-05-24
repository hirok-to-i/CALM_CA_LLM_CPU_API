# CALM_CA_LLM_CPU_API
This repository is API for OpenCALM with CyberAgent Japanese LLM and CPU.

## Start OpenCALM API
```bash
cd ~
git clone CALM_CA_LLM_CPU_API
cd CALM_CA_LLM_CPU_API
bash build_docker_calm3b.sh #Build Docker
bash start_docker_calm3b.sh #Start Docker
```

## Request API
```bash
time curl localhost:8000/ -XPOST -d '{"message":"株式とは、"}'
```
