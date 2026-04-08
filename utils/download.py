from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="TheBloke/Llama-2-13B-GGUF",
    local_dir="/workspace/models/llm"
)

snapshot_download(
    repo_id="black-forest-labs/FLUX.1-dev",
    local_dir="/workspace/models/flux"
)