import openai

class AI:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

        with open("translations.json", 'r', encoding="utf8") as file:
            self.dictionary = file.read()

        try:
            openai.Model.retrieve("gpt-4")
        except openai.error.InvalidRequestError:
            self.kwargs['model'] = "gpt-3.5-turbo"

    def chat(self, filename, content):
        messages = [
        {"role": "system", "content": "you're a transpiler from Chava to Java and vice versa. Chava is a Hebrew flavor of Java. "
        "It uses Hebrew words for all keywords, class names, functions and parameters"
        "When you're given a file name and its content you need to identify its language by the file extension and translate it accordingly"
        f"when translating keywords use the following dictionary:\n{self.dictionary}"
        "Your output must be a valid Chava or Java code. Add the filename as a comment"
        "add nothing else to the output"},
        {"role": "user", "content": f"{filename}:\n{content}"}
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
