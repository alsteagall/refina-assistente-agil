# Refina — Assistente de Refinamento e Estimativa com IA

Projeto demonstrativo de aplicação de inteligência artificial ao trabalho de Product Owners, analistas de negócios e squads de desenvolvimento.

**Status:** em desenvolvimento. Este repositório contém a documentação inicial; a aplicação ainda não está disponível.

## Problema

Demandas podem chegar ao refinamento com objetivos pouco claros, regras incompletas e dependências não identificadas. Essas lacunas dificultam a discussão e a estimativa de esforço pela equipe.

## Objetivo

Apoiar a preparação de histórias de usuário para refinamento, identificando dúvidas, sugerindo critérios de aceite e oferecendo apoio à estimativa com base em referências da própria squad.

## Funcionalidades previstas para a primeira versão

- Receber uma demanda e seu contexto de negócio.
- Identificar informações ausentes e gerar perguntas de refinamento.
- Sugerir uma versão mais clara da história de usuário.
- Propor critérios de aceite verificáveis.
- Apontar possíveis dependências e riscos.
- Sugerir esforço preliminar quando houver histórias de referência.
- Permitir copiar ou baixar a análise.

## Informações de entrada

- História de usuário ou descrição da demanda.
- Contexto e objetivo de negócio.
- Regras conhecidas.
- Sistemas envolvidos.
- Histórias de referência com estimativas da squad, quando disponíveis.

## Princípios da análise

- Separar fatos informados, hipóteses e sugestões.
- Não inventar regras de negócio.
- Sinalizar informações que precisam de confirmação.
- Não atribuir story points sem referências da equipe.
- Não converter automaticamente story points em horas.
- Manter a validação de requisitos e estimativas sob responsabilidade do time.

## Exemplo de uso planejado

**Demanda:** “Como cliente, quero solicitar o reembolso de uma compra pelo aplicativo.”

O assistente deverá identificar perguntas sobre prazo, reembolso parcial, formas de pagamento e integrações, sem assumir respostas que não foram fornecidas.

## Tecnologias planejadas

- Python para a lógica da aplicação.
- Streamlit para a interface.
- API de modelo de linguagem para a análise com IA.
- GitHub para versionamento e documentação.
- Streamlit Community Cloud para hospedagem.

## Plano de desenvolvimento

- [x] Criar o repositório.
- [x] Documentar a proposta inicial.
- [ ] Construir a interface.
- [ ] Validar o fluxo com exemplo simulado e identificado.
- [ ] Integrar o serviço de IA.
- [ ] Testar a qualidade das análises e o tratamento de falhas.
- [ ] Publicar a aplicação.
- [ ] Preparar a demonstração do case.

## Avaliação planejada

Os testes verificarão se o assistente identifica lacunas relevantes, respeita as regras fornecidas e justifica suas sugestões. Também serão avaliados casos de demanda vaga, ausência de referências de estimativa e indisponibilidade do serviço de IA.

## Limitações

A IA pode produzir respostas incorretas ou incompletas. Suas análises precisam de revisão humana e não substituem o refinamento colaborativo nem a estimativa da squad.

O projeto utilizará dados fictícios para demonstração.

## Autor

Alvin Leroy Steagall  
Product Owner | Scrum Master | Squad Lead

Projeto de portfólio voltado à aplicação de IA em atividades de gestão de produtos e trabalho ágil.

## Experimente o Refina

Aplicação: https://refina-alvin.streamlit.app/

## Sobre este case

Projeto demonstrativo de Alvin Leroy Steagall, desenvolvido com
Python, Streamlit e integração com a API do Google Gemini.

A aplicação apoia o refinamento de histórias de usuário, propondo
perguntas, critérios de aceite, dependências, riscos e estimativas
provisórias quando há referências da squad.

## Validação e limitações

Foram realizados testes com dados fictícios, com e sem referências
de estimativa. Os resultados estão registrados em casos_de_teste.md.

A IA pode presumir requisitos não informados. Todas as sugestões
devem ser revisadas pela equipe. O serviço está sujeito às cotas
e à disponibilidade do provedor de IA.
