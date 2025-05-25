from gptqmodel import GPTQModel, QuantizeConfig
from transformers import AutoTokenizer

def load_model():
    model_path = "STiFLeR7/Phi2-GPTQ"
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
    model = GPTQModel.from_quantized(
        model_path,
        device="cpu",  # ✅ Streamlit Cloud is CPU-only
        use_safetensors=True,
        quantize_config=None
    )
    return tokenizer, model

def generate_response(prompt, tokenizer, model, max_new_tokens=150):
    inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
