# import streamlit as st

# # ===== Função para formatação BR =====
# def br(num, decimais=2):
#     """Formata número para o padrão brasileiro: 1.234.567,89"""
#     if num is None:
#         return "-"
#     return f"{num:,.{decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")

# # ===== Configuração da página =====
# st.set_page_config(page_title="Simulações - E se?", layout="wide")

# # ===== CSS customizado =====
# st.markdown("""
# <style>
# .block-container {
#     padding-top: 1.4rem !important;
#     padding-bottom: 0rem !important;
# }
# hr {
#     margin: 0.1rem 0rem !important;
#     padding: 2px 0 5px 0 !important;
#     border-width: 1px !important;
# }
# h1 {font-size: 1.8rem !important; margin-bottom: 0.4rem !important;}
# h2 {font-size: 1.2rem !important; margin-bottom: 0.3rem !important;}
# h3 {font-size: 1.0rem !important; margin-bottom: 0.2rem !important;}
# .stSlider {margin-bottom: 0.2rem !important;}
# .stNumberInput {margin-top: -0.4rem !important;}
# div[data-testid="metric-container"] {
#     margin: 0rem !important;
#     padding: 0rem 0rem !important;
# }
# div[data-testid="stMetricLabel"] > div {
#     font-size: 0.75rem !important;
# }
# div[data-testid="stMetricValue"] > div {
#     font-size: 1.0rem !important;
#     line-height: 1.2rem !important;
# }
# div[data-testid="stMarkdownContainer"] > div {
#     margin-bottom: 0rem !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # ===== Título =====
# st.title("🌾 Simulações - \"E se?\" (Ago-Dez)")

# st.info("ℹ️ **Os dados de Jan-Jul são FIXOS (realizados). Os sliders abaixo afetam apenas a projeção de Ago-Dez.**")

# # ===== DADOS REALIZADOS (Jan-Jul) - FIXOS =====
# ORCAMENTO_JAN_JUL = 68_737_354.00
# CUSTO_CAMPO_REALIZADO = 25_496_393.97
# CUSTO_PH_REALIZADO = 16_038_318.32
# CUSTO_ADM_REALIZADO = 7_641_942.00
# DESP_FINANCEIRA_REALIZADA = 2_699_257.00
# CAIXAS_REALIZADAS = 2_699_257.00
# CUSTO_TOTAL_JAN_JUL = 51_875_911.28
# LUCRO_JAN_JUL = 16_861_442.72

# # ===== Parâmetros fixos conforme tabela do print =====
# AREA_TOTAL_HA = 962.70
# HECTARES_FECHADOS = 390.51
# HECTARES_RESTANTES = 573.32
# peso_caixa_kg = 4.0
# PRODUTIVIDADE_MEDIA_JAN_JUL = 31.23
# REFUGO_DEFAULT = 0.0808
# VALOR_MEDIO_CAIXA_JAN_JUL = 25.47
# TON_PREV_AGO_DEZ_BRUTO = 18_007.40  # BRUTO (sem refugo aplicado)
# TON_PREV_POR_HECTARE = 31.41
# CAIXAS_PREVISTAS_AGO_DEZ_BRUTO = 4_501_850.00

# # ===== Sliders para simulação Ago-Dez =====
# st.subheader("📊 Parâmetros para Simulação Ago-Dez")

# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     produtividade = st.slider(
#         "Produtividade Ton/ha", 
#         10.0, 50.0, TON_PREV_POR_HECTARE, 0.01, key="s1"
#     )

# with col2:
#     preco_venda_euro = st.slider("Preço Venda (€/Cx)", 1.0, 10.0, 5.0, 0.1, key="s2")

# with col3:
#     cambio = st.slider("Câmbio (R$)", 3.0, 8.0, 6.0, 0.05, key="s3")

# with col4:
#     custo_campo = st.slider("R$/Kg Campo", 0.5, 5.0, 1.80, 0.1, key="s4")

# with col5:
#     refugo = st.slider("% Refugo", 0.01, 0.20, REFUGO_DEFAULT, 0.01, key="s5")

# col6, col7, col8, col9 = st.columns(4)

# with col6:
#     custo_packing = st.slider("R$/Cx Packing", 1.0, 15.0, 5.94, 0.1, key="s6")

# with col7:
#     desp_adm = st.slider("Desp. Adm (R$/Cx)", 0.0, 10.0, 2.83, 0.1, key="s7")

# with col8:
#     desp_financeira = st.slider("Desp. Financeira (R$/Cx)", 0.0, 10.0, 1.0, 0.1, key="s8")

# with col9:
#     valor_medio_folha = st.slider("Valor Médio Folha (R$)", 1_000_000.0, 5_000_000.0, 2_300_000.0, 50_000.0, key="s9")

# st.divider()

# # ===== Cálculos AGO-DEZ =====
# producao_ago_dez_ton_bruta = HECTARES_RESTANTES * produtividade
# producao_ago_dez_kg_bruta = producao_ago_dez_ton_bruta * 1000
# producao_ago_dez_ton_liquida = producao_ago_dez_ton_bruta * (1 - refugo)
# producao_ago_dez_kg_liquida = producao_ago_dez_ton_liquida * 1000
# qtd_caixas_ago_dez = producao_ago_dez_kg_liquida / peso_caixa_kg

# preco_caixa_reais = preco_venda_euro * cambio
# faturamento_ago_dez = qtd_caixas_ago_dez * preco_caixa_reais

# custo_campo_ago_dez = producao_ago_dez_kg_bruta * custo_campo
# custo_packing_ago_dez = qtd_caixas_ago_dez * custo_packing
# desp_adm_ago_dez = qtd_caixas_ago_dez * desp_adm
# desp_financeira_ago_dez = qtd_caixas_ago_dez * desp_financeira
# custos_ago_dez = custo_campo_ago_dez + custo_packing_ago_dez + desp_adm_ago_dez + desp_financeira_ago_dez

# lucro_ago_dez = faturamento_ago_dez - custos_ago_dez

# # ===== TOTAIS DO ANO (Realizado + Projetado) =====
# faturamento_total_ano = ORCAMENTO_JAN_JUL + faturamento_ago_dez
# custo_campo_total_ano = CUSTO_CAMPO_REALIZADO + custo_campo_ago_dez
# custo_packing_total_ano = CUSTO_PH_REALIZADO + custo_packing_ago_dez
# desp_adm_total_ano = CUSTO_ADM_REALIZADO + desp_adm_ago_dez
# desp_financeira_total_ano = DESP_FINANCEIRA_REALIZADA + desp_financeira_ago_dez
# custos_total_ano = custo_campo_total_ano + custo_packing_total_ano + desp_adm_total_ano + desp_financeira_total_ano

# caixas_total_ano = CAIXAS_REALIZADAS + qtd_caixas_ago_dez
# producao_jan_jul_ton = HECTARES_FECHADOS * PRODUTIVIDADE_MEDIA_JAN_JUL
# producao_total_ano_bruta = producao_jan_jul_ton + producao_ago_dez_ton_bruta
# producao_total_ano_liquida = producao_jan_jul_ton + producao_ago_dez_ton_liquida

# lucro_liquido_ano = faturamento_total_ano - custos_total_ano
# margem_liquida_ano = (lucro_liquido_ano / faturamento_total_ano * 100) if faturamento_total_ano > 0 else 0
# participacao_resultados = (lucro_liquido_ano * 0.10) / valor_medio_folha if valor_medio_folha > 0 else 0

# # ===== Cálculos REALIZADO JAN-JUL =====
# lucro_jan_jul = ORCAMENTO_JAN_JUL - (CUSTO_CAMPO_REALIZADO + CUSTO_PH_REALIZADO + CUSTO_ADM_REALIZADO + DESP_FINANCEIRA_REALIZADA)
# margem_jan_jul = (lucro_jan_jul / ORCAMENTO_JAN_JUL * 100) if ORCAMENTO_JAN_JUL > 0 else 0

# # ===== Exibição - REALIZADO JAN-JUL =====
# st.subheader("✅ Realizado Jan-Jul")

# col_j1, col_j2, col_j3 = st.columns(3)

# with col_j1:
#     st.markdown(f"""
#     <div style='background-color: #4a6741; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Jan-Jul</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(ORCAMENTO_JAN_JUL, 0)}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.divider()
#     st.metric("📦 Caixas Jan-Jul", f"{br(CAIXAS_REALIZADAS, 0)}")

# with col_j2:
#     cor_lucro_jan = "#2d5016" if lucro_jan_jul >= 0 else "#8B0000"
#     st.markdown(f"""
#     <div style='background-color: {cor_lucro_jan}; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Jan-Jul</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_jan_jul, 0)}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.divider()
#     st.metric("📊 Margem Jan-Jul", f"{br(margem_jan_jul, 1)}%")

# with col_j3:
#     st.markdown(f"""
#     <div style='background-color: #6b5d43; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>🌾 Produção Jan-Jul</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(producao_jan_jul_ton, 0)} ton</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.divider()
#     st.metric("🏞️ Hectares Fechados", f"{br(HECTARES_FECHADOS, 2)} ha")

# st.divider()

# # ===== Exibição - PROJEÇÃO AGO-DEZ =====
# st.subheader("📅 Projeção Ago-Dez")

# col_a1, col_a2, col_a3 = st.columns(3)

# with col_a1:
#     st.markdown(f"""
#     <div style='background-color: #5a7d9a; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Ago-Dez</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(faturamento_ago_dez, 0)}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.divider()
#     st.metric("📦 Caixas Ago-Dez", f"{br(qtd_caixas_ago_dez, 0)}")

# with col_a2:
#     cor_lucro = "#2d5016" if lucro_ago_dez >= 0 else "#8B0000"
#     st.markdown(f"""
#     <div style='background-color: {cor_lucro}; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Ago-Dez</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_ago_dez, 0)}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.divider()
#     margem_ago_dez = (lucro_ago_dez / faturamento_ago_dez * 100) if faturamento_ago_dez > 0 else 0
#     st.metric("📊 Margem Ago-Dez", f"{br(margem_ago_dez, 1)}%")

# with col_a3:
#     st.markdown(f"""
#     <div style='background-color: #7a6a4d; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>🌾 Produção Ago-Dez</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(producao_ago_dez_ton_liquida, 0)} ton</h3>
#         <!--<p style='color: white; margin: 0; font-size: 0.7rem;'>({br(producao_ago_dez_ton_bruta, 0)} ton bruta)</p>-->
#     </div>
#     """, unsafe_allow_html=True)
#     st.divider()
#     st.metric("🏞️ Hectares Restantes", f"{br(HECTARES_RESTANTES, 2)} ha")

# st.divider()

# # ===== Exibição - RESULTADO TOTAL DO ANO =====
# st.subheader("📈 Total Ano (Jan-Dez)")

# col_r1, col_r2, col_r3 = st.columns(3)

# with col_r1:
#     st.markdown(f"""
#     <div style='background-color: #1e7ba3; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Total Ano</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(faturamento_total_ano, 0)}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.divider()
#     st.metric("📦 Caixas Totais Ano", f"{br(caixas_total_ano, 0)}")

# with col_r2:
#     cor_lucro_ano = "#2d5016" if lucro_liquido_ano >= 0 else "#8B0000"
#     st.markdown(f"""
#     <div style='background-color: {cor_lucro_ano}; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Líquido Ano</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_liquido_ano, 0)}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.divider()
#     st.metric("📊 Margem Líquida Ano", f"{br(margem_liquida_ano, 1)}%")

# with col_r3:
#     st.markdown(f"""
#     <div style='background-color: #812378; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>👥 PPR (10%)</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(participacao_resultados, 2)}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.divider()
#     st.metric("🌾 Produção Total Ano", f"{br(producao_total_ano_liquida, 0)} ton")

# st.divider()

# # ===== Detalhamento de custos TOTAIS DO ANO =====
# st.subheader("📋 Custos e Despesas Totais do Ano")

# col_d1, col_d2, col_d3, col_d4, col_d5 = st.columns(5)

# with col_d1:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo Campo</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custo_campo_total_ano, 0)}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d2:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo PH</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custo_packing_total_ano, 0)}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d3:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Desp. Financeira</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(desp_financeira_total_ano, 0)}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d4:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Adm. Sede</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(desp_adm_total_ano, 0)}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d5:
#     st.markdown(f"""
#     <div style='background-color: #d35400; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Total Custos</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custos_total_ano, 0)}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# st.divider()

# # ===== Informações adicionais =====
# st.info(f"""
# **ℹ️ Informações da Simulação:**
# - Área Total: {br(AREA_TOTAL_HA, 2)} ha | Hectares Fechados (Jan-Jul): {br(HECTARES_FECHADOS, 2)} ha | Hectares Restantes (Ago-Dez): {br(HECTARES_RESTANTES, 2)} ha
# - Peso por Caixa: {peso_caixa_kg} kg | Refugo: {br(refugo * 100, 2)}%
# - Preço de Venda: €{br(preco_venda_euro, 2)}/cx = R$ {br(preco_caixa_reais, 2)}/cx
# - Produtividade Ago-Dez: {br(produtividade, 2)} ton/ha
# - Produção Ago-Dez: {br(producao_ago_dez_ton_bruta, 0)} ton bruta → {br(producao_ago_dez_ton_liquida, 0)} ton líquida
# - Caixas Realizadas (Jan-Jul): {br(CAIXAS_REALIZADAS, 0)} | Caixas Projetadas (Ago-Dez): {br(qtd_caixas_ago_dez, 0)} | **Total Ano: {br(caixas_total_ano, 0)}**
# """)






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
.block-container {
    padding-top: 1.4rem !important;
    padding-bottom: 0rem !important;
}
hr {
    margin: 0.1rem 0rem !important;
    padding: 2px 0 5px 0 !important;
    border-width: 1px !important;
}
h1 {font-size: 1.8rem !important; margin-bottom: 0.4rem !important;}
h2 {font-size: 1.2rem !important; margin-bottom: 0.3rem !important;}
h3 {font-size: 1.0rem !important; margin-bottom: 0.2rem !important;}
.stNumberInput {margin-bottom: 0.5rem !important;}
div[data-testid="metric-container"] {
    margin: 0rem !important;
    padding: 0rem 0rem !important;
}
div[data-testid="stMetricLabel"] > div {
    font-size: 0.75rem !important;
}
div[data-testid="stMetricValue"] > div {
    font-size: 1.0rem !important;
    line-height: 1.2rem !important;
}
div[data-testid="stMarkdownContainer"] > div {
    margin-bottom: 0rem !important;
}
</style>
""", unsafe_allow_html=True)


# ===== Título =====
st.title("🌾 Simulações - \"E se?\" (Ago-Dez)")


st.info("ℹ️ **Os dados de Jan-Jul são FIXOS (realizados). Os inputs abaixo afetam apenas a projeção de Ago-Dez.**")


# ===== DADOS REALIZADOS (Jan-Jul) - FIXOS =====
ORCAMENTO_JAN_JUL = 68_737_354.00
CUSTO_CAMPO_REALIZADO = 25_496_393.97
CUSTO_PH_REALIZADO = 16_038_318.32
CUSTO_ADM_REALIZADO = 7_641_942.00
DESP_FINANCEIRA_REALIZADA = 2_699_257.00
CAIXAS_REALIZADAS = 2_699_257.00
CUSTO_TOTAL_JAN_JUL = 51_875_911.28
LUCRO_JAN_JUL = 16_861_442.72


# ===== Parâmetros fixos conforme tabela do print =====
AREA_TOTAL_HA = 962.70
HECTARES_FECHADOS = 390.51
HECTARES_RESTANTES = 573.32
peso_caixa_kg = 4.0
PRODUTIVIDADE_MEDIA_JAN_JUL = 31.23
REFUGO_DEFAULT = 0.0808
VALOR_MEDIO_CAIXA_JAN_JUL = 25.47
TON_PREV_AGO_DEZ_BRUTO = 18_007.40  # BRUTO (sem refugo aplicado)
TON_PREV_POR_HECTARE = 31.00
CAIXAS_PREVISTAS_AGO_DEZ_BRUTO = 4_501_850.00


# ===== Inputs para simulação Ago-Dez =====
st.subheader("📊 Parâmetros para Simulação Ago-Dez")


col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    # Input para produtividade em toneladas por hectare
    produtividade = st.number_input(
        "Produtividade Ton/ha", 
        min_value=10.0, 
        max_value=50.0, 
        value=TON_PREV_POR_HECTARE, 
        step=0.01,
        format="%.2f"
    )


with col2:
    # Input para preço de venda em euros por caixa
    preco_venda_euro = st.number_input(
        "Preço Venda (€/Cx)", 
        min_value=1.0,
        max_value=10.0,
        value=4.5,
        step=0.1,
        format="%.2f"
    )


with col3:
    # Input para taxa de câmbio em reais
    cambio = st.number_input(
        "Câmbio (R$)", 
        min_value=3.0, 
        max_value=8.0, 
        value=6.0, 
        step=0.05,
        format="%.2f"
    )


with col4:
    # Input para custo de campo em reais por kg
    custo_campo = st.number_input(
        "R$/Kg Campo", 
        min_value=0.5, 
        max_value=5.0, 
        value=1.90, 
        step=0.1,
        format="%.2f"
    )


with col5:
    # Input para percentual de refugo
    refugo = st.number_input(
        "% Refugo", 
        min_value=0.01, 
        max_value=0.20, 
        value=REFUGO_DEFAULT, 
        step=0.01,
        format="%.4f"
    )


col6, col7, col8, col9 = st.columns(4)


with col6:
    # Input para custo de packing em reais por caixa
    custo_packing = st.number_input(
        "R$/Cx Packing", 
        min_value=1.0, 
        max_value=15.0, 
        value=4.9, 
        step=0.1,
        format="%.2f"
    )


with col7:
    # Input para despesa administrativa em reais por caixa
    desp_adm = st.number_input(
        "Desp. Adm (R$/Cx)", 
        min_value=0.0, 
        max_value=10.0, 
        value=2.3, 
        step=0.1,
        format="%.2f"
    )


with col8:
    # Input para despesa financeira em reais por caixa
    desp_financeira = st.number_input(
        "Desp. Financeira (R$/Cx)", 
        min_value=0.0, 
        max_value=10.0, 
        value=1.0, 
        step=0.1,
        format="%.2f"
    )


with col9:
    # Input para valor médio da folha de pagamento em reais
    valor_medio_folha = st.number_input(
        "Valor Médio Folha (R$)", 
        min_value=1_000_000.0, 
        max_value=5_000_000.0, 
        value=2_200_000.0, 
        step=50_000.0,
        format="%.0f"
    )


st.divider()


# ===== Cálculos AGO-DEZ =====

# Calcula a produção bruta de Ago-Dez em toneladas (sem descontar refugo)
producao_ago_dez_ton_bruta = HECTARES_RESTANTES * produtividade

# Converte a produção bruta para kg
producao_ago_dez_kg_bruta = producao_ago_dez_ton_bruta * 1000

# Calcula a produção líquida descontando o refugo
producao_ago_dez_ton_liquida = producao_ago_dez_ton_bruta * (1 - refugo)

# Converte a produção líquida para kg
producao_ago_dez_kg_liquida = producao_ago_dez_ton_liquida * 1000

# Calcula a quantidade de caixas com base na produção líquida
qtd_caixas_ago_dez = producao_ago_dez_kg_liquida / peso_caixa_kg


# Calcula o preço da caixa em reais (conversão de euros)
preco_caixa_reais = preco_venda_euro * cambio

# Calcula o faturamento de Ago-Dez
faturamento_ago_dez = qtd_caixas_ago_dez * preco_caixa_reais


# Calcula os custos de campo para Ago-Dez (baseado na produção bruta em kg)
custo_campo_ago_dez = producao_ago_dez_kg_bruta * custo_campo

# Calcula o custo de packing para Ago-Dez
custo_packing_ago_dez = qtd_caixas_ago_dez * custo_packing

# Calcula a despesa administrativa para Ago-Dez
desp_adm_ago_dez = qtd_caixas_ago_dez * desp_adm

# Calcula a despesa financeira para Ago-Dez
desp_financeira_ago_dez = qtd_caixas_ago_dez * desp_financeira

# Soma todos os custos de Ago-Dez
custos_ago_dez = custo_campo_ago_dez + custo_packing_ago_dez + desp_adm_ago_dez + desp_financeira_ago_dez


# Calcula o lucro de Ago-Dez
lucro_ago_dez = faturamento_ago_dez - custos_ago_dez


# ===== TOTAIS DO ANO (Realizado + Projetado) =====

# Calcula o faturamento total do ano (Jan-Jul realizado + Ago-Dez projetado)
faturamento_total_ano = ORCAMENTO_JAN_JUL + faturamento_ago_dez

# Calcula o custo de campo total do ano
custo_campo_total_ano = CUSTO_CAMPO_REALIZADO + custo_campo_ago_dez

# Calcula o custo de packing total do ano
custo_packing_total_ano = CUSTO_PH_REALIZADO + custo_packing_ago_dez

# Calcula a despesa administrativa total do ano
desp_adm_total_ano = CUSTO_ADM_REALIZADO + desp_adm_ago_dez

# Calcula a despesa financeira total do ano
desp_financeira_total_ano = DESP_FINANCEIRA_REALIZADA + desp_financeira_ago_dez

# Calcula o total de custos do ano
custos_total_ano = custo_campo_total_ano + custo_packing_total_ano + desp_adm_total_ano + desp_financeira_total_ano


# Calcula o total de caixas do ano
caixas_total_ano = CAIXAS_REALIZADAS + qtd_caixas_ago_dez

# Calcula a produção de Jan-Jul em toneladas
producao_jan_jul_ton = HECTARES_FECHADOS * PRODUTIVIDADE_MEDIA_JAN_JUL

# Calcula a produção total do ano (bruta)
producao_total_ano_bruta = producao_jan_jul_ton + producao_ago_dez_ton_bruta

# Calcula a produção total do ano (líquida)
producao_total_ano_liquida = producao_jan_jul_ton + producao_ago_dez_ton_liquida


# Calcula o lucro líquido do ano
lucro_liquido_ano = faturamento_total_ano - custos_total_ano

# Calcula a margem líquida do ano em percentual
margem_liquida_ano = (lucro_liquido_ano / faturamento_total_ano * 100) if faturamento_total_ano > 0 else 0

# Calcula a participação nos resultados (PPR) - 10% do lucro dividido pela folha média
participacao_resultados = (lucro_liquido_ano * 0.10) / valor_medio_folha if valor_medio_folha > 0 else 0


# ===== Cálculos REALIZADO JAN-JUL =====

# Calcula o lucro de Jan-Jul (realizado)
lucro_jan_jul = ORCAMENTO_JAN_JUL - (CUSTO_CAMPO_REALIZADO + CUSTO_PH_REALIZADO + CUSTO_ADM_REALIZADO + DESP_FINANCEIRA_REALIZADA)

# Calcula a margem líquida de Jan-Jul em percentual
margem_jan_jul = (lucro_jan_jul / ORCAMENTO_JAN_JUL * 100) if ORCAMENTO_JAN_JUL > 0 else 0


# ===== Exibição - REALIZADO JAN-JUL =====
st.subheader("✅ Realizado Jan-Jul")


col_j1, col_j2, col_j3 = st.columns(3)


with col_j1:
    st.markdown(f"""
    <div style='background-color: #4a6741; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Jan-Jul</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(ORCAMENTO_JAN_JUL, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.metric("📦 Caixas Jan-Jul", f"{br(CAIXAS_REALIZADAS, 0)}")


with col_j2:
    # Define a cor do card de lucro (verde se positivo, vermelho se negativo)
    cor_lucro_jan = "#2d5016" if lucro_jan_jul >= 0 else "#8B0000"
    st.markdown(f"""
    <div style='background-color: {cor_lucro_jan}; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Jan-Jul</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_jan_jul, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.metric("📊 Margem Jan-Jul", f"{br(margem_jan_jul, 1)}%")


with col_j3:
    st.markdown(f"""
    <div style='background-color: #6b5d43; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>🌾 Produção Jan-Jul</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(producao_jan_jul_ton, 0)} ton</h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.metric("🏞️ Hectares Fechados", f"{br(HECTARES_FECHADOS, 2)} ha")


st.divider()


# ===== Exibição - PROJEÇÃO AGO-DEZ =====
st.subheader("📅 Projeção Ago-Dez")


col_a1, col_a2, col_a3 = st.columns(3)


with col_a1:
    st.markdown(f"""
    <div style='background-color: #5a7d9a; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Ago-Dez</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(faturamento_ago_dez, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.metric("📦 Caixas Ago-Dez", f"{br(qtd_caixas_ago_dez, 0)}")


with col_a2:
    # Define a cor do card de lucro (verde se positivo, vermelho se negativo)
    cor_lucro = "#2d5016" if lucro_ago_dez >= 0 else "#8B0000"
    st.markdown(f"""
    <div style='background-color: {cor_lucro}; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Ago-Dez</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_ago_dez, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    # Calcula a margem líquida de Ago-Dez em percentual
    margem_ago_dez = (lucro_ago_dez / faturamento_ago_dez * 100) if faturamento_ago_dez > 0 else 0
    st.metric("📊 Margem Ago-Dez", f"{br(margem_ago_dez, 1)}%")


with col_a3:
    st.markdown(f"""
    <div style='background-color: #7a6a4d; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>🌾 Produção Ago-Dez</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(producao_ago_dez_ton_liquida, 0)} ton</h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.metric("🏞️ Hectares Restantes", f"{br(HECTARES_RESTANTES, 2)} ha")


st.divider()


# ===== Exibição - RESULTADO TOTAL DO ANO =====
st.subheader("📈 Total Ano (Jan-Dez)")


col_r1, col_r2, col_r3 = st.columns(3)


with col_r1:
    st.markdown(f"""
    <div style='background-color: #1e7ba3; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Total Ano</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(faturamento_total_ano, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.metric("📦 Caixas Totais Ano", f"{br(caixas_total_ano, 0)}")


with col_r2:
    # Define a cor do card de lucro anual (verde se positivo, vermelho se negativo)
    cor_lucro_ano = "#2d5016" if lucro_liquido_ano >= 0 else "#8B0000"
    st.markdown(f"""
    <div style='background-color: {cor_lucro_ano}; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Líquido Ano</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_liquido_ano, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.metric("📊 Margem Líquida Ano", f"{br(margem_liquida_ano, 1)}%")


with col_r3:
    st.markdown(f"""
    <div style='background-color: #812378; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>👥 PPR (10%)</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(participacao_resultados, 2)}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.metric("🌾 Produção Total Ano", f"{br(producao_total_ano_liquida, 0)} ton")


st.divider()


# ===== Detalhamento de custos TOTAIS DO ANO =====
st.subheader("📋 Custos e Despesas Totais do Ano")


col_d1, col_d2, col_d3, col_d4, col_d5 = st.columns(5)


with col_d1:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo Campo</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custo_campo_total_ano, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)


with col_d2:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo PH</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custo_packing_total_ano, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)


with col_d3:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Desp. Financeira</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(desp_financeira_total_ano, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)


with col_d4:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Adm. Sede</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(desp_adm_total_ano, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)


with col_d5:
    st.markdown(f"""
    <div style='background-color: #d35400; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Total Custos</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custos_total_ano, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)


st.divider()


# ===== Informações adicionais =====
st.info(f"""
**ℹ️ Informações da Simulação:**
- Área Total: {br(AREA_TOTAL_HA, 2)} ha | Hectares Fechados (Jan-Jul): {br(HECTARES_FECHADOS, 2)} ha | Hectares Restantes (Ago-Dez): {br(HECTARES_RESTANTES, 2)} ha
- Peso por Caixa: {peso_caixa_kg} kg | Refugo: {br(refugo * 100, 2)}%
- Preço de Venda: €{br(preco_venda_euro, 2)}/cx = R$ {br(preco_caixa_reais, 2)}/cx
- Produtividade Ago-Dez: {br(produtividade, 2)} ton/ha
- Produção Ago-Dez: {br(producao_ago_dez_ton_bruta, 0)} ton bruta → {br(producao_ago_dez_ton_liquida, 0)} ton líquida
- Caixas Realizadas (Jan-Jul): {br(CAIXAS_REALIZADAS, 0)} | Caixas Projetadas (Ago-Dez): {br(qtd_caixas_ago_dez, 0)} | **Total Ano: {br(caixas_total_ano, 0)}**
""")
