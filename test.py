from huggingface_hub import InferenceClient

import os
token = os.environ.get("HF_TOKEN")
client = InferenceClient(token=token)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-72B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Review this code and find bugs: print('hello world')"
        }
    ],
    max_tokens=500
)

print(response.choices[0].message.content)