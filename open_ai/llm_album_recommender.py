from dotenv import load_dotenv
from os import getenv
from langchain import OpenAI, PromptTemplate, LLMChain

load_dotenv()
OPENAI_API_KEY = getenv('OPENAI_API_KEY')

llm: OpenAI = OpenAI(
    temperature=0.9,
    openai_api_key=OPENAI_API_KEY,
    max_retries=0
)

prompt_template: PromptTemplate = PromptTemplate(
    input_variables=['artists'],
    template="""Indique um álbum para conhecer dos seguintes artistas e dê uma 
    breve explicação da importância: {artists}"""
)

album_recommender_chain: LLMChain = LLMChain(
    llm=llm,
    prompt=prompt_template
)