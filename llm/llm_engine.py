from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = None
tokenizer = None

def load_model():
    global model, tokenizer
    if model is None:
        tokenizer = AutoTokenizer.from_pretrained(
            "/workspace/models/llm", trust_remote_code=True
        )
        model = AutoModelForCausalLM.from_pretrained(
            "/workspace/models/llm",
            torch_dtype=torch.float16,
            device_map="auto"
        )

def generate(prompt):
    load_model()

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_new_tokens=200)

    return tokenizer.decode(output[0], skip_special_tokens=True)