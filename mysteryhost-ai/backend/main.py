import subprocess
import json
import os

def load_persona_prompt():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.join(script_dir, "../prompts/host_persona.txt")
    with open(prompt_path, "r") as f:
        return f.read()

def build_prompt():
    persona = load_persona_prompt()
    user_input = "Begin the first scene of a mystery. Set the mood and give me two choices."

    full_prompt = f"{persona}\n\nUser: {user_input}"
    return full_prompt

def call_ollama(prompt, model="llama3"):
    result = subprocess.run(
        ["ollama", "run", model, prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        print("Error running Ollama:", result.stderr)
    return result.stdout

def start_case():
    prompt = build_prompt()
    response = call_ollama(prompt)
    print("\n--- MYSTERY HOST ---\n")
    print(response)

if __name__ == "__main__":
    start_case()