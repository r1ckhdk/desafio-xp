import streamlit as st
from openai.error import APIError, AuthenticationError, RateLimitError
from open_ai.llm_eli5 import eli5_chain

st.title(':memo: Explain Like I\'m Five')
st.markdown(
    """
    :gray[Traduzido como ***Explique-me como se eu tivesse cinco anos***, o ELI5 é um método para explicar conceitos complexos
    de forma simplificada, utilizando analogias para que um público mais leigo em determinado assunto consiga
    entender com facilidade.]
    
    Aqui você pode inserir um assunto que deseja receber uma explicação como por exemplo "estoicismo" ou alguma
    pergunta mais elaborada como "por que as nuvens se formam em uma determinada altura, e não na superfície?"
    """
)

user_input: str = st.text_input('Insira uma pergunta ou assunto')

if st.button('Enviar!') and user_input:
    try:
        with st.spinner("Gerando explicação..."):
            response: str = eli5_chain.run(subject=user_input)
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
