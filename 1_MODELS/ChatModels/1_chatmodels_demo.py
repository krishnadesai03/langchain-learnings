from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# model = ChatOpenAI(model='gpt-4')
model = ChatOpenAI(model='gpt-4', temperature=0.8, max_completion_tokens=50)
# temperature -> how creative the answer should be (0: most deterministic; 2: most creative)
# 0 - 0.3 -> math, code, facts
# 0.5 - 0.7 -> QnA
# 0.9 - 1.2 -> creative writing
# 1.5+ -> wild ideas, brainstorming

# max_completion_tokens -> max words in output

result = model.invoke("What is the capital of India")

print(result) # outputs answer as well as metadata

print(result.content) # outputs required answer only

# ***************************************************************************************

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-sonnet-4-6')

result = model.invoke("What is the capital of India")

print(result.content)

# ***************************************************************************************

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result = model.invoke("What is the capital of India")

print(result.content)