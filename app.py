import streamlit as st

st.set_page_config(
    page_title="Refina | Assistente Ágil",
    page_icon="📝",
    layout="centered",
)

st.title("Refina")
st.subheader("Assistente de Refinamento e Estimativa com IA")

st.info(
    "Protótipo em construção: esta versão valida o formulário. "
    "A análise com IA ainda não está conectada."
)

st.write(
    "Descreva sua demanda e acrescente as informações disponíveis. "
    "Utilize apenas dados fictícios neste projeto demonstrativo."
)

with st.form("formulario_historia"):
    historia = st.text_area(
        "História de usuário ou demanda *",
        placeholder=(
            "Como cliente, quero solicitar o reembolso "
            "de uma compra pelo aplicativo."
        ),
        height=120,
    )

    contexto = st.text_area(
        "Contexto e objetivo de negócio",
        placeholder="Qual problema queremos resolver?",
    )

    regras = st.text_area(
        "Regras de negócio conhecidas",
        placeholder="Informe somente regras já confirmadas.",
    )

    sistemas = st.text_area(
        "Sistemas envolvidos",
        placeholder="Ex.: aplicativo, sistema de pedidos e pagamentos.",
    )

    referencias = st.text_area(
        "Referências de estimativa da squad",
        placeholder=(
            "Descreva histórias já estimadas, seus pontos "
            "e os fatores que influenciaram o esforço."
        ),
    )

    enviar = st.form_submit_button(
        "Validar preenchimento",
        type="primary",
    )

if enviar:
    if not historia.strip():
        st.error("Preencha a história de usuário ou demanda.")
    else:
        st.success("Dados recebidos! Confira o conteúdo abaixo.")

        campos = {
            "História ou demanda": historia,
            "Contexto": contexto,
            "Regras conhecidas": regras,
            "Sistemas envolvidos": sistemas,
            "Referências de estimativa": referencias,
        }

        for titulo, conteudo in campos.items():
            st.markdown(f"**{titulo}**")
            st.text(conteudo.strip() or "Não informado.")

        st.warning(
            "Nenhuma análise ou estimativa foi gerada nesta versão."
        )

st.divider()
st.caption(
    "Projeto demonstrativo de Alvin Leroy Steagall | "
    "Requisitos e estimativas devem ser validados pela squad."
)