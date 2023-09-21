from dotenv import load_dotenv
from os import getenv
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = getenv('OPENAI_API_KEY')

llm: ChatOpenAI = ChatOpenAI(
    temperature=0.8,
    openai_api_key=OPENAI_API_KEY,
)

prompt_template: PromptTemplate = PromptTemplate(
    input_variables=['subject'],
    template="""Explique-me como se eu tivesse 5 anos: {subject}"""
)

eli5_chain: LLMChain = LLMChain(
    llm=llm,
    prompt=prompt_template
)
