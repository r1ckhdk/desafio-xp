import streamlit as st
from openai.error import APIError, AuthenticationError, RateLimitError
from open_ai.ll_album_genius import album_recommender_chain

st.title(':cd: AlbumGenius')
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

    except APIError as e:
        st.markdown(
            ":red[**Erro**]: Houve um erro de API da OpenAI. Tente novamente em instantes."
        )
        print(e)

    except RateLimitError as e:
        st.markdown(
            ":red[**Erro**]: Você atingiu o limite de chamadas à API da OpenAI. Verifique sua cota de requisições."
        )
        print(e)

    except AuthenticationError as e:
        st.markdown(
            ":red[**Erro**]: Houve um erro de autenticação. Verifique sua chave API."
        )
        print(e)
