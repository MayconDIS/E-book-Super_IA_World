# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é

E-book estático de página única com curiosidades sobre Inteligência Artificial, na estética 16 bits de *Super Mario World*. HTML + CSS + um arquivo JS, sem build, sem dependências, sem framework. Serve como portfólio e material educacional para entusiastas de IA, estudantes e quem se interessa por estética retrô.

O e-book mora em `ebook.html`. Não há `index.html`.

O conteúdo reflete o cenário de IA de **maio de 2026** (modelos, técnicas e datas citados nos capítulos). Atualizar o e-book significa revisar esses trechos datados, não só o visual.

O GitHub Pages **nunca foi ativado** — o deploy era uma fase do roadmap original que não chegou a ser feita. Por isso as meta tags Open Graph e Twitter de `ebook.html`, que apontam para `https://maycondis.github.io/Super_IA_World-Ebook/` (um nome antigo do repositório), respondem 404. Mantido assim por decisão do autor.

Idioma do conteúdo, dos comentários no código e das mensagens de commit: **português do Brasil**.

## Rodar

Não há build, lint nem suíte de testes. Abrir `ebook.html` direto no navegador funciona (as fontes vêm do Google Fonts); para medir no navegador com consistência, servir a pasta:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Exportar PDF: botão "BAIXAR PDF" ou `Ctrl+P`, com "Gráficos de fundo" ligado e margens "Nenhuma". PDFs gerados ficam fora do git (`*.pdf` no `.gitignore`).

## Decisões de projeto

Tomadas durante o desenvolvimento e ainda válidas no código:

- **PDF pelo `window.print()` nativo.** O plano inicial previa a biblioteca `html2pdf.js` (captura em canvas); foi descartada por ser uma dependência pesada. Não reintroduzir.
- **Folha A4 estrita na tela e na impressão.** Cada folha tem exatamente 21cm × 29,7cm, com fontes escalonadas para a tela e o PDF saírem idênticos. Toda mudança de fonte ou de bloco de capítulo precisa caber em 29,7cm: o que passa disso é cortado (`overflow: hidden`) ou gera página em branco no PDF.
- **O cenário decorativo sai na impressão de propósito.** `.world-bg`, `.ground-real` e os sprites não são escondidos no `@media print`; por isso o leitor precisa ligar "Gráficos de fundo". Só `#pipe-container` e `#btn-pdf` somem no papel.
- **Cores dos temas só por custom properties** em `variables.css`. Uma refatoração de maio de 2026 ("sanitização semântica") acabou com cores repetidas seletor a seletor; tema novo segue o mesmo padrão.
- **Sem CSS inline, com duas exceções deliberadas:** os ícones flutuantes dos blocos `.q-block`/`.powerup-block` e o texto dourado da capa, cujo `style` anula a animação herdada de uma classe utilitária. Não espalhar novos `style=""`.
- **Imagens decorativas com `loading="lazy"` e `decoding="async"`**, e `preconnect` para as fontes no `<head>`.

## Arquitetura

### Contrato de folha

Cada página é um `<article class="page theme-X">` de 21cm × 29,7cm, com `page-break-after: always`, `overflow: hidden` e um `.retro-box` dentro. A capa é `.page.cover`, com `capa.png` de fundo; as demais levam o tijolo `bloco-tijolo.png` como fundo da folha. A folha do chefão usa `.boss-box` e as referências usam `.ref-box`.

### CSS

`assets/css/style.css` importa, nesta ordem: `variables → base → layout → components → themes → animations → print`. Regras de mesma especificidade em arquivo posterior vencem. `assets/css/cenario.css` é carregado à parte e estiliza só o cenário de fundo fixo (`.world-bg`, nuvens, blocos e personagens decorativos).

- `variables.css` — paleta por capítulo (`--color-<tema>-bg/-accent/-heading`).
- `themes.css` — uma classe por capítulo (`.theme-data`, `.theme-human`, `.theme-engine`, `.theme-tokens`, `.theme-impact`, `.theme-victory`, `.theme-vanilla`) e as variantes de cor dos blocos (`.theme-green-block` etc.).
- `print.css` — reproduz a A4 exata e força `print-color-adjust: exact`, senão o navegador descarta tijolos e cores no PDF. Componente colorido novo precisa entrar nessa lista.

Duas `url()` do CSS usam caminho relativo ao módulo: `../../figures/bloco-tijolo.png` (layout) e `../../img/capa.png` (components).

### JavaScript

`assets/js/script.js`: botão de exportar PDF (`#btn-pdf` → `window.print()`) e rastreamento de seção para um menu lateral (`#sidebar`).

**O menu lateral não existe mais no HTML.** Ele já existiu — um "cano" verde fixo com o Mapa do Mundo, que ia para o topo em telas estreitas —, mas foi retirado. O CSS (`#pipe-container`, `.pipe-collar`, `#sidebar` em `layout.css`) e o rastreamento no JS continuam lá, sem efeito. Se o menu voltar, as duas partes estão prontas.

A ordem em `initializeApplication` importa: o botão de PDF é configurado **antes** do rastreamento, que retorna cedo quando não acha o menu. Com a ordem invertida o botão parava de funcionar — já foi bug.

### Imagens

28 PNGs (cerca de 15,8 MB) em `assets/figures/` (sprites) e `assets/img/` (capa, ilustrações e ícone), referenciados por caminho relativo no HTML e no CSS. `assets/pdf/old/` guarda as páginas de uma versão anterior em PDF.

## Verificação antes de entregar

Critérios de aceite do projeto que continuam aplicáveis:

1. O PDF gerado mantém as cores e os fundos originais.
2. Cada capítulo ocupa exatamente uma folha A4 — nenhuma cortada, nenhuma em branco.
3. A folha do chefão (fundo escuro) continua legível.
4. `author` e `description` das meta tags estão corretos.

## Relatório de extensão

`Extensão Universitária/Ebook (50h)/` segue o padrão das pastas de extensão universitária do repositório CasalFlow: `relatorio.html` (ABNT, A4), `RELATORIO.md` e `assets/` com logo e figuras. O Anexo A do relatório é uma **cópia** do `ebook.html` e dos módulos CSS, montada por `gerar_relatorio.py`, na mesma pasta, que acha o `ebook.html` subindo as pastas. Ao mudar o e-book, rodar o script de novo em vez de editar o anexo à mão. O CSS de base do relatório vem da pasta da Cartilha no CasalFlow, por caminho absoluto no topo do script.

Três particularidades deste e-book que o script trata:

- As `url()` do CSS e os `src="assets/..."` das folhas são reescritos para caminhos relativos à pasta do relatório. Por isso o `relatorio.html` precisa ser aberto de dentro do repositório: as imagens do anexo vêm de `../../assets/`.
- O e-book chama as próprias folhas de `.page`, a mesma classe das folhas do relatório. É o `@scope (.anexo-a)` que impede a regra `.page` do e-book de alcançar o relatório; não tirar as regras do e-book de dentro do escopo.
- `@keyframes` e `@page` não valem dentro de `@scope` e são movidos para fora ou removidos.

Depois de mexer no texto do relatório, conferir no navegador que nenhuma `body > section.page` passa de 29,7cm: a folha cresce em vez de cortar, e na impressão isso vira uma página extra que desloca a numeração do sumário.

`Extensão Universitária/MODELO/` é para os documentos oficiais da UNIP, referência local fora do git (`.gitignore`).

## Pendências do roadmap original

- Deploy no GitHub Pages — nunca feito (ver "O que é").
- Tutorial de divulgação no LinkedIn — produzido como PDF fora do git (`LinkedIn_Tutorial.pdf` no `.gitignore`), aguardando validação.
- Ideias de expansão não iniciadas: coleta de feedback de leitores, um "Mundo 2" com novos capítulos e otimização avançada para celular.

## Origem do conteúdo e das ferramentas

- **O capítulo Bônus ("A Fusão: IA + Impacto Humano") vem da base de conhecimento da skill Powerbook**, um mentor de estratégia de infoprodutos: o tripé "Oferta Clara + Criativo de Impacto + Página Simples" e os exemplos de TDAH infantil e terceira idade saíram dela. Ao revisar esse capítulo, é esse o referencial.
- O projeto foi conduzido com a metodologia GSD (*Get Shit Done*), as skills dos plugins [superpowers](https://github.com/obra/superpowers) e [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) e o modo de comunicação comprimido Caveman. As cópias dessas skills, que ficavam em `.agent/`, e os documentos de planejamento, que ficavam em `.planning/`, foram removidos do repositório depois de incorporados aqui; o histórico do git ainda os tem.

## Autoria

O e-book credita "Maycon Douglas". No relatório de extensão aparece com nome completo e R.A.: Maycon Douglas Inácio Silva (R.A. H719CD3).
