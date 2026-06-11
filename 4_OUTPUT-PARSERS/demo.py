from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct:cerebras",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# prompt 1 -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# prompt 2 -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic': 'black hole'})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result1.content})
result2 = model.invoke(prompt2)
print(result2.content)