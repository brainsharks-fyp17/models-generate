import os
from dotenv import load_dotenv
from transformers import MBartForConditionalGeneration, MBartTokenizer

load_dotenv()
model_path = os.getenv("MODEL_PATH", "Rumesh/txt-smp-mbart")

print("Loading the model..............")
model = MBartForConditionalGeneration.from_pretrained(model_path)
tokenizer = MBartTokenizer.from_pretrained(model_path)
print("Loaded the model")
