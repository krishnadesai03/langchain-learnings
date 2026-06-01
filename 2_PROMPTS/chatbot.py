from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct:cerebras",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# without user, system and AI designation

# chat_history = []

# while True:
#     user_input = input('You: ')
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break
#     result = model.invoke(user_input)
#     chat_history.append(result.content)
#     print('AI: ', result.content)

# print(chat_history)

# with them

chat_history = [
    SystemMessage(content='You are a helpful Assistant.')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    chat_history.append(AIMessage(content = result.content))
    print('AI: ', result.content)

print(chat_history)