# This document was modified from https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/main/scripts/inference/inference_hf.py

import os
import torch
from transformers import LlamaForCausalLM, LlamaTokenizer

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

model = os.path.abspath(".") + "\\model"

generation_config = dict(
    temperature=0.2,
    top_k=40,
    top_p=0.9,
    do_sample=True,
    num_beams=1,
    repetition_penalty=1.3,
    max_new_tokens=1000
)

# The prompt template below is taken from llama.cpp
# and is slightly different from the one used in training.
# But we find it gives better results
prompt_input = (
    "Below is an instruction that describes a task. "
    "Write a response that appropriately completes the request.\n\n"
    "### Instruction:\n\n{instruction}\n\n### Response:\n\n"
)


def generate_prompt(instruction, input_parm=None):
    if input_parm:
        instruction = instruction + '\n' + input_parm
    return prompt_input.format_map({'instruction': instruction})


if __name__ == '__main__':
    load_type = torch.float16
    if torch.cuda.is_available():
        device = torch.device(0)
    else:
        device = torch.device('cpu')

    tokenizer = LlamaTokenizer.from_pretrained(model)

    model = LlamaForCausalLM.from_pretrained(
        model,
        load_in_8bit=False,
        torch_dtype=load_type,
        low_cpu_mem_usage=True,
        device_map='auto',
    )

    if device == torch.device('cpu'):
        model.float()

    model.eval()

    with torch.no_grad():
        while True:
            raw_input_text = input("Input:")
            if len(raw_input_text.strip()) == 0:
                break

            input_text = generate_prompt(instruction=raw_input_text)

            inputs = tokenizer(input_text, return_tensors="pt")  # add_special_tokens=False ?
            generation_output = model.generate(
                input_ids=inputs["input_ids"].to(device),
                attention_mask=inputs['attention_mask'].to(device),
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.pad_token_id,
                **generation_config
            )
            s = generation_output[0]
            output = tokenizer.decode(s, skip_special_tokens=True)

            response = output.split("### Response:")[1].strip()

            print("Response: ", response)
            print("\n")
