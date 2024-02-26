import tkinter as tk
from tkinter import scrolledtext
import random
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class ChatBot:
    def __init__(self):
        self.dialogue_history = {}
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def respond(self, user_input):
        response = self.generate_response(user_input)
        return response

    def generate_response(self, user_input):
        input_ids = self.tokenizer.encode(user_input, return_tensors='pt')
        output = self.model.generate(input_ids, max_length=100, num_return_sequences=1)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

class ChatInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("ChatBot")
        self.chat_bot = ChatBot()
        
        self.chat_history = scrolledtext.ScrolledText(self.master, width=40, height=20)
        self.chat_history.grid(column=0, row=0, padx=10, pady=10)

        self.user_input = tk.Entry(self.master, width=40)
        self.user_input.grid(column=0, row=1, padx=10, pady=10)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.master, text="Send", command=self.send_message)
        self.send_button.grid(column=1, row=1, padx=10, pady=10)

    def send_message(self, event=None):
        user_input_text = self.user_input.get()
        self.chat_history.insert(tk.END, f"You: {user_input_text}\n")
        self.chat_history.insert(tk.END, f"Bot: {self.chat_bot.respond(user_input_text)}\n")
        self.chat_history.see(tk.END)
        self.user_input.delete(0, tk.END)

def main():
    root = tk.Tk()
    chat_interface = ChatInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
