import json
from pathlib import Path

from google import genai
from google.genai import types


def analisar_historia(
    historia,
    contexto,
    regras,
    sistemas,
    referencias,
    chave_api,
):
    if not historia.strip():
        raise ValueError("Informe uma história ou demanda.")

    dados = {
        "historia": historia.strip(),
        "contexto": contexto.strip(),
        "regras": regras.strip(),
        "sistemas": sistemas.strip(),
        "referencias": referencias.strip(),
    }

    if sum(len(valor) for valor in dados.values()) > 15000:
        raise ValueError("Reduza o conteúdo para até 15 mil caracteres.")

    arquivo = Path(__file__).with_name("instrucoes.md")
    instrucoes = arquivo.read_text(encoding="utf-8")

    pedido = (
        "Analise os dados abaixo seguindo as instruções. "
        "Campos vazios representam informações não fornecidas.\n\n"
        + json.dumps(dados, ensure_ascii=False)
    )

    with genai.Client(
        api_key=chave_api,
        http_options=types.HttpOptions(timeout=60000),
    ) as cliente:
        resposta = cliente.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=pedido,
            config=types.GenerateContentConfig(
                system_instruction=instrucoes,
                max_output_tokens=4096,
            ),
        )

    if not resposta.text:
        raise RuntimeError(
            "A IA não retornou uma análise. Revise a demanda e tente novamente."
        )

    return resposta.text