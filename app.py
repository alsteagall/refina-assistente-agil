import streamlit as st
from google.genai import errors

from analise import analisar_historia


st.set_page_config(
    page_title="Refina | Assistente Ágil",
    page_icon="📝",
    layout="centered",
)

st.title("Refina")
st.subheader("Assistente de Refinamento e Estimativa com IA")

st.info(
    "Projeto demonstrativo. Use apenas dados fictícios. "
    "O conteúdo será enviado ao Gemini para análise."
)

st.write(
    "Prepare sua história para discussão com a squad. "
    "As sugestões da IA precisam de validação da equipe."
)

with st.form("formulario_historia"):
    historia = st.text_area(
        "História de usuário ou demanda *",
        placeholder=(
            "Como cliente, quero solicitar o reembolso "
            "de uma compra pelo aplicativo."
        ),
        height=120,
        max_chars=5000,
    )

    contexto = st.text_area(
        "Contexto e objetivo de negócio",
        placeholder="Qual problema queremos resolver?",
        max_chars=2500,
    )

    regras = st.text_area(
        "Regras de negócio conhecidas",
        placeholder="Informe somente regras já confirmadas.",
        max_chars=2500,
    )

    sistemas = st.text_area(
        "Sistemas envolvidos",
        placeholder="Ex.: aplicativo, pedidos e pagamentos.",
        max_chars=2500,
    )

    referencias = st.text_area(
        "Referências de estimativa da squad",
        placeholder=(
            "Descreva histórias já estimadas, seus pontos "
            "e os fatores que influenciaram o esforço."
        ),
        max_chars=2500,
    )

    enviar = st.form_submit_button(
        "Analisar história",
        type="primary",
    )

if enviar:
    st.session_state.pop("resultado", None)

    if not historia.strip():
        st.error("Preencha a história de usuário ou demanda.")
    else:
        try:
            chave = st.secrets["GEMINI_API_KEY"]
        except Exception:
            st.error(
                "Não foi possível ler a chave. Confira a configuração "
                "de GEMINI_API_KEY em .streamlit/secrets.toml."
            )
            st.stop()

        if not chave or chave == "COLE_SUA_CHAVE_AQUI":
            st.error("Configure uma chave válida antes de analisar.")
            st.stop()

        try:
            with st.spinner("Analisando a história..."):
                resultado = analisar_historia(
                    historia=historia,
                    contexto=contexto,
                    regras=regras,
                    sistemas=sistemas,
                    referencias=referencias,
                    chave_api=chave,
                )

            st.session_state["resultado"] = resultado

        except errors.APIError as erro:
            codigo = getattr(erro, "code", None)

            if codigo == 429:
                st.error(
                    "O Gemini informou um limite de uso ou de cota. "
                    "Confira os limites no Google AI Studio."
                )
            elif codigo in (401, 403):
                st.error(
                    "O Gemini recusou o acesso. "
                    "Confira a chave e as permissões do projeto."
                )
            elif codigo == 404:
                st.error(
                    "O modelo configurado não foi encontrado "
                    "ou não está disponível para este projeto."
                )
            else:
                st.error(
                    f"O Gemini não concluiu a análise. Código: {codigo}."
                )

        except FileNotFoundError:
            st.error("O arquivo instrucoes.md não foi encontrado.")

        except Exception:
            st.error(
                "Não foi possível concluir a análise. "
                "Confira os arquivos e a conexão e tente novamente."
            )

if "resultado" in st.session_state:
    st.divider()
    st.subheader("Análise sugerida")
    st.markdown(st.session_state["resultado"])

    st.warning(
        "Valide as regras, os critérios de aceite e a estimativa "
        "com a squad antes de utilizá-los."
    )

    st.download_button(
        "Baixar análise",
        data=st.session_state["resultado"],
        file_name="analise_refina.md",
        mime="text/markdown",
    )

    with st.expander("Copiar análise"):
        st.code(st.session_state["resultado"], language=None)

st.divider()
st.caption("Projeto demonstrativo de Alvin Leroy Steagall")