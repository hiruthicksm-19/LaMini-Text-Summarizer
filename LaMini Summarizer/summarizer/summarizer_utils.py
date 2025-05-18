from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline
import torch
import asyncio
import os

# Ensure event loop compatibility
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

os.environ["STREAMLIT_WATCH_DISABLE"] = "true"

checkpoint = "LaMini-Flan-T5-248M"
tokenizer = T5Tokenizer.from_pretrained(checkpoint)
base_model = T5ForConditionalGeneration.from_pretrained(
    checkpoint,
    device_map='auto',
    torch_dtype=torch.float32,
    offload_folder="./offload"
)

from summarizer.file_utils import file_processing

def llm_pipeline(filepath):
    pipe_sum = pipeline(
        "summarization",
        model=base_model,
        tokenizer=tokenizer,
        device_map="auto",
        max_length=500,
        min_length=50,
    )
    input_text = file_processing(filepath)
    result = pipe_sum(input_text)
    return result[0]['summary_text']
