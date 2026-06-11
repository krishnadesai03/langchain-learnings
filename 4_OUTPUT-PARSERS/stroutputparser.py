from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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
    template='Write a 5 line summary on \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic': 'black hole'})
print(result)