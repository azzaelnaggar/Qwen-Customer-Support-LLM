from transformers import AutoModelForCausalLM, AutoTokenizer
from pathlib import Path

model_name = "Qwen/Qwen2.5-3B-Instruct"

save_dir = Path("qwen_base")
save_dir.mkdir(exist_ok=True)  
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
model.save_pretrained(save_dir)

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.save_pretrained(save_dir)

print(f"Model and tokenizer saved in {save_dir}/")
