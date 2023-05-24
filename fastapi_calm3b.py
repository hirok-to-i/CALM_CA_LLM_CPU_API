import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from colorama import Fore, Back, Style, init
from fastapi import FastAPI, Body
import json

init(autoreset=True)

model = AutoModelForCausalLM.from_pretrained("cyberagent/open-calm-3b", device_map="auto", torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, cache_dir="./")
tokenizer = AutoTokenizer.from_pretrained("cyberagent/open-calm-3b", cache_dir='./')

app = FastAPI()

@app.post("/")
def read_root(body=Body(...)):
    data = json.loads(body)
    print(json.dumps(data, indent=2))

    inputs = tokenizer(data["message"] , return_tensors="pt").to(model.device)
    with torch.no_grad():
        tokens = model.generate(
            **inputs,
            max_new_tokens=64,
            do_sample=True,
            temperature=0.9,
            pad_token_id=tokenizer.pad_token_id,
        )
        
    output = tokenizer.decode(tokens[0], skip_special_tokens=True)
    print(Fore.YELLOW+'CPU: '+output)

    data["output"] = output

    return data

