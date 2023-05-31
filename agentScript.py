import langchain
import os

class Agent:
    def __init__(self):
        self.langchain = langchain.LangChain()

    def train_agent(self, file_paths):
        # Check if files exist
        for file_path in file_paths:
            if not os.path.isfile(file_path):
                print(f"File not found: {file_path}")
                return

        # Load and process the files
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                content = file.read()
                self.langchain.add_text(content)

        # Train the agent
        self.langchain.train()

        print("Agent trained successfully.")

    def ask_question(self, question):
        # Generate an answer using Langchain
        answer = self.langchain.generate_text(question)

        if answer:
            return answer
        else:
            return "I'm sorry, I don't have an answer for that."

# Example usage
agent = Agent()

# Train the agent by providing file paths
file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
agent.train_agent(file_paths)

# Ask questions to the agent
while True:
    user_question = input("Ask a question (or 'q' to quit): ")
    if user_question == 'q':
        break

    response = agent.ask_question(user_question)
    print(response)
