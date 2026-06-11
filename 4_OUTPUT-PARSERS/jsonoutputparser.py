from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct:cerebras",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template= 'Give me name, age and city of a fictional person.\n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.invoke()
print(prompt)  # prompt that is sent to LLM will also include a line "Return a JSON object."

result = model.invoke(prompt)
print(result.content)

final_result = parser.parse(result.content)
print(final_result)
print(type(final_result))
print(final_result['name'])


# using chain
# chain = template | model | parser
# result = chain.invoke({})
# print(result)