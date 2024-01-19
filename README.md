# Autogen using functions and a local LLM
Example of how to use a local llm with function calling, in this example to call local (company) ERP systems

# Local LLM
I just started a local API with llama_cpp.server like this

>  python -m llama_cpp.server --model C:\pathto\mistral-7b-instruct-v0.2.Q4_K_M.gguf --n_ctx 4096 --main_gpu 0 --n_gpu_layers -1

It listenes to localhost:8000
