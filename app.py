from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global tokenizer
    global model
    
    device = 0 if torch.cuda.is_available() else -1
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global tokenizier
    global model

    # Parse out your arguments
    input_text = model_inputs.get('input_text', None)
    if input_text == None:
        return {'message': "No input_text provided"}
    
    # Run the model with a hack
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=200)
    for i in outputs:
        yield tokenizer.decode(i)

