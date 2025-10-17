# import streamlit as st

# # Configuração da página
# st.set_page_config(page_title="Simulações - E se?", layout="wide")

# # Título
# st.title("🌾 Simulações - \"E se?\"")

# # Área total fixa
# AREA_TOTAL_HA = 964.46

# # Criar colunas para os sliders
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     produtividade = st.slider(
#         "Produtividade Ton/ha",
#         min_value=10.0,
#         max_value=50.0,
#         value=32.0,
#         step=0.5
#     )

# with col2:
#     preco_venda_euro = st.slider(
#         "Preço de Venda (€/Cx)",
#         min_value=1.0,
#         max_value=10.0,
#         value=3.5,
#         step=0.1
#     )

# with col3:
#     cambio = st.slider(
#         "Câmbio (R$)",
#         min_value=3.0,
#         max_value=8.0,
#         value=5.15,
#         step=0.05
#     )

# with col4:
#     custo_campo = st.slider(
#         "R$/Kg Campo",
#         min_value=0.5,
#         max_value=5.0,
#         value=1.80,
#         step=0.1
#     )

# # Segunda linha de sliders
# col5, col6, col7, col8 = st.columns(4)

# with col5:
#     custo_packing = st.slider(
#         "R$/Cx Packing House",
#         min_value=1.0,
#         max_value=15.0,
#         value=4.60,
#         step=0.1
#     )

# with col6:
#     st.markdown("**Quantidade de Caixas**")
#     st.markdown("*(Calculado automaticamente)*")

# with col7:
#     desp_adm = st.slider(
#         "Desp. Adm (R$/Cx)",
#         min_value=0.0,
#         max_value=10.0,
#         value=2.32,
#         step=0.1
#     )

# with col8:
#     desp_financeira = st.slider(
#         "Desp. Financeira (R$/Cx)",
#         min_value=0.0,
#         max_value=10.0,
#         value=2.89,
#         step=0.1
#     )

# st.divider()

# # CÁLCULOS
# # Conversões
# peso_caixa_kg = 4.0

# # Produção total
# producao_total_ton = AREA_TOTAL_HA * produtividade
# producao_total_kg = producao_total_ton * 1000

# # Quantidade de caixas (automático)
# qtd_caixas = producao_total_kg / peso_caixa_kg

# # Preço por caixa em reais
# preco_caixa_reais = preco_venda_euro * cambio

# # Faturamento baseado no preço POR CAIXA
# faturamento_proporcional = qtd_caixas * preco_caixa_reais

# # Custos
# custo_campo_total = producao_total_kg * custo_campo
# custo_packing_total = qtd_caixas * custo_packing
# desp_adm_total = qtd_caixas * desp_adm
# desp_financeira_total = qtd_caixas * desp_financeira

# custos_despesas_total = custo_campo_total + custo_packing_total + desp_adm_total + desp_financeira_total

# # Lucro
# lucro_liquido = faturamento_proporcional - custos_despesas_total
# margem_liquida = (lucro_liquido / faturamento_proporcional * 100) if faturamento_proporcional > 0 else 0

# # Exibição dos resultados
# st.subheader("📊 Resultados da Simulação")

# # Criar layout visual
# col_resultado1, col_resultado2 = st.columns(2)

# with col_resultado1:
#     st.markdown("### 💰 Faturamento")
    
#     # Faturamento Próprio
#     st.markdown(f"""
#     <div style='background-color: #2d5016; padding: 20px; border-radius: 10px; margin-bottom: 10px;'>
#         <h4 style='color: white; margin: 0;'>Faturamento Prop.</h4>
#         <h2 style='color: white; margin: 10px 0;'>R$ {faturamento_proporcional:,.2f}</h2>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Caixas
#     st.metric("📦 Caixas Totais", f"{qtd_caixas:,.0f}")
#     st.metric("🌾 Produção Total", f"{producao_total_ton:,.2f} ton")

# with col_resultado2:
#     st.markdown("### 💵 Lucro Líquido")
    
#     # Lucro
#     cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
#     st.markdown(f"""
#     <div style='background-color: {cor_lucro}; padding: 20px; border-radius: 10px; margin-bottom: 10px;'>
#         <h4 style='color: white; margin: 0;'>Lucro Líquido</h4>
#         <h2 style='color: white; margin: 10px 0;'>R$ {lucro_liquido:,.2f}</h2>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Margem
#     st.markdown(f"""
#     <div style='background-color: #f0f0f0; padding: 15px; border-radius: 10px;'>
#         <h4 style='color: #333; margin: 0;'>Margem Líquida</h4>
#         <h3 style='color: {"green" if margem_liquida >= 0 else "red"}; margin: 10px 0;'>{margem_liquida:.2f}%</h3>
#     </div>
#     """, unsafe_allow_html=True)

# st.divider()

# # Detalhamento de custos
# st.subheader("📋 Detalhamento de Custos e Despesas")

# col_detalhe1, col_detalhe2, col_detalhe3, col_detalhe4 = st.columns(4)

# with col_detalhe1:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 15px; border-radius: 10px; text-align: center;'>
#         <h5 style='color: white; margin: 0;'>Custo Campo</h5>
#         <h4 style='color: white; margin: 10px 0;'>R$ {custo_campo_total:,.2f}</h4>
#     </div>
#     """, unsafe_allow_html=True)

# with col_detalhe2:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 15px; border-radius: 10px; text-align: center;'>
#         <h5 style='color: white; margin: 0;'>Custo PH</h5>
#         <h4 style='color: white; margin: 10px 0;'>R$ {custo_packing_total:,.2f}</h4>
#     </div>
#     """, unsafe_allow_html=True)

# with col_detalhe3:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 15px; border-radius: 10px; text-align: center;'>
#         <h5 style='color: white; margin: 0;'>Desp. Financeira</h5>
#         <h4 style='color: white; margin: 10px 0;'>R$ {desp_financeira_total:,.2f}</h4>
#     </div>
#     """, unsafe_allow_html=True)

# with col_detalhe4:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 15px; border-radius: 10px; text-align: center;'>
#         <h5 style='color: white; margin: 0;'>Adm. Sede</h5>
#         <h4 style='color: white; margin: 10px 0;'>R$ {desp_adm_total:,.2f}</h4>
#     </div>
#     """, unsafe_allow_html=True)

# # Total de custos
# st.markdown(f"""
# <div style='background-color: #d35400; padding: 20px; border-radius: 10px; margin-top: 20px; text-align: center;'>
#     <h4 style='color: white; margin: 0;'>Custos + Desp. Total</h4>
#     <h2 style='color: white; margin: 10px 0;'>R$ {custos_despesas_total:,.2f}</h2>
# </div>
# """, unsafe_allow_html=True)

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






# import streamlit as st

# # ===== CONFIGURAÇÕES =====
# st.set_page_config(page_title="Simulações - E se?", layout="wide")
# st.markdown(
#     """
#     <style>
#         div.block-container {padding-top: 0.5rem; padding-bottom: 0.5rem; padding-left: 1rem; padding-right: 1rem;}
#         .metric-container h4, .metric-container h2, .metric-container h3, h5 {margin: 0;}
#         h2, h3, h4, h5 {margin-top: 0.2rem; margin-bottom: 0.2rem;}
#         .small-box {padding: 10px !important;}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ===== TÍTULO =====
# st.title("🌾 Simulações - \"E se?\"")

# # ===== CONSTANTES =====
# AREA_TOTAL_HA = 964.46
# peso_caixa_kg = 4.0

# # ===== SLIDERS + INPUTS =====
# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     produtividade = st.slider("Produtividade Ton/ha", 10.0, 50.0, 32.0, 0.5)
#     produtividade = st.number_input("ou digite:", value=produtividade, step=0.5)

# with col2:
#     preco_venda_euro = st.slider("Preço Venda (€/Cx)", 1.0, 10.0, 3.5, 0.1)
#     preco_venda_euro = st.number_input("ou digite €:", value=preco_venda_euro, step=0.1)

# with col3:
#     cambio = st.slider("Câmbio (R$)", 3.0, 8.0, 5.15, 0.05)
#     cambio = st.number_input("ou digite R$:", value=cambio, step=0.05)

# with col4:
#     custo_campo = st.slider("R$/Kg Campo", 0.5, 5.0, 1.80, 0.1)
#     custo_campo = st.number_input("ou digite:", value=custo_campo, step=0.1)

# with col5:
#     custo_packing = st.slider("R$/Cx Packing", 1.0, 15.0, 4.60, 0.1)
#     custo_packing = st.number_input("ou digite:", value=custo_packing, step=0.1)

# col6, col7, col8, col9 = st.columns(4)

# with col6:
#     desp_adm = st.slider("Desp. Adm (R$/Cx)", 0.0, 10.0, 2.32, 0.1)
#     desp_adm = st.number_input("ou digite:", value=desp_adm, step=0.1)

# with col7:
#     desp_financeira = st.slider("Desp. Financeira (R$/Cx)", 0.0, 10.0, 2.89, 0.1)
#     desp_financeira = st.number_input("ou digite:", value=desp_financeira, step=0.1)

# with col8:
#     valor_folha = st.slider("Valor Médio da Folha (R$)", 1_000_000.0, 5_000_000.0, 2_500_000.0, 50_000.0)
#     valor_folha = st.number_input("ou digite R$ folha:", value=valor_folha, step=50_000.0)

# with col9:
#     st.markdown("**Caixas**")
#     st.markdown("*(calculado automaticamente)*")

# st.divider()

# # ===== CÁLCULOS =====
# producao_total_ton = AREA_TOTAL_HA * produtividade
# producao_total_kg = producao_total_ton * 1000
# qtd_caixas = producao_total_kg / peso_caixa_kg

# preco_caixa_reais = preco_venda_euro * cambio
# faturamento_proporcional = qtd_caixas * preco_caixa_reais

# custo_campo_total = producao_total_kg * custo_campo
# custo_packing_total = qtd_caixas * custo_packing
# desp_adm_total = qtd_caixas * desp_adm
# desp_financeira_total = qtd_caixas * desp_financeira

# custos_despesas_total = (
#     custo_campo_total + custo_packing_total + desp_adm_total + desp_financeira_total
# )

# lucro_liquido = faturamento_proporcional - custos_despesas_total
# margem_liquida = (lucro_liquido / faturamento_proporcional * 100) if faturamento_proporcional > 0 else 0
# participacao_resultados = (lucro_liquido * 0.10) / valor_folha if valor_folha > 0 else 0

# # ===== EXIBIÇÃO DOS RESULTADOS =====
# st.subheader("📊 Resultados da Simulação")

# col_r1, col_r2, col_r3 = st.columns(3)

# with col_r1:
#     st.markdown(f"""
#     <div style='background-color:#2d5016; padding:10px; border-radius:8px;'>
#         <h4 style='color:white;'>💰 Faturamento</h4>
#         <h3 style='color:white;'>R$ {faturamento_proporcional:,.2f}</h3>
#     </div>
#     """, unsafe_allow_html=True)
#     st.metric("📦 Caixas", f"{qtd_caixas:,.0f}")
#     st.metric("🌾 Produção", f"{producao_total_ton:,.2f} ton")

# with col_r2:
#     cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
#     st.markdown(f"""
#     <div style='background-color:{cor_lucro}; padding:10px; border-radius:8px;'>
#         <h4 style='color:white;'>💵 Lucro Líquido</h4>
#         <h3 style='color:white;'>R$ {lucro_liquido:,.2f}</h3>
#         <p style='color:white; margin:0;'>Margem: {margem_liquida:.2f}%</p>
#     </div>
#     """, unsafe_allow_html=True)

# with col_r3:
#     st.markdown(f"""
#     <div style='background-color:#3b3b3b; padding:10px; border-radius:8px;'>
#         <h4 style='color:white;'>👥 Participação Resultados</h4>
#         <h3 style='color:white;'>{participacao_resultados*100:.2f}%</h3>
#         <p style='color:#ccc; margin:0;'>10% Lucro / Folha</p>
#     </div>
#     """, unsafe_allow_html=True)

# st.divider()

# # ===== DETALHAMENTO DE CUSTOS =====
# st.subheader("📋 Detalhamento de Custos e Despesas")

# cols = st.columns(4)
# labels = ["Campo", "Packing", "Financeira", "Adm."]
# values = [custo_campo_total, custo_packing_total, desp_financeira_total, desp_adm_total]

# for i in range(4):
#     with cols[i]:
#         st.markdown(f"""
#         <div style='background-color:#ff8c00; padding:8px; border-radius:8px; text-align:center;'>
#             <h5 style='color:white;'>{labels[i]}</h5>
#             <h4 style='color:white;'>R$ {values[i]:,.2f}</h4>
#         </div>
#         """, unsafe_allow_html=True)

# st.markdown(f"""
# <div style='background-color:#d35400; padding:12px; border-radius:8px; text-align:center;'>
#     <h4 style='color:white;'>Custos + Desp. Total</h4>
#     <h3 style='color:white;'>R$ {custos_despesas_total:,.2f}</h3>
# </div>
# """, unsafe_allow_html=True)

# st.divider()

# # ===== INFO =====
# st.info(f"""
# **ℹ️ Informações da Simulação:**
# - Área Total: {AREA_TOTAL_HA} ha
# - Peso por Caixa: {peso_caixa_kg} kg
# - Preço Venda: €{preco_venda_euro:.2f}/cx = R$ {preco_caixa_reais:.2f}/cx
# - Caixas: {qtd_caixas:,.0f}
# - Kg Totais: {producao_total_kg:,.2f}
# """)












import streamlit as st

# Configuração da página
st.set_page_config(page_title="Simulações - E se?", layout="wide")

# CSS customizado para interface compacta
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

# Título
st.title("🌾 Simulações - \"E se?\"")

# Área total fixa
AREA_TOTAL_HA = 964.46

# Primeira linha de sliders
col1, col2, col3, col4  = st.columns(4)

with col1:
    produtividade = st.slider("Produtividade Ton/ha", 10.0, 50.0, 32.0, 0.5, key="s1")
    # produtividade = st.number_input("", value=produtividade, min_value=10.0, max_value=50.0, step=0.5, key="n1", label_visibility="collapsed")

with col2:
    preco_venda_euro = st.slider("Preço Venda (€/Cx)", 1.0, 10.0, 3.5, 0.1, key="s2")
    # preco_venda_euro = st.number_input("", value=preco_venda_euro, min_value=1.0, max_value=10.0, step=0.1, key="n2", label_visibility="collapsed")

with col3:
    cambio = st.slider("Câmbio (R$)", 3.0, 8.0, 5.15, 0.05, key="s3")
    # cambio = st.number_input("", value=cambio, min_value=3.0, max_value=8.0, step=0.05, key="n3", label_visibility="collapsed")

with col4:
    custo_campo = st.slider("R$/Kg Campo", 0.5, 5.0, 1.80, 0.1, key="s4")
    # custo_campo = st.number_input("", value=custo_campo, min_value=0.5, max_value=5.0, step=0.1, key="n4", label_visibility="collapsed")


# Segunda linha de sliders
col5, col6, col7, col8 = st.columns(4)


with col5:
    custo_packing = st.slider("R$/Cx Packing", 1.0, 15.0, 4.60, 0.1, key="s5")
    # custo_packing = st.number_input("", value=custo_packing, min_value=1.0, max_value=15.0, step=0.1, key="n5", label_visibility="collapsed")


with col6:
    desp_adm = st.slider("Desp. Adm (R$/Cx)", 0.0, 10.0, 2.32, 0.1, key="s6")
    # desp_adm = st.number_input("", value=desp_adm, min_value=0.0, max_value=10.0, step=0.1, key="n6", label_visibility="collapsed")

with col7:
    desp_financeira = st.slider("Desp. Financeira (R$/Cx)", 0.0, 10.0, 2.89, 0.1, key="s7")
    # desp_financeira = st.number_input("", value=desp_financeira, min_value=0.0, max_value=10.0, step=0.1, key="n7", label_visibility="collapsed")

with col8:
    valor_medio_folha = st.slider("Valor Médio Folha (R$)", 1000000.0, 5000000.0, 3000000.0, 50000.0, key="s8")
    # valor_medio_folha = st.number_input("", value=valor_medio_folha, min_value=1000000.0, max_value=5000000.0, step=50000.0, key="n8", label_visibility="collapsed")

st.divider()

# CÁLCULOS
peso_caixa_kg = 4.0
producao_total_ton = AREA_TOTAL_HA * produtividade
producao_total_kg = producao_total_ton * 1000
qtd_caixas = producao_total_kg / peso_caixa_kg
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

# Exibição dos resultados - Layout compacto
col_r1, col_r2, col_r3 = st.columns(3)

with col_r1:
    st.markdown(f"""
    <div style='background-color: #2d5016; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Prop.</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {faturamento_proporcional:,.0f}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.metric("📦 Caixas", f"{qtd_caixas:,.0f}", label_visibility="visible")

with col_r2:
    cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
    st.markdown(f"""
    <div style='background-color: {cor_lucro}; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Líquido</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {lucro_liquido:,.0f}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.metric("📊 Margem Líquida", f"{margem_liquida:.1f}%")

with col_r3:
    st.markdown(f"""
    <div style='background-color: #1e7ba3; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>👥 Participação 10%</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{participacao_resultados:.2f}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.metric("🌾 Produção", f"{producao_total_ton:,.0f} ton")

st.divider()

# Detalhamento de custos - mais compacto
col_d1, col_d2, col_d3, col_d4, col_d5 = st.columns(5)

with col_d1:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo Campo</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {custo_campo_total:,.0f}</h5>
    </div>
    """, unsafe_allow_html=True)

with col_d2:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo PH</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {custo_packing_total:,.0f}</h5>
    </div>
    """, unsafe_allow_html=True)

with col_d3:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Desp. Financeira</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {desp_financeira_total:,.0f}</h5>
    </div>
    """, unsafe_allow_html=True)

with col_d4:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Adm. Sede</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {desp_adm_total:,.0f}</h5>
    </div>
    """, unsafe_allow_html=True)

with col_d5:
    st.markdown(f"""
    <div style='background-color: #d35400; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Total Custos</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {custos_despesas_total:,.0f}</h5>
    </div>
    """, unsafe_allow_html=True)

# Informações adicionais
st.divider()
st.info(f"""
**ℹ️ Informações da Simulação:**
- Área Total: {AREA_TOTAL_HA} ha
- Peso por Caixa: {peso_caixa_kg} kg
- Preço de Venda: €{preco_venda_euro:.2f}/cx = R$ {preco_caixa_reais:.2f}/cx
- Caixas (automático): {qtd_caixas:,.0f}
- Kg Totais: {producao_total_kg:,.2f}
""")