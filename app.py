# import streamlit as st

# # Configuração da página
# st.set_page_config(page_title="Simulações - E se?", layout="wide")

# # CSS customizado para interface compacta
# st.markdown("""
# <style>
#     .block-container {padding-top: 1.2rem; padding-bottom: 0rem;}
#     h1 {font-size: 1.8rem; margin-bottom: 0.5rem;}
#     h2 {font-size: 1.3rem; margin-bottom: 0.3rem;}
#     h3 {font-size: 1.1rem; margin-bottom: 0.2rem;}
#     .stSlider {margin-bottom: 0.3rem;}
#     .stNumberInput {margin-top: -0.5rem;}
#     div[data-testid="metric-container"] {padding: 0.3rem;}
# </style>
# """, unsafe_allow_html=True)

# # Título
# st.title("🌾 Simulações - \"E se?\"")

# # Área total fixa
# AREA_TOTAL_HA = 964.46

# # Primeira linha de sliders
# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     produtividade = st.slider("Produtividade Ton/ha", 10.0, 50.0, 32.0, 0.5, key="s1")
#     # produtividade = st.number_input("", value=produtividade, min_value=10.0, max_value=50.0, step=0.5, key="n1", label_visibility="collapsed")

# with col2:
#     preco_venda_euro = st.slider("Preço Venda (€/Cx)", 1.0, 10.0, 3.5, 0.1, key="s2")
#     # preco_venda_euro = st.number_input("", value=preco_venda_euro, min_value=1.0, max_value=10.0, step=0.1, key="n2", label_visibility="collapsed")

# with col3:
#     cambio = st.slider("Câmbio (R$)", 3.0, 8.0, 5.15, 0.05, key="s3")
#     # cambio = st.number_input("", value=cambio, min_value=3.0, max_value=8.0, step=0.05, key="n3", label_visibility="collapsed")

# with col4:
#     custo_campo = st.slider("R$/Kg Campo", 0.5, 5.0, 1.80, 0.1, key="s4")
#     # custo_campo = st.number_input("", value=custo_campo, min_value=0.5, max_value=5.0, step=0.1, key="n4", label_visibility="collapsed")


# with col5:
#     refugo = st.slider("% Refugo", 0.01, 0.2, 0.05, 0.01, key="s5")
#     # custo_campo = st.number_input("", value=custo_campo, min_value=0.5, max_value=5.0, step=0.1, key="n4", label_visibility="collapsed")


# # Segunda linha de sliders
# col6, col7, col8, col9 = st.columns(4)


# with col6:
#     custo_packing = st.slider("R$/Cx Packing", 1.0, 15.0, 4.60, 0.1, key="s6")
#     # custo_packing = st.number_input("", value=custo_packing, min_value=1.0, max_value=15.0, step=0.1, key="n5", label_visibility="collapsed")


# with col7:
#     desp_adm = st.slider("Desp. Adm (R$/Cx)", 0.0, 10.0, 2.32, 0.1, key="s7")
#     # desp_adm = st.number_input("", value=desp_adm, min_value=0.0, max_value=10.0, step=0.1, key="n6", label_visibility="collapsed")

# with col8:
#     desp_financeira = st.slider("Desp. Financeira (R$/Cx)", 0.0, 10.0, 2.89, 0.1, key="s8")
#     # desp_financeira = st.number_input("", value=desp_financeira, min_value=0.0, max_value=10.0, step=0.1, key="n7", label_visibility="collapsed")

# with col9:
#     valor_medio_folha = st.slider("Valor Médio Folha (R$)", 1000000.0, 5000000.0, 3000000.0, 50000.0, key="s9")
#     # valor_medio_folha = st.number_input("", value=valor_medio_folha, min_value=1000000.0, max_value=5000000.0, step=50000.0, key="n8", label_visibility="collapsed")

# st.divider()

# # CÁLCULOS
# peso_caixa_kg = 4.0
# producao_total_ton = AREA_TOTAL_HA * produtividade
# producao_total_kg = producao_total_ton * 1000
# qtd_caixas = (producao_total_kg / peso_caixa_kg) - ((producao_total_kg / peso_caixa_kg) * refugo)  # Abatendo 5% de Refugo
# preco_caixa_reais = preco_venda_euro * cambio
# faturamento_proporcional = qtd_caixas * preco_caixa_reais

# custo_campo_total = producao_total_kg * custo_campo
# custo_packing_total = qtd_caixas * custo_packing
# desp_adm_total = qtd_caixas * desp_adm
# desp_financeira_total = qtd_caixas * desp_financeira
# custos_despesas_total = custo_campo_total + custo_packing_total + desp_adm_total + desp_financeira_total

# lucro_liquido = faturamento_proporcional - custos_despesas_total
# margem_liquida = (lucro_liquido / faturamento_proporcional * 100) if faturamento_proporcional > 0 else 0
# participacao_resultados = (lucro_liquido * 0.10) / valor_medio_folha if valor_medio_folha > 0 else 0

# # Exibição dos resultados - Layout compacto
# col_r1, col_r2, col_r3 = st.columns(3)

# with col_r1:
#     st.markdown(f"""
#     <div style='background-color: #2d5016; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Prop.</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {faturamento_proporcional:,.0f}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.metric("📦 Caixas", f"{qtd_caixas:,.0f}", label_visibility="visible")

# with col_r2:
#     cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
#     st.markdown(f"""
#     <div style='background-color: {cor_lucro}; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Líquido</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {lucro_liquido:,.0f}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.metric("📊 Margem Líquida", f"{margem_liquida:.1f}%")

# with col_r3:
#     st.markdown(f"""
#     <div style='background-color: #1e7ba3; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>👥 Participação 10%</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{participacao_resultados:.2f}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.metric("🌾 Produção", f"{producao_total_ton:,.0f} ton")

# st.divider()

# # Detalhamento de custos - mais compacto
# col_d1, col_d2, col_d3, col_d4, col_d5 = st.columns(5)

# with col_d1:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo Campo</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {custo_campo_total:,.0f}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d2:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo PH</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {custo_packing_total:,.0f}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d3:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Desp. Financeira</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {desp_financeira_total:,.0f}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d4:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Adm. Sede</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {desp_adm_total:,.0f}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d5:
#     st.markdown(f"""
#     <div style='background-color: #d35400; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Total Custos</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {custos_despesas_total:,.0f}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# # Informações adicionais
# st.divider()
# st.info(f"""
# **ℹ️ Informações da Simulação:**
# - Área Total: {AREA_TOTAL_HA} ha
# - Peso por Caixa: {peso_caixa_kg} kg
# - Preço de Venda: €{preco_venda_euro:.2f}/cx = R$ {preco_caixa_reais:.2f}/cx
# - Caixas (automático): {qtd_caixas:,.0f}
# - Kg Totais: {producao_total_kg:,.2f}
# """)













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
st.markdown("""
<style>
    .block-container {padding-top: 1.2rem; padding-bottom: 0rem;}
    h1 {font-size: 1.8rem; margin-bottom: 0.5rem;}
    h2 {font-size: 1.3rem; margin-bottom: 0.3rem;}
    h3 {font-size: 1.1rem; margin-bottom: 0.2rem;}
    .stSlider {margin-bottom: 0.3rem;}
    .stNumberInput {margin-top: -0.5rem;}
    div[data-testid="metric-container"] {padding: 0.3rem;}
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
    preco_venda_euro = st.slider("Preço Venda (€/Cx)", 1.0, 10.0, 3.5, 0.1, key="s2")

with col3:
    cambio = st.slider("Câmbio (R$)", 3.0, 8.0, 5.15, 0.05, key="s3")

with col4:
    custo_campo = st.slider("R$/Kg Campo", 0.5, 5.0, 1.80, 0.1, key="s4")

with col5:
    refugo = st.slider("% Refugo", 0.01, 0.2, 0.05, 0.01, key="s5")

# ===== Segunda linha de sliders =====
col6, col7, col8, col9 = st.columns(4)

with col6:
    custo_packing = st.slider("R$/Cx Packing", 1.0, 15.0, 4.60, 0.1, key="s6")

with col7:
    desp_adm = st.slider("Desp. Adm (R$/Cx)", 0.0, 10.0, 2.32, 0.1, key="s7")

with col8:
    desp_financeira = st.slider("Desp. Financeira (R$/Cx)", 0.0, 10.0, 2.89, 0.1, key="s8")

with col9:
    valor_medio_folha = st.slider("Valor Médio Folha (R$)", 1_000_000.0, 5_000_000.0, 3_000_000.0, 50_000.0, key="s9")

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
    <div style='background-color: #2d5016; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Prop.</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(faturamento_proporcional, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.metric("📦 Caixas", f"{br(qtd_caixas, 0)}")

with col_r2:
    cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
    st.markdown(f"""
    <div style='background-color: {cor_lucro}; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Líquido</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_liquido, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.metric("📊 Margem Líquida", f"{br(margem_liquida, 1)}%")

with col_r3:
    st.markdown(f"""
    <div style='background-color: #1e7ba3; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>👥 Participação 10%</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(participacao_resultados, 2)}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.metric("🌾 Produção", f"{br(producao_total_ton, 0)} ton")

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
