from mlx_lm import load, generate
from mlx_lm.utils import generate_step
import mlx.core as mx

model, tokenizer = load("mlx-community/quantized-gemma-2b")
# response = generate(model, tokenizer, prompt="write a python progeam to check prime", verbose=True)
prompt = "write a hello world program in python"
print(mx.array(tokenizer.encode(prompt)))
print("tokenizer.eos_token_id")
print(tokenizer.eos_token_id)
temperature = 0
context_length = 100
def generate_chat_steps(the_prompt, the_model, tokenizer):
    tokens = []
    skip = 0

    for (token, prob), n in zip(generate_step(mx.array(tokenizer.encode(the_prompt)), the_model, temperature),
                                range(context_length)):

        if token == tokenizer.eos_token_id:
            break

        tokens.append(token)
        text = tokenizer.decode(tokens)

        # trim = None
        #
        # for sw in stop_words:
        #     if text[-len(sw):].lower() == sw:
        #         return
        #     else:
        #         for i, _ in enumerate(sw, start=1):
        #             if text[-i:].lower() == sw[:i]:
        #                 trim = -i

        yield text
        # skip = len(text)
response = generate_step(
        prompt=mx.array(tokenizer.encode(prompt)),
        model = model
        )
# for r in response:
#
#     token, prob = r
#     # print("token")
#     # print(token)
#     # print("prob")
#     # print(prob)
#     print(tokenizer.decode(token))
#     if token == tokenizer.eos_token_id:
#         break
#
ans = ''
for chunk in generate_chat_steps(prompt, model, tokenizer):
    ans += chunk
    print(chunk)

