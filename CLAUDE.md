# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é

E-book estático de página única com curiosidades sobre Inteligência Artificial, na estética 16 bits de *Super Mario World*. HTML + CSS + um arquivo JS, sem build, sem dependências, sem framework.

O e-book mora em `ebook.html`. Não há `index.html`.

O GitHub Pages **não está ativo** neste repositório. As meta tags Open Graph e Twitter de `ebook.html` apontam para `https://maycondis.github.io/Super_IA_World-Ebook/`, um nome antigo do repositório, que hoje responde 404. Mantido assim por decisão do autor.

Idioma do conteúdo, dos comentários no código e das mensagens de commit: **português do Brasil**.

## Rodar

Não há build, lint nem suíte de testes. Abrir `ebook.html` direto no navegador funciona (as fontes vêm do Google Fonts); para medir no navegador com consistência, servir a pasta:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Exportar PDF: botão "BAIXAR PDF" ou `Ctrl+P`, com "Gráficos de fundo" ligado e margens "Nenhuma".

## Arquitetura

### Contrato de folha

Cada página é um `<article class="page theme-X">` de 21cm × 29.7cm, com `overflow: hidden` e um `.retro-box` dentro. A capa é `.page.cover`, com `capa.png` de fundo; as demais levam o tijolo `bloco-tijolo.png` como fundo da folha. A folha do chefão usa `.boss-box` e as referências usam `.ref-box`.

### CSS

`assets/css/style.css` importa, nesta ordem: `variables → base → layout → components → themes → animations → print`. Regras de mesma especificidade em arquivo posterior vencem. `assets/css/cenario.css` é carregado à parte e estiliza só o cenário de fundo fixo (`.world-bg`, nuvens, blocos e personagens decorativos).

- `variables.css` — paleta por capítulo (`--color-<tema>-bg/-accent/-heading`).
- `themes.css` — uma classe por capítulo (`.theme-data`, `.theme-human`, `.theme-engine`, `.theme-tokens`, `.theme-impact`, `.theme-victory`, `.theme-vanilla`) e as variantes de cor dos blocos (`.theme-green-block` etc.).
- `print.css` — reproduz a A4 exata e força `print-color-adjust: exact`, senão o navegador descarta tijolos e cores no PDF. Componente colorido novo precisa entrar nessa lista.

Duas `url()` do CSS usam caminho relativo ao módulo: `../../figures/bloco-tijolo.png` (layout) e `../../img/capa.png` (components).

### JavaScript

`assets/js/script.js`: botão de exportar PDF (`#btn-pdf` → `window.print()`) e rastreamento de seção para um menu lateral (`#sidebar`).

**O menu lateral não existe no HTML.** O CSS dele (`#pipe-container`, `#sidebar` em `layout.css`) e o rastreamento no JS estão presentes, mas não fazem nada hoje.

### Imagens

28 PNGs (cerca de 15,8 MB) em `assets/figures/` (sprites) e `assets/img/` (capa, ilustrações e ícone), referenciados por caminho relativo no HTML e no CSS. `assets/pdf/old/` guarda as páginas de uma versão anterior em PDF.

### Outras pastas

`.agent/` (skills de agente de IA) e `.planning/` (planejamento e pesquisa das fases do projeto) são artefatos de ferramenta, não fazem parte do e-book publicado.

## Relatório de extensão

`Extensão Universitária/Ebook (50h)/` segue o padrão das pastas de extensão universitária do repositório CasalFlow: `relatorio.html` (ABNT, A4), `RELATORIO.md` e `assets/` com logo e figuras. O Anexo A do relatório é uma **cópia** do `ebook.html` e dos módulos CSS, montada por `gerar_relatorio.py`, na mesma pasta, que acha o `ebook.html` subindo as pastas. Ao mudar o e-book, rodar o script de novo em vez de editar o anexo à mão. O CSS de base do relatório vem da pasta da Cartilha no CasalFlow, por caminho absoluto no topo do script.

Três particularidades deste e-book que o script trata:

- As `url()` do CSS e os `src="assets/..."` das folhas são reescritos para caminhos relativos à pasta do relatório. Por isso o `relatorio.html` precisa ser aberto de dentro do repositório: as imagens do anexo vêm de `../../assets/`.
- O e-book chama as próprias folhas de `.page`, a mesma classe das folhas do relatório. É o `@scope (.anexo-a)` que impede a regra `.page` do e-book de alcançar o relatório; não tirar as regras do e-book de dentro do escopo.
- `@keyframes` e `@page` não valem dentro de `@scope` e são movidos para fora ou removidos.

Depois de mexer no texto do relatório, conferir no navegador que nenhuma `body > section.page` passa de 29,7cm: a folha cresce em vez de cortar, e na impressão isso vira uma página extra que desloca a numeração do sumário.

`Extensão Universitária/MODELO/` é para os documentos oficiais da UNIP, referência local fora do git (`.gitignore`).

## Autoria

O e-book credita "Maycon Douglas". No relatório de extensão aparece com nome completo e R.A.: Maycon Douglas Inácio Silva (R.A. H719CD3).
