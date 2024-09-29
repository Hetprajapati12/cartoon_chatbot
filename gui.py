import tkinter as tk
from tkinter import Text, Scrollbar, Frame, Entry, Button
from chatbot import CartoonChatbot  # Assuming CartoonChatbot class is defined in chatbot.py

class ChatbotGUI:
    def __init__(self, root):
        self.bot = CartoonChatbot()  # Initialize your chatbot instance
        self.root = root
        self.root.title("Cartoon Chatbot")

        # Create a frame to hold the chat log
        self.chat_frame = Frame(root)
        self.chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create a scrollbar for the chat log
        self.scrollbar = Scrollbar(self.chat_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a text widget to display the chat log
        self.chat_log = Text(self.chat_frame, wrap=tk.WORD, yscrollcommand=self.scrollbar.set, state='disabled', bg="white", fg="black", font=("Helvetica", 12))
        self.chat_log.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.chat_log.yview)

        # Create an entry box for user input
        self.entry_box = Entry(root, font=("Helvetica", 12))
        self.entry_box.pack(padx=10, pady=10, fill=tk.X)
        self.entry_box.bind("<Return>", self.send_message)

        # Create a button to send messages
        self.send_button = Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=5)

    def send_message(self, event=None):
        user_message = self.entry_box.get()
        self.entry_box.delete(0, tk.END)
        
        if user_message:
            self.display_message("You: " + user_message, "blue")
            if user_message.lower() == "exit":
                self.display_message("Bot: Exiting...", "red")
                self.root.after(1000, self.root.destroy)  # Close the window after 1 second
            else:
                response = self.bot.get_response(user_message)
                self.display_message("Bot: " + response, "green")

    def display_message(self, message, color):
        self.chat_log.configure(state='normal')
        self.chat_log.insert(tk.END, message + "\n", ("color",))
        self.chat_log.tag_configure("color", foreground=color)
        self.chat_log.configure(state='disabled')
        self.chat_log.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
