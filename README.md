# 🎮 Super IA World — E-book 16-bits

> Um e-book interativo sobre **Inteligência Artificial** com visual inspirado no **Super Mario World** dos anos 90.

![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Versão](https://img.shields.io/badge/versão-3.0_Refactored-blue)
![Arquitetura](https://img.shields.io/badge/arquitetura-SMACSS%20%7C%20Clean%20Code-orange)
![Licença](https://img.shields.io/badge/licença-MIT-yellow)

## 📖 Sobre

Este e-book gratuito apresenta curiosidades fascinantes sobre IA usando uma estética retrô de 16 bits. Todo o conteúdo é atualizado para **maio de 2026**, cobrindo os modelos mais recentes como GPT-5.5, Claude Opus 4.7 e Gemini 3.1 Pro. A versão 3.0 trouxe uma refatoração massiva de arquitetura de software, focada em performance, acessibilidade e renderização de impressão.

## 🗺️ Capítulos

| # | Capítulo | Tema |
|---|---------|------|
| 01 | Mundo 1-1: O Apetite por Dados | Como IAs devoram trilhões de palavras |
| 02 | Mundo 1-2: O Fator Humano | RLHF e IA Constitucional |
| 03 | Mundo 1-3: O Motor Transformer | A arquitetura que mudou tudo |
| 04 | Mundo 1-4: Tokens e Contexto | A corrida das janelas de contexto |
| 05 | Fase do Chefão: A Caixa Preta | Comportamentos emergentes |
| Bônus | A Fusão: IA + Impacto Humano | Hiper-personalização e agência digital |
| 06 | Mundo Especial: Referências | Papers e marcos históricos |

## 🚀 Como Usar

### Ler no navegador
Basta acessar pelo seu navegador web, ou hospedar via GitHub Pages. Para abrir o projeto localmente:
```bash
start ebook.html
```

### Exportar como PDF (Pixel-Perfect)
O e-book foi projetado com regras rigorosas de `@media print` para garantir fidelidade visual no papel:
1. Abra `ebook.html` no Google Chrome ou Edge.
2. Pressione `Ctrl + P` ou clique no botão flutuante **"BAIXAR PDF"**.
3. Selecione **"Salvar como PDF"**.
4. ✅ Ative a opção **"Gráficos de fundo"** (Background graphics).
5. Defina as Margens como **"Nenhuma"** (None).
6. O layout será renderizado perfeitamente no formato A4, preservando espaçamentos e pixel art.

## 🛠️ Tecnologias & Engenharia de Software

Na versão mais recente, o projeto foi reestruturado seguindo princípios profissionais de Engenharia:

- **Princípios SOLID & Clean Code:** Refatoração orientada ao Princípio da Responsabilidade Única (*Single Responsibility*), garantindo que cada arquivo CSS e cada função JavaScript cuide estritamente de apenas um aspecto da aplicação.
- **Arquitetura SMACSS:** CSS modularizado e escalável (`variables`, `base`, `layout`, `components`, `themes`, `animations`, `print`).
- **Semântica HTML5:** Uso rigoroso de `<main>`, `<article>`, `<nav>`, `<aside>` e `<footer>` para estruturação hierárquica imaculada.
- **Acessibilidade e SEO:** Utilização de `aria-labels`, Open Graph / Twitter Cards para previews em redes sociais, e classes `.sr-only` para manter o visual limpo enquanto leitores de tela leem os `<h1/>` corretos.
- **Isolamento de Estado:** Elementos decorativos do cenário desvinculados do layout do e-book, evitando CSS inline e code smells.
- **Design Visual (Canva):** Tratamento de imagem, ajustes e o toque final das figuras e composições da estética 16-bits foram realizados cirurgicamente utilizando o **Canva**.

## 📁 Estrutura do Projeto

```
📦 E-book-Super_IA_World
├── 📄 ebook.html          # Conteúdo semântico do e-book (HTML5)
├── 📂 assets/
│   ├── 📂 css/
│   │   ├── 🎨 style.css   # Hub central de importação CSS
│   │   ├── 🎨 cenario.css # Animações e posicionamento de elementos de fundo
│   │   └── 📂 modules/    # Arquitetura SMACSS (Arquivos modulares)
│   ├── 📂 js/
│   │   └── ⚙️ script.js   # Lógica (Scroll tracking, Event listeners)
│   ├── 📂 img/            # Imagens chave de layout
│   ├── 📂 figures/        # Sprites 16-bits para o cenário (nuvens, inimigos)
│   └── 📂 pdf/            # Páginas de uma versão anterior em PDF
├── 📂 Extensão Universitária/
│   └── 📂 Ebook (50h)/    # Relatório de extensão universitária
│       ├── 📄 relatorio.html
│       ├── 📘 RELATORIO.md
│       ├── ⚙️ gerar_relatorio.py
│       └── 📂 assets/     # Logo e figuras do relatório
├── 📂 .agent/             # Skills de agentes de IA usadas no desenvolvimento
├── 📂 .planning/          # Planejamento e pesquisa das fases do projeto
├── 🤖 CLAUDE.md           # Guia de arquitetura para o Claude Code
└── 📘 README.md           # Este arquivo
```

## 🎓 Relatório de Extensão Universitária

Este e-book foi produzido como atividade de extensão universitária (**Ebook — 50 horas**) do curso de Análise e Desenvolvimento de Sistemas da UNIP. O relatório fica em [`Extensão Universitária/Ebook (50h)/`](Extens%C3%A3o%20Universit%C3%A1ria/Ebook%20%2850h%29/):

- **`relatorio.html`** — relatório no formato ABNT (A4), com o e-book reproduzido na íntegra no Anexo A.
- **`RELATORIO.md`** — a mesma estrutura em texto, com o resumo para o portal da UNIP.
- **`gerar_relatorio.py`** — monta o `relatorio.html` a partir do `ebook.html` e dos módulos CSS.

Para gerar o PDF do relatório, abra `relatorio.html` **de dentro do repositório** — as imagens do anexo vêm da pasta `assets/` da raiz —, pressione `Ctrl + P` e ative **"Gráficos de fundo"**.

Se o e-book mudar, gere o relatório de novo em vez de editar o anexo à mão. O script usa como base o modelo de relatório da pasta de extensão do projeto CasalFlow:

```bash
cd "Extensão Universitária/Ebook (50h)"
python gerar_relatorio.py
```

## ✨ Features

- 🎨 **Paleta Temática** adaptativa que muda a cor das bordas retrô conforme o avanço dos capítulos.
- 🖨️ **Impressão A4 Milimétrica** garantindo espaçamentos perfeitos para a pontuação final e conteúdos dinâmicos.
- 🎮 **Parallax Backgrounds** com animações suaves de cenário infinito e nuvens deslizando.
- 🔗 **Open Graph Otimizado** para gerar miniatura com imagem ao compartilhar no WhatsApp/LinkedIn.
- 📱 **Mobile-Friendly** sem perder o charme dos 16-bits.

## 👤 Autor

**Maycon Douglas** — Entusiasta de Tecnologia

## 📄 Licença

Este projeto é de uso livre para fins educacionais.

---

*"O conhecimento liberta"* 🌟
