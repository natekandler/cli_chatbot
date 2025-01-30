import cmd
from chatbot import Chatbot

class CLIChat(cmd.Cmd):
    def __init__(self):
        super().__init__() 
        self.chatbot = Chatbot()

    intro = "Hi I'm a chatbot. For help with commands, type 'help' or '?'. Otherwise just ask me a question. To finish the session type 'exit'\n"
    prompt = ">>> "


    def do_query(self, line):
        self.chatbot.query_chat(line)

    def do_exit(self, line):
        """Exit the CLI"""
        print("Goodbye!")
        return True  
    
    def default(self, line):
        self.do_query(line)

if __name__ == "__main__":
    CLIChat().cmdloop()
