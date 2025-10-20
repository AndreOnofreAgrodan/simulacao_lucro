# ====================== FORMATADO COMO MILHAR =======================================

import streamlit as st

# ===== Função para formatação BR =====
def br(num, decimais=2):
    """Formata número para o padrão brasileiro: 1.234.567,89"""
    if num is None:
        return "-"
    return f"{num:,.{decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ===== Configuração da página =====
st.set_page_config(page_title="Simulações - E se?", layout="wide")

# ===== CSS customizado =====

# st.markdown("""
# <style>
#     .block-container {
#             padding-top: 1.2rem; padding-bottom: 0rem;
#         }
            
#     hr {
#         margin: 2px 0px;
#         }
            
#     h1 {
#         font-size: 1.8rem; margin-bottom: 0.5rem;
#         }
            
#     h2 {
#         font-size: 1.3rem; margin-bottom: 0.3rem;
#         }
            
#     h3 {
#         font-size: 1.1rem; margin-bottom: 0.2rem;
#         }
            
#     .stSlider {
#         margin-bottom: 0.2rem;}
#     .stNumberInput {margin-top: -0.5rem;}
#     div[data-testid="metric-container"] {padding: 0.3rem;}

# </style>
# """, unsafe_allow_html=True)

st.markdown("""
<style>
/* ======== Ajuste de espaçamento global ======== */
.block-container {
    padding-top: 1.4rem !important;
    padding-bottom: 0rem !important;
}

/* ======== Divider ======== */
hr {
    margin: 0.1rem 0rem !important;
    padding: 2px 0 5px 0 !important;
    border-width: 1px !important;
}

/* ======== Títulos ======== */
h1 {font-size: 1.8rem !important; margin-bottom: 0.4rem !important;}
h2 {font-size: 1.2rem !important; margin-bottom: 0.3rem !important;}
h3 {font-size: 1.0rem !important; margin-bottom: 0.2rem !important;}

/* ======== Sliders e inputs ======== */
.stSlider {margin-bottom: 0.2rem !important;}
.stNumberInput {margin-top: -0.4rem !important;}

/* ======== Métricas ======== */
div[data-testid="metric-container"] {
    margin: 0rem !important;
    padding: 0rem 0rem !important;
}
div[data-testid="stMetricLabel"] > div {
    font-size: 0.75rem !important;  /* diminui o texto da label */
}
div[data-testid="stMetricValue"] > div {
    font-size: 1.0rem !important;   /* diminui o número da métrica */
    line-height: 1.2rem !important;
}

/* ======== Cards customizados ======== */
div[data-testid="stMarkdownContainer"] > div {
    margin-bottom: 0rem !important;
}

/* ======== Cards principais ======== */
div.card-principal h3 {
    font-size: 1.8rem !important; /* aumenta o valor principal */
}
div.card-principal h5 {
    font-size: 2.0rem !important; /* título levemente maior */
}
</style>
""", unsafe_allow_html=True)


# ===== Título =====
st.title("🌾 Simulações - \"E se?\"")

# ===== Parâmetros fixos =====
AREA_TOTAL_HA = 964.46
peso_caixa_kg = 4.0

# ===== Sliders =====

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    produtividade = st.slider("Produtividade Ton/ha", 10.0, 50.0, 32.0, 0.5, key="s1")

with col2:
    preco_venda_euro = st.slider("Preço Venda (€/Cx)", 1.0, 10.0, 5.0, 0.1, key="s2")

with col3:
    cambio = st.slider("Câmbio (R$)", 3.0, 8.0, 6.0, 0.05, key="s3")

with col4:
    custo_campo = st.slider("R$/Kg Campo", 0.5, 5.0, 1.80, 0.1, key="s4")

with col5:
    refugo = st.slider("% Refugo", 0.01, 0.2, 0.05, 0.01, key="s5")

# ===== Segunda linha de sliders =====
col6, col7, col8, col9 = st.columns(4)

with col6:
    custo_packing = st.slider("R$/Cx Packing", 1.0, 15.0, 5.0, 0.1, key="s6")

with col7:
    desp_adm = st.slider("Desp. Adm (R$/Cx)", 0.0, 10.0, 2.30, 0.1, key="s7")

with col8:
    desp_financeira = st.slider("Desp. Financeira (R$/Cx)", 0.0, 10.0, 1.0, 0.1, key="s8")

with col9:
    valor_medio_folha = st.slider("Valor Médio Folha (R$)", 1_000_000.0, 5_000_000.0, 2_300_000.0, 50_000.0, key="s9")

st.divider()

# ===== Cálculos =====
producao_total_ton = AREA_TOTAL_HA * produtividade
producao_total_kg = producao_total_ton * 1000
qtd_caixas = (producao_total_kg / peso_caixa_kg) * (1 - refugo)
preco_caixa_reais = preco_venda_euro * cambio
faturamento_proporcional = qtd_caixas * preco_caixa_reais

custo_campo_total = producao_total_kg * custo_campo
custo_packing_total = qtd_caixas * custo_packing
desp_adm_total = qtd_caixas * desp_adm
desp_financeira_total = qtd_caixas * desp_financeira
custos_despesas_total = custo_campo_total + custo_packing_total + desp_adm_total + desp_financeira_total

lucro_liquido = faturamento_proporcional - custos_despesas_total
margem_liquida = (lucro_liquido / faturamento_proporcional * 100) if faturamento_proporcional > 0 else 0
participacao_resultados = (lucro_liquido * 0.10) / valor_medio_folha if valor_medio_folha > 0 else 0

# ===== Exibição dos resultados =====
col_r1, col_r2, col_r3 = st.columns(3)

with col_r1:
    st.markdown(f"""
    <div style='background-color: #1e7ba3; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Próprio</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(faturamento_proporcional, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.metric("📦 Caixas", f"{br(qtd_caixas, 0)}")

with col_r2:
    cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
    st.markdown(f"""
    <div style='background-color: {cor_lucro}; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Líquido</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_liquido, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.metric("📊 Margem Líquida", f"{br(margem_liquida, 1)}%")

with col_r3:
    st.markdown(f"""
    <div style='background-color: #812378; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>👥 PPR (10%)</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(participacao_resultados, 2)}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.metric("🌾 Produção", f"{br(producao_total_ton, 0)} ton")



# ===== Exibição dos resultados (4 colunas) =====
# col_r1, col_r2, col_r3, col_r4, col_r5 = st.columns([1, 1, 1, 0.7, 0.8])

# # ==== Coluna 1 - Faturamento ====
# with col_r1:
#     st.markdown(f"""
#     <div style='background-color: #1e7ba3; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Próprio</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(faturamento_proporcional, 0)}</h3>
#     </div>
#     """, unsafe_allow_html=True)

# # ==== Coluna 2 - Lucro Líquido ====
# with col_r2:
#     cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
#     st.markdown(f"""
#     <div style='background-color: {cor_lucro}; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Líquido</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_liquido, 0)}</h3>
#     </div>
#     """, unsafe_allow_html=True)

# # ==== Coluna 3 - PPR ====
# with col_r3:
#     st.markdown(f"""
#     <div style='background-color: #812378; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>👥 PPR (10%)</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(participacao_resultados, 2)}</h3>
#     </div>
#     """, unsafe_allow_html=True)

# # ==== Coluna 4 - Métricas empilhadas ====
# with col_r4:
#     st.metric("📦 Caixas", f"{br(qtd_caixas, 0)}")
#     st.metric("📊 Margem Líquida", f"{br(margem_liquida, 1)}%")

# with col_r5:
#     st.metric("🌾 Produção", f"{br(producao_total_ton, 0)} ton")




st.divider()

# ===== Detalhamento de custos =====
col_d1, col_d2, col_d3, col_d4, col_d5 = st.columns(5)

with col_d1:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo Campo</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custo_campo_total, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)

with col_d2:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo PH</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custo_packing_total, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)

with col_d3:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Desp. Financeira</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(desp_financeira_total, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)

with col_d4:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Adm. Sede</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(desp_adm_total, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)

with col_d5:
    st.markdown(f"""
    <div style='background-color: #d35400; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Total Custos</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custos_despesas_total, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)

# ===== Informações adicionais =====

st.divider()

st.info(f"""
**ℹ️ Informações da Simulação:**
- Área Total: {br(AREA_TOTAL_HA, 2)} ha  
- Peso por Caixa: {peso_caixa_kg} kg  
- Preço de Venda: €{br(preco_venda_euro, 2)}/cx = R$ {br(preco_caixa_reais, 2)}/cx  
- Caixas (automático): {br(qtd_caixas, 0)}  
- Kg Totais: {br(producao_total_kg, 2)}
""")
