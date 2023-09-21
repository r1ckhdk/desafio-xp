import streamlit as st
from open_ai.ll_album_genius import album_recommender_chain
from openai.error import RateLimitError

st.title('AlbumGenius')
st.markdown(
    """
    Está interessado em conhecer sobre um artista ou banda mas não sabe por onde começar?\n
    O AlbumGenius é um recomendador de álbuns, onde você insere um artista e ele te recomenda o melhor álbum introdutório
    para conhecer a obra dele!
    """
)

user_input: str = st.text_input('Insira um ou mais bandas/artistas (separados por vírgula)')

if st.button('Enviar!') and user_input:
    try:
        with st.spinner('Gerando recomendações...'):
            response: str = album_recommender_chain.run(artists=user_input)
            st.write(response)

    except RateLimitError as e:
        print(e)
        st.markdown(
            e.code,
            """:red[Erro:] Você atingiu o limite de chamadas à API da OpenAI.
            """
        )
