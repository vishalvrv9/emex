import sys
import cmd
from .generate import chat

from mlx_lm import load

class ExitCommandException(Exception):
    pass


class Emex(cmd.Cmd):

    def __init__(self, model):
        super().__init__()
        self.model, self.tokenizer = load(model)
        self.messages = []

    def default(self, line):
        if line == "/bye" or line == "/exit":
            self.exit()
        else:
            self.messages.append({
                'role' : 'user',
                'content' : line
            })

            # response = chat(self.model, self.tokenizer, self.messages) 
            response = chat(self.messages, self.model, self.tokenizer)

            self.messages.append({
                'role' : 'assistant',
                'content' : response
            })

            print()

    def exit(self):
        raise ExitCommandException()

def main():
    if len(sys.argv) < 3:
        print("Insufficient args. Usage: emex run username/modelname from huggingface")
    elif len(sys.argv) > 3:
        print("Too many arguments")
    else:
        try:
            if sys.argv[1] != "run":
                print("Unknown command: Usage: emex run username/modelname from huggingface")
            else:
                model = sys.argv[2]
                Emex(model).cmdloop()
        except ExitCommandException as e:
            print("GoodBye")


