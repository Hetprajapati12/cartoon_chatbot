import re

class CartoonChatbot:
    def __init__(self):
        self.knowledge_base = {
            "doraemon": "Doraemon is a Japanese Anime.",
            "nobita": "Nobita is a character in the Anime Doraemon, who is often seen as the main character's best friend.",
            "shizuka": "Shizuka is a character in an Anime named Doraemon. She is the best friend of Nobita.",
            "spongebob": "Spongebob is a character from the American animated series 'Spongebob Squarepants'.",
            "patrick": "Patrick is Spongebob's best friend in the series 'Spongebob Squarepants'.",
            "tom": "Tom is a cat from the animated series 'Tom and Jerry'.",
            "jerry": "Jerry is a mouse from the animated series 'Tom and Jerry'."
        }
        self.rules = [
            (re.compile(r'who is (\w+)', re.IGNORECASE), self.get_character_info),
            (re.compile(r'tell me about (\w+)', re.IGNORECASE), self.get_character_info)
        ]

    def get_character_info(self, match):
        character = match.group(1).lower()
        return self.knowledge_base.get(character, "Sorry, I don't have information on that character.")

    def get_response(self, question):
        for pattern, func in self.rules:
            match = pattern.search(question)
            if match:
                return func(match)
        return "Sorry, I didn't understand the question."

if __name__ == "__main__":
    bot = CartoonChatbot()
    
    while True:
        question = input("You: ")
        if question.lower() == "exit":
            print("Bot: Exiting...")
            break
        response = bot.get_response(question)
        print(f"Bot: {response}")
