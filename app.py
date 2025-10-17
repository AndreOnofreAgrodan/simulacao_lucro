import streamlit as st

# Configuração da página
st.set_page_config(page_title="Simulações - E se?", layout="wide")

# Título
st.title("🌾 Simulações - \"E se?\"")

# Área total fixa
AREA_TOTAL_HA = 964.46

# Criar colunas para os sliders
col1, col2, col3, col4 = st.columns(4)

with col1:
    produtividade = st.slider(
        "Produtividade Ton/ha",
        min_value=10.0,
        max_value=50.0,
        value=32.0,
        step=0.5
    )

with col2:
    preco_venda_euro = st.slider(
        "Preço de Venda (€/Cx)",
        min_value=1.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

with col3:
    cambio = st.slider(
        "Câmbio (R$)",
        min_value=3.0,
        max_value=8.0,
        value=5.15,
        step=0.05
    )

with col4:
    custo_campo = st.slider(
        "R$/Kg Campo",
        min_value=0.5,
        max_value=5.0,
        value=1.80,
        step=0.1
    )

# Segunda linha de sliders
col5, col6, col7, col8 = st.columns(4)

with col5:
    custo_packing = st.slider(
        "R$/Cx Packing House",
        min_value=1.0,
        max_value=15.0,
        value=4.60,
        step=0.1
    )

with col6:
    st.markdown("**Quantidade de Caixas**")
    st.markdown("*(Calculado automaticamente)*")

with col7:
    desp_adm = st.slider(
        "Desp. Adm (R$/Cx)",
        min_value=0.0,
        max_value=10.0,
        value=2.32,
        step=0.1
    )

with col8:
    desp_financeira = st.slider(
        "Desp. Financeira (R$/Cx)",
        min_value=0.0,
        max_value=10.0,
        value=2.89,
        step=0.1
    )

st.divider()

# CÁLCULOS
# Conversões
peso_caixa_kg = 4.0

# Produção total
producao_total_ton = AREA_TOTAL_HA * produtividade
producao_total_kg = producao_total_ton * 1000

# Quantidade de caixas (automático)
qtd_caixas = producao_total_kg / peso_caixa_kg

# Preço por caixa em reais
preco_caixa_reais = preco_venda_euro * cambio

# Faturamento baseado no preço POR CAIXA
faturamento_proporcional = qtd_caixas * preco_caixa_reais

# Custos
custo_campo_total = producao_total_kg * custo_campo
custo_packing_total = qtd_caixas * custo_packing
desp_adm_total = qtd_caixas * desp_adm
desp_financeira_total = qtd_caixas * desp_financeira

custos_despesas_total = custo_campo_total + custo_packing_total + desp_adm_total + desp_financeira_total

# Lucro
lucro_liquido = faturamento_proporcional - custos_despesas_total
margem_liquida = (lucro_liquido / faturamento_proporcional * 100) if faturamento_proporcional > 0 else 0

# Exibição dos resultados
st.subheader("📊 Resultados da Simulação")

# Criar layout visual
col_resultado1, col_resultado2 = st.columns(2)

with col_resultado1:
    st.markdown("### 💰 Faturamento")
    
    # Faturamento Próprio
    st.markdown(f"""
    <div style='background-color: #2d5016; padding: 20px; border-radius: 10px; margin-bottom: 10px;'>
        <h4 style='color: white; margin: 0;'>Faturamento Prop.</h4>
        <h2 style='color: white; margin: 10px 0;'>R$ {faturamento_proporcional:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Caixas
    st.metric("📦 Caixas Totais", f"{qtd_caixas:,.0f}")
    st.metric("🌾 Produção Total", f"{producao_total_ton:,.2f} ton")

with col_resultado2:
    st.markdown("### 💵 Lucro Líquido")
    
    # Lucro
    cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
    st.markdown(f"""
    <div style='background-color: {cor_lucro}; padding: 20px; border-radius: 10px; margin-bottom: 10px;'>
        <h4 style='color: white; margin: 0;'>Lucro Líquido</h4>
        <h2 style='color: white; margin: 10px 0;'>R$ {lucro_liquido:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Margem
    st.markdown(f"""
    <div style='background-color: #f0f0f0; padding: 15px; border-radius: 10px;'>
        <h4 style='color: #333; margin: 0;'>Margem Líquida</h4>
        <h3 style='color: {"green" if margem_liquida >= 0 else "red"}; margin: 10px 0;'>{margem_liquida:.2f}%</h3>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Detalhamento de custos
st.subheader("📋 Detalhamento de Custos e Despesas")

col_detalhe1, col_detalhe2, col_detalhe3, col_detalhe4 = st.columns(4)

with col_detalhe1:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 15px; border-radius: 10px; text-align: center;'>
        <h5 style='color: white; margin: 0;'>Custo Campo</h5>
        <h4 style='color: white; margin: 10px 0;'>R$ {custo_campo_total:,.2f}</h4>
    </div>
    """, unsafe_allow_html=True)

with col_detalhe2:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 15px; border-radius: 10px; text-align: center;'>
        <h5 style='color: white; margin: 0;'>Custo PH</h5>
        <h4 style='color: white; margin: 10px 0;'>R$ {custo_packing_total:,.2f}</h4>
    </div>
    """, unsafe_allow_html=True)

with col_detalhe3:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 15px; border-radius: 10px; text-align: center;'>
        <h5 style='color: white; margin: 0;'>Desp. Financeira</h5>
        <h4 style='color: white; margin: 10px 0;'>R$ {desp_financeira_total:,.2f}</h4>
    </div>
    """, unsafe_allow_html=True)

with col_detalhe4:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 15px; border-radius: 10px; text-align: center;'>
        <h5 style='color: white; margin: 0;'>Adm. Sede</h5>
        <h4 style='color: white; margin: 10px 0;'>R$ {desp_adm_total:,.2f}</h4>
    </div>
    """, unsafe_allow_html=True)

# Total de custos
st.markdown(f"""
<div style='background-color: #d35400; padding: 20px; border-radius: 10px; margin-top: 20px; text-align: center;'>
    <h4 style='color: white; margin: 0;'>Custos + Desp. Total</h4>
    <h2 style='color: white; margin: 10px 0;'>R$ {custos_despesas_total:,.2f}</h2>
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




# import streamlit as st

# # Configuração da página
# st.set_page_config(page_title="Simulações - E se?", layout="wide")

# # CSS customizado para reduzir espaçamentos
# st.markdown("""
# <style>
#     .block-container {
#         padding-top: 1rem;
#         padding-bottom: 0rem;
#         padding-left: 2rem;
#         padding-right: 2rem;
#     }
#     h1 {
#         margin-bottom: 0.5rem;
#         font-size: 2rem;
#     }
#     .stSlider {
#         padding-top: 0rem;
#         padding-bottom: 0rem;
#     }
#     div[data-testid="stMetricValue"] {
#         font-size: 1.2rem;
#     }
#     div[data-testid="stMetricLabel"] {
#         font-size: 0.9rem;
#     }
#     hr {
#         margin-top: 0.5rem;
#         margin-bottom: 0.5rem;
#     }
#     .stNumberInput {
#         margin-top: -10px;
#     }
#     .stNumberInput > div > div > input {
#         padding: 0.25rem;
#         font-size: 0.85rem;
#     }
# </style>
# """, unsafe_allow_html=True)

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
#         step=0.5,
#         key="slider_prod"
#     )
#     produtividade = st.number_input("", value=produtividade, step=0.5, format="%.2f", key="input_prod", label_visibility="collapsed")

# with col2:
#     preco_venda_euro = st.slider(
#         "Preço de Venda (€/Cx)",
#         min_value=1.0,
#         max_value=10.0,
#         value=3.5,
#         step=0.1,
#         key="slider_preco"
#     )
#     preco_venda_euro = st.number_input("", value=preco_venda_euro, step=0.1, format="%.2f", key="input_preco", label_visibility="collapsed")

# with col3:
#     cambio = st.slider(
#         "Câmbio (R$)",
#         min_value=3.0,
#         max_value=8.0,
#         value=5.15,
#         step=0.05,
#         key="slider_cambio"
#     )
#     cambio = st.number_input("", value=cambio, step=0.05, format="%.2f", key="input_cambio", label_visibility="collapsed")

# with col4:
#     custo_campo = st.slider(
#         "R$/Kg Campo",
#         min_value=0.5,
#         max_value=5.0,
#         value=1.80,
#         step=0.1,
#         key="slider_campo"
#     )
#     custo_campo = st.number_input("", value=custo_campo, step=0.1, format="%.2f", key="input_campo", label_visibility="collapsed")

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
# st.subheader("📊 Resultados")

# # Criar layout visual
# col_resultado1, col_resultado2 = st.columns(2)

# with col_resultado1:
#     st.markdown("#### 💰 Faturamento")
    
#     # Faturamento Próprio
#     st.markdown(f"""
#     <div style='background-color: #2d5016; padding: 15px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.95rem;'>Faturamento Prop.</h5>
#         <h3 style='color: white; margin: 8px 0; font-size: 1.5rem;'>R$ {faturamento_proporcional:,.2f}</h3>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Caixas
#     col_m1, col_m2 = st.columns(2)
#     with col_m1:
#         st.metric("📦 Caixas", f"{qtd_caixas:,.0f}")
#     with col_m2:
#         st.metric("🌾 Produção", f"{producao_total_ton:,.0f} ton")

# with col_resultado2:
#     st.markdown("#### 💵 Lucro Líquido")
    
#     # Lucro
#     cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
#     st.markdown(f"""
#     <div style='background-color: {cor_lucro}; padding: 15px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.95rem;'>Lucro Líquido</h5>
#         <h3 style='color: white; margin: 8px 0; font-size: 1.5rem;'>R$ {lucro_liquido:,.2f}</h3>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Margem
#     st.markdown(f"""
#     <div style='background-color: #f0f0f0; padding: 12px; border-radius: 8px;'>
#         <h5 style='color: #333; margin: 0; font-size: 0.95rem;'>Margem Líquida</h5>
#         <h4 style='color: {"green" if margem_liquida >= 0 else "red"}; margin: 8px 0; font-size: 1.3rem;'>{margem_liquida:.2f}%</h4>
#     </div>
#     """, unsafe_allow_html=True)

# st.divider()

# # Detalhamento de custos
# st.subheader("📋 Custos e Despesas")

# col_detalhe1, col_detalhe2, col_detalhe3, col_detalhe4 = st.columns(4)

# with col_detalhe1:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 12px; border-radius: 8px; text-align: center;'>
#         <h6 style='color: white; margin: 0; font-size: 0.85rem;'>Custo Campo</h6>
#         <h5 style='color: white; margin: 8px 0; font-size: 1.1rem;'>R$ {custo_campo_total:,.2f}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_detalhe2:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 12px; border-radius: 8px; text-align: center;'>
#         <h6 style='color: white; margin: 0; font-size: 0.85rem;'>Custo PH</h6>
#         <h5 style='color: white; margin: 8px 0; font-size: 1.1rem;'>R$ {custo_packing_total:,.2f}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_detalhe3:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 12px; border-radius: 8px; text-align: center;'>
#         <h6 style='color: white; margin: 0; font-size: 0.85rem;'>Desp. Financeira</h6>
#         <h5 style='color: white; margin: 8px 0; font-size: 1.1rem;'>R$ {desp_financeira_total:,.2f}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_detalhe4:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 12px; border-radius: 8px; text-align: center;'>
#         <h6 style='color: white; margin: 0; font-size: 0.85rem;'>Adm. Sede</h6>
#         <h5 style='color: white; margin: 8px 0; font-size: 1.1rem;'>R$ {desp_adm_total:,.2f}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# # Total de custos
# st.markdown(f"""
# <div style='background-color: #d35400; padding: 15px; border-radius: 8px; margin-top: 10px; text-align: center;'>
#     <h5 style='color: white; margin: 0; font-size: 0.95rem;'>Custos + Desp. Total</h5>
#     <h3 style='color: white; margin: 8px 0; font-size: 1.5rem;'>R$ {custos_despesas_total:,.2f}</h3>
# </div>
# """, unsafe_allow_html=True)

# # Informações adicionais
# st.divider()
# with st.expander("ℹ️ Informações da Simulação", expanded=False):
#     st.markdown(f"""
#     - **Área Total:** {AREA_TOTAL_HA} ha
#     - **Peso por Caixa:** {peso_caixa_kg} kg
#     - **Preço de Venda:** €{preco_venda_euro:.2f}/cx = R$ {preco_caixa_reais:.2f}/cx
#     - **Caixas (automático):** {qtd_caixas:,.0f}
#     - **Kg Totais:** {producao_total_kg:,.2f}
#     """)