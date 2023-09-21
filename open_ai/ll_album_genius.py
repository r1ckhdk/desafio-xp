from dotenv import load_dotenv
from os import getenv
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = getenv('OPENAI_API_KEY')

llm: ChatOpenAI = ChatOpenAI(
    temperature=0.7,
    openai_api_key=OPENAI_API_KEY,
)

prompt_template: PromptTemplate = PromptTemplate(
    input_variables=['artists'],
    template="""Recomende-me um álbum introdutório para quem quer conhecer as seguintes bandas/artistas e escreva
     um breve resumo sobre o álbum e a sua importância: {artists}"""
)

album_recommender_chain: LLMChain = LLMChain(
    llm=llm,
    prompt=prompt_template
)
