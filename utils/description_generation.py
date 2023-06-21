import openai

openai.api_key = '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'

def generate_description(name, type_, code, code_elements, args=None, bases=None):
    prompt = f"I have a piece of Python code and I need to understand the {type_} named {name}. Here is the code:\n\n{code}\n\n"
    prompt += f"And here are the code elements I've extracted:\n\n{code_elements}\n\n"
    if args:
        prompt += f"The {type_} {name} has the following arguments: {', '.join(args)}. "
    if bases:
        prompt += f"The class {name} is derived from the following base classes: {', '.join(bases)}. "
    prompt += f"Can you describe what the {type_} {name} does. Answer like you are writing a document and not having a conversation. Stick to the facts and explain things step by step."

    messages = [
        {"role": "system", "content": "You are a expert python developer assistant."},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages
    )

    return response['choices'][0]['message']['content'].strip()
