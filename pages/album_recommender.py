import streamlit as st
from open_ai.llm_album_recommender import album_recommender_chain
from openai.error import RateLimitError

st.title('Album Recommender')

user_input: str = st.text_input('Insira um ou mais artistas (separados por vírgula)')

if user_input:
    try:
        response: str = album_recommender_chain.run(artists=user_input)
        st.write(response)
    except RateLimitError as e:
        print(e)
        st.markdown(
            e.code,
            """:red[Erro:] Você excedeu o limite de chamadas à API do OpenAI.
            """
        )