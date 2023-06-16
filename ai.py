import openai

class AI:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

        try:
            openai.Model.retrieve("gpt-4")
        except openai.error.InvalidRequestError:
            self.kwargs['model'] = "gpt-3.5-turbo"

    def chat(self, prompt):
        messages = [
        {"role": "system", "content": "you're a transpiler from Chava to Java. Chava is a Hebrew flavor of Java. "
        "It uses Hebrew words for all keywords, class names, functions and parameters"
        "You need to translate all of these back to English"},
        {"role": "user", "content": prompt}
        ]

        response = openai.ChatCompletion.create(
            messages=messages, stream=True, **self.kwargs
        )

        chat = []
        for chunk in response:
            delta = chunk['choices'][0]['delta']
            msg = delta.get('content', '')
            print(msg, end="")
            chat.append(msg)
        return messages + [{"role": "assistant", "content": "".join(chat)}]
