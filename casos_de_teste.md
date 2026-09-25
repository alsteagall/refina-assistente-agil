# Testes do Refina

## Caso 1 — Demanda sem contexto
Entrada: solicitar reembolso de uma compra pelo aplicativo.
Esperado: levantar dúvidas, sinalizar hipóteses e não atribuir pontos.
Resultado: atendimento parcial.
Limitação: sugeriu elementos de interface como requisitos confirmados.

## Caso 2 — Escopo explícito
Entrada: registrar número da compra e motivo, retornar protocolo,
com análise manual. Sistemas: aplicativo e atendimento interno.
Sem lista de compras e sem integração com ERP ou gateway.
Aprovação e execução do estorno fora do escopo.

Esperado: preservar essas restrições e não atribuir pontos.
Resultado: atendimento parcial.
Acertos: história coerente e ausência de pontos sem referências.
Falhas:
- Classificou o estorno como manual sem essa informação.
- Tratou comunicação não detalhada como integração inexistente.
- Afirmou impossibilidade de validação automática sem base suficiente.

Status: protótipo funcional; qualidade das respostas em validação.

## Caso 3 — Distinções explícitas
Entrada: mesmas informações do caso 2, esclarecendo que somente
a análise é manual. Execução do estorno fora do escopo e forma
de comunicação entre sistemas ainda não definida.

Resultado: atendimento parcial.
Acertos:
- Não classificou o estorno ou a comunicação como manuais.
- Preservou o benefício do protocolo para acompanhamento.
- Não atribuiu pontos sem referências.

Limitações:
- Omitiu o aplicativo na história revisada.
- Presumiu digitação manual do número da compra.

Conclusão: explicitar as incertezas melhorou esta resposta,
mas não eliminou a necessidade de revisão humana.

## Caso 4 — Estimativa com referências

Entrada: mesma demanda, com referências fictícias de 3, 5 e 8 pontos.

Resultado: comparação por cenários apresentada, com ressalvas.
- Sugeriu 3 pontos com API existente e 5 com novo endpoint.
- Não converteu pontos em horas.
- Indicou necessidade de validação humana.
- Favoreceu 5 pontos antes de confirmar a premissa.
- Afirmou bloqueio total do desenvolvimento sem base suficiente.

Ocorrência técnica:
A primeira tentativa retornou erro 503.
Uma nova tentativa manual retornou a análise.

Melhoria pendente:
Apresentar mensagem mais clara para indisponibilidade temporária.