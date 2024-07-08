import os
import uuid


def save_corpus(signal_name: str, input_reason: str):
    os.makedirs(f"../corpus/{signal_name}/", exist_ok=True)
    with open(f"../corpus/{signal_name}/{uuid.uuid4()}.txt", 'w+') as f:
        f.write(input_reason)
