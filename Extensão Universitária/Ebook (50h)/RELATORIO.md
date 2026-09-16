# Relatório de Atividade de Extensão Universitária

> **Campos a confirmar antes de submeter ao portal.** Tudo que descreve a obra foi
> medido no próprio código e no README do repositório. Os dados que dependem da
> realidade do aluno estão marcados com ⚠️: data do relatório, organização parceira,
> pessoas atendidas e local.
>
> **Atenção à regra de presencialidade.** As Orientações aos Alunos (p. 6) e as
> Perguntas Frequentes (item 8) exigem que a atividade seja realizada
> **presencialmente**.

## 1. Dados de Cadastro

| Item | Descrição |
|---|---|
| **Instituição** | Universidade Paulista — UNIP |
| **Curso** | Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) |
| **Campus** | Campus SJC Dutra — São José dos Campos (SP) |
| **Semestre / Ano** | 3º Semestre / 2026 |
| **Carga Horária** | **50 horas** |
| **Área Temática e Projeto** | TRABALHO, ECONOMIA E ADMINISTRAÇÃO · Programas e projetos desenvolvidos para a comunidade. |
| **Ação de Extensão** | **Ebook (50 horas)** |
| **Pessoas Impactadas** | ⚠️ *(informar o número de pessoas atendidas presencialmente)* |
| **Organização Parceira** | ⚠️ *(escola, biblioteca, curso técnico, coletivo ou comunidade atendida)* |
| **Público Beneficiário** | Estudantes e comunidade externa interessados em Inteligência Artificial |
| **Repositório Público** | <https://github.com/MayconDIS/E-book-Super_IA_World> |

### Alunos Participantes

| Nº | R.A. | Nome do Aluno | Curso |
|---|---|---|---|
| 1 | **H719CD3** | Maycon Douglas Inácio Silva | Análise e Desenvolvimento de Sistemas |

*Turma: DS3A48*

*Atividade realizada individualmente, abrangendo pesquisa, redação, design e desenvolvimento da obra.*

---

## 2. Descrição da Atividade

### 2.1 Descrição Geral da Atividade

A presente atividade de extensão universitária consistiu na pesquisa, redação, design
e desenvolvimento do e-book **"Super IA World: Curiosidades da IA"**, obra digital
gratuita de **10 folhas em formato A4**, com cerca de **1.600 palavras**, que apresenta
curiosidades sobre Inteligência Artificial usando a estética retrô de 16 bits inspirada
em *Super Mario World*.

A obra aproxima o público não especialista de conceitos técnicos da área — dados de
treinamento, alinhamento de modelos, arquitetura Transformer, tokens, janelas de
contexto e interpretabilidade — usando a linguagem visual de um jogo clássico como ponto
de entrada. Cada capítulo é apresentado como uma fase, com blocos de destaque em forma
de curiosidade, dica e *power-up*, e encerra com a fonte utilizada. O conteúdo foi
atualizado para maio de 2026.

#### Estrutura do conteúdo

| Capítulo | Conceitos tratados |
|---|---|
| Mundo 1-1 — O Apetite por Dados | Volume de dados de treinamento, leis de escala, dados curados, dados sintéticos e colapso de modelo |
| Mundo 1-2 — O Fator Humano | RLHF, IA Constitucional, DPO, cadeia de raciocínio (*Chain of Thought*) e *Red Teaming* |
| Mundo 1-3 — O Motor Transformer | Mecanismo de atenção, *self-attention*, sistemas agênticos, modelos abertos e *Mixture of Experts* |
| Mundo 1-4 — Tokens e Contexto | Tokens e espaço vetorial, teste *needle in a haystack*, janelas de contexto, RAG e *context caching* |
| Fase do Chefão — A Caixa Preta | Habilidades emergentes, interpretabilidade mecanística, *Sparse Autoencoders* e alucinações |
| Bônus — A Fusão: IA + Impacto Humano | Hiper-personalização, design centrado na dor e agência |
| Mundo Especial — Referências | Nove artigos e marcos da área, com link |

#### Desenvolvimento técnico

A peça foi construída como aplicação web estática, sem framework e sem bibliotecas de
terceiros:

- **HTML5 semântico** — 311 linhas, estruturadas com `main`, `article`, `nav`, `aside` e
  `footer`, com rótulos de acessibilidade nas folhas e título da capa acessível a
  leitores de tela.
- **CSS modular em arquitetura SMACSS** — 728 linhas em 9 arquivos: sete módulos
  separados por responsabilidade (variáveis, base, layout, componentes, temas, animações
  e impressão), o arquivo central de importação e o do cenário de fundo.
- **JavaScript sem bibliotecas** — 73 linhas organizadas em funções de responsabilidade
  única, incluindo o botão de exportação para PDF.
- **Ilustração** — 28 imagens PNG (personagens, blocos e elementos de cenário da estética
  16 bits), com tratamento de imagem e composição realizados no Canva.
- **Temas por capítulo** — cada fase recebe uma paleta de cor própria, aplicada por
  classes de tema.

#### Impressão

A obra reproduz o formato A4 exato por meio de regras de impressão (`@media print`),
preservando as imagens e as cores de fundo na exportação para PDF, o que permite
distribuir a versão impressa com a mesma diagramação da digital.

---

### 2.2 Descrição da Participação de Cada Aluno

#### Maycon Douglas Inácio Silva (R.A. H719CD3)

Atuou em **todas as etapas da obra: pesquisa, redação, design e desenvolvimento**,
aplicando conhecimentos das disciplinas de *Programação Web*, *Engenharia de Software* e
*Interface Homem-Computador*. Foi responsável por pesquisar e selecionar os conteúdos e as
nove referências sobre Inteligência Artificial, redigir os capítulos em linguagem
acessível, compor a identidade visual de 16 bits com tratamento das imagens no Canva,
estruturar o CSS em arquitetura modular e codificar o suporte a impressão em A4.

---

## 3. Conclusão e Resultados Alcançados

A atividade entregou à comunidade uma obra introdutória e gratuita sobre Inteligência
Artificial, que usa a linguagem visual de um jogo clássico para tornar acessíveis
conceitos técnicos da área, disponível em formato digital e em versão para impressão em
A4.

A atividade atendeu diretamente ⚠️ *(informar o número de pessoas atendidas
presencialmente e onde)*.

Resultados objetivos e verificáveis:

- **7 capítulos em 10 folhas A4**, com capa, índice e folha final.
- **Nove referências** com link direto para os artigos e marcos citados.
- **Versão para impressão A4** fiel à versão digital.
- **Código-fonte aberto** em repositório público, com histórico de versões.

A atividade atendeu aos seguintes **Objetivos de Desenvolvimento Sustentável (ODS) da
ONU**:

- **ODS 4 (Educação de Qualidade):** material didático gratuito sobre Inteligência
  Artificial em linguagem acessível.
- **ODS 9 (Indústria, Inovação e Infraestrutura):** divulgação de conceitos centrais da
  inovação tecnológica recente.
- **ODS 10 (Redução das Desigualdades):** acesso gratuito e código aberto, reutilizável
  por terceiros.

### 3.1 Local Onde a Atividade Foi Realizada

A obra foi desenvolvida pelo aluno e disponibilizada em repositório público. ⚠️ *(Informar
o local e a data da apresentação ou distribuição presencial, exigida pelas Orientações da
UNIP.)*

### 3.2 Considerações Finais

- **Dificuldades enfrentadas.** A principal foi garantir que a exportação para PDF fosse
  fiel à versão digital — dimensões A4 rigorosas, imagens de fundo preservadas na
  impressão e tipografia ajustada à folha —, o que exigiu sucessivas correções registradas
  no histórico do projeto.
- **Sugestões.** Como a área de Inteligência Artificial evolui rapidamente, recomenda-se
  revisar periodicamente os capítulos que citam modelos e técnicas recentes.
- **Observações.** O conteúdo da obra reflete o estado da área em maio de 2026, data da
  última atualização.

---

## 4. Comprovação

- **Obra reproduzida na íntegra:** Anexo A de `relatorio.html` (folhas 12 a 21).
- **Figura 1:** capa e Mapa do Mundo (índice) do e-book.
- **Figura 2:** visão geral das 10 folhas.
- **Código-fonte com histórico de versões:** <https://github.com/MayconDIS/E-book-Super_IA_World>
- ⚠️ **Registro da ação presencial:** *(anexar lista de presença e registro fotográfico)*
- ⚠️ **Carta de Apresentação institucional:** *(anexar, se a atividade foi realizada junto
  a organização parceira)*

---

## 5. Texto para Preenchimento no Portal da UNIP (Campo "Relatório síntese" — Máx. 800 caracteres)

> Ebook (50h) produzido por aluno de ADS da UNIP SJC Dutra: "Super IA World — Curiosidades da IA". Obra digital gratuita de 10 folhas A4 e 7 capítulos que apresenta conceitos de Inteligência Artificial — dados de treinamento, alinhamento, arquitetura Transformer, tokens e interpretabilidade — com estética retrô de 16 bits inspirada em Super Mario World. Nove referências com link. Desenvolvida em HTML5 semântico, CSS modular SMACSS e JavaScript sem bibliotecas, com ilustrações tratadas no Canva e versão para impressão A4. Código aberto em repositório público. ODS 4, 9 e 10.
