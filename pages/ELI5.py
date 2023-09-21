import streamlit as st
from open_ai.llm_eli5 import eli5_chain
from openai.error import RateLimitError

st.title('Explain Like I\'m Five')
st.markdown(
    """
    :gray[Traduzido como ***Explique-me como se eu tivesse cinco anos***, o ELI5 é um método para explicar conceitos complexos
    de forma simplificada, utilizando analogias para que um público mais leigo em determinado assunto consiga
    entender com facilidade.]
    
    Aqui você pode inserir um assunto que deseja receber uma explicação como por exemplo "blockchain/bitcoins" ou alguma
    pergunta mais elaborada como "por que as nuvens se formam em uma determinada altura, e não na superfície?"
    """
)

user_input: str = st.text_input('Insira uma pergunta ou assunto')

if st.button("Explique!") and user_input:
    try:
        with st.spinner("Gerando explicação..."):
            response: str = eli5_chain.run(subject=user_input)
            st.write(response)

    except RateLimitError as e:
        print(e)