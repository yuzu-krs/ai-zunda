# llm_adapter.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class LLMAdapter:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt-neox-3.6b-instruction-sft", use_fast=False)
        self.model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt-neox-3.6b-instruction-sft", torch_dtype=torch.float16).to("cuda")

    def create_chat(self, comment):
        prompt = f"ユーザー: {comment}<NL>システム: "

        token_ids = self.tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")

        with torch.no_grad():
            output_ids = self.model.generate(
                token_ids.to(self.model.device),
                do_sample=True,
                max_new_tokens=128,
                temperature=0.7,
                pad_token_id=self.tokenizer.pad_token_id,
                bos_token_id=self.tokenizer.bos_token_id,
                eos_token_id=self.tokenizer.eos_token_id
            )
        output = self.tokenizer.decode(output_ids.tolist()[0][token_ids.size(1):])
        output = output.replace("<NL>", "\n")
        output = output.replace("</s>", "")  # </s> を削除
        return output + "なのだ"