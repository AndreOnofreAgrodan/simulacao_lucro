import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu App", layout="wide")

# Definir as páginas (AMBAS na mesma pasta "pages")
pages = [
    st.Page("pages/resumo.py", title="Simulação Resumida", icon="🌾"),
    st.Page("pages/detalhe.py", title="Simulação Detalhada", icon="📊"),
]

# Criar navegação (aparece na sidebar por padrão)
pg = st.navigation(pages, position="sidebar", expanded=True)

# Executar a página selecionada
pg.run()
