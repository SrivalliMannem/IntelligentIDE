
### Code

#### 1. Code Generation (Python)
```python
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "Create a Python function to sort a list of integers using bubble sort."
    print(generate_code(prompt))
