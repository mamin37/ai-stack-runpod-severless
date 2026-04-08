import runpod
from llm.llm_engine import generate
from flux.flux_engine import generate_image

def handler(event):
    input_data = event["input"]

    task = input_data.get("task")

    if task == "chat":
        prompt = input_data.get("prompt", "")
        result = generate(prompt)

        return {"output": result}

    elif task == "image":
        prompt = input_data.get("prompt", "")
        image_path = generate_image(prompt)

        return {"image_path": image_path}

    else:
        return {"error": "Invalid task"}

runpod.serverless.start({"handler": handler})