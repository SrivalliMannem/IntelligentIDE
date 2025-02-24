import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def debug_code(code):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Identify and fix the bug in the following code:\n\n{code}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    buggy_code = '''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
'''
    print(debug_code(buggy_code))
