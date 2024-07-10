import sys
import cmd
from .generate import chat

from mlx_lm import load

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

            response = chat(self.messages, self.model, self.tokenizer) 

            self.messages.append({
                'role' : 'assistant',
                'content' : response
            })

            print()

    def exit():
        return True

def main():
    print(sys.argv)
