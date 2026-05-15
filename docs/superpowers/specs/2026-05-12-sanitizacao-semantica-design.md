# Design: Sanitizacao Semantica do E-book

## Objetivo

Refatorar o projeto Super IA World E-book eliminando CSS inline, introduzindo CSS custom properties, reorganizando o stylesheet, melhorando performance e corrigindo o JS — sem build tools, mantendo HTML/CSS/JS puro e um unico `index.html`.

## Problemas Identificados

1. **CSS inline abundante** — `style=""` espalhado por todo o HTML (capa, blocos, listas, referencias, final)
2. **Cores hardcoded nos temas** — cada tema repete cores em multiplos seletores, dificil trocar paleta
3. **style.css desorganizado** — sem secoes claras, mistura reset com componentes com temas
4. **Imagens sem otimizacao** — sem lazy loading, sem decodificacao assincrona, sem preconnect
5. **JS quebrado** — `script.js` referencia `#toc-list` que nao existe no HTML

## Mudancas

### 1. Eliminacao de CSS Inline

Mapeamento de `style=""` para classes CSS (algumas ja existem mas nao estao sendo usadas no HTML):

| Trecho no HTML | Classe CSS |
|---|---|
| Capa: `position:absolute; top:29%; left:50%; ...` | `.cover-text-container` |
| Capa subtitulo: `color:#fff; text-shadow:...; font-size:20px; ...` | `.cover-subtitle` |
| Capa autor badge: `background:rgba(0,0,0,0.8); padding:8px 20px; ...` | `.cover-author-badge` |
| Capa autor principal: `font-size:18px` | `.cover-author-badge.cover-author-main` |
| Capa footer: `position:absolute; bottom:3%; ...` | `.cover-footer-container` |
| Capa autor footer: `font-size:16px` | `.cover-author-badge.cover-author-footer` |
| Bloco verde: `background-color:#2ecc71; border-color:#000` | `.theme-green-block` |
| Bloco azul: `background-color:#3498db; color:#fff` | `.theme-blue-block` |
| Bloco laranja: `background-color:#f39c12` | `.theme-orange-block` |
| Bloco roxo: `background-color:#9b59b6; color:#fff` | `.theme-purple-block` |
| Bloco vermelho: `background-color:#c0392b` | `.theme-red-block` |
| Bloco bonus q: `background-color:#273c75; color:#fff; border-color:#fbc531` | `.bonus-q-block` |
| Texto de bloco: `margin-bottom:0; font-size:14pt` | `.block-content-text` |
| Lista bonus: `font-family:'VT323'; font-size:16pt; ...` | `.bonus-list` |
| Sub-lista bonus: `font-size:14pt; margin-top:10px; ...` | `.bonus-sublist` |
| Highlight verde: `color:#2ecc71` | `.bonus-highlight-green` |
| Highlight azul: `color:#3498db` | `.bonus-highlight-blue` |
| Highlight amarelo: `color:#f1c40f` | `.bonus-highlight-yellow` |
| Highlight vermelho: `color:#e74c3c` | `.bonus-highlight-red` |
| Caixa de referencias: `background:#fff; color:#000; border:4px solid #000; padding:1.5cm` | `.ref-box` |
| Lista de referencias: `margin-top:0.5cm; font-family:'VT323'; font-size:13pt; text-align:center` | `.ref-list` |
| Link titulo ref: `font-size:13pt` | `.ref-link-title` |
| Link desc ref: `font-size:10pt` | `.ref-link-desc` |
| Final box: `justify-content:center; align-items:center; text-align:center; flex-grow:1` | `.end-box` |
| Final imagem: `width:200px; image-rendering:pixelated; margin-bottom:20px` | `.end-img` |
| Final titulo: `color:#000; font-size:24pt` | `.end-title` |
| Final footer: `margin-top:0.5cm; font-family:'Press Start 2P'; font-size:8pt; color:#555` | `.end-footer-text` |
| Lista boss: `font-family:'VT323'; font-size:18pt; margin-bottom:0.8cm; padding-left:1.5cm; color:#eee` | `.boss-list` |

Resultado: `index.html` com zero atributos `style=""`.

### 2. CSS Custom Properties

Substituir cores hardcoded por variaveis no `:root`:

```css
:root {
  --color-data-bg: #cffcfc;
  --color-data-accent: #00cccc;
  --color-data-heading: #007a7a;
  --color-human-bg: #ffe5d9;
  --color-human-accent: #ff8c69;
  --color-human-heading: #a35a42;
  --color-engine-bg: #d0f0f0;
  --color-engine-accent: #4db6ac;
  --color-engine-heading: #006a6a;
  --color-tokens-bg: #f3e5f5;
  --color-tokens-accent: #b39ddc;
  --color-tokens-heading: #6a0dad;
  --color-impact-bg: #d5f5e3;
  --color-impact-accent: #52be80;
  --color-impact-heading: #1e8449;
  --color-victory-bg: #fff9e6;
  --color-victory-accent: #fccb28;
  --color-victory-heading: #b8860b;
  --color-boss-bg: #2a2a2a;
  --color-boss-accent: #fccb28;
  --color-boss-heading: #ff3838;
  --color-retro-bg: #fccb28;
  --color-highlight-default: #00cc00;
  --color-accent-red: #ff3838;
}
```

Temas refatorados para usar variaveis:

```css
.theme-data { background-color: var(--color-data-bg); }
.theme-data .retro-box { background-color: var(--color-data-bg); }
.theme-data .retro-box h2 { color: var(--color-data-heading); border-bottom-color: var(--color-data-accent); }
.theme-data h2 + p::first-letter { color: var(--color-data-accent); }
.theme-data .highlight { background-color: var(--color-data-accent); color: #000; }
```

### 3. Reorganizacao do style.css

Secoes com comentarios de cabecalho:

```
/* ============================================
   1. RESET & BASE
   ============================================ */

/* ============================================
   2. LAYOUT
   ============================================ */

/* ============================================
   3. TIPOGRAFIA
   ============================================ */

/* ============================================
   4. COMPONENTES
   ============================================ */

/* ============================================
   5. PAGINAS ESPECIAIS (cover, index, boss, end)
   ============================================ */

/* ============================================
   6. TEMAS POR CAPITULO (custom properties)
   ============================================ */

/* ============================================
   7. UTILIDADES (highlights, decos, lists)
   ============================================ */

/* ============================================
   8. ANIMACOES
   ============================================ */

/* ============================================
   9. PRINT / PDF
   ============================================ */
```

### 4. Performance

- `loading="lazy"` em todas as `<img>` de decoracao (bg-cloud, bg-deco, figuras internas)
- `decoding="async"` nas imagens de conteudo
- `<link rel="preconnect" href="https://fonts.googleapis.com">` e `href="https://fonts.gstatic.com"` no `<head>`
- Imagens de conteudo maiores convertidas para WebP/AVIF com fallback `<picture>`

### 5. Sanitizacao do JS

- Remover referencia a `#toc-list` (nao existe no HTML)
- O script atualmente tenta gerar sidebar dinamica mas o HTML ja tem sidebar estatica no pipe-container
- Simplificar para: observar scroll e destacar capitulo ativo no sidebar (se aplicavel), ou remover completamente

## Escopo Nao Incluido

- Build tools ou bundlers
- Separacao em multiplos HTMLs
- Mudancas visuais ou de design
- Adicao de novos capitulos ou conteudo
- Framework CSS externo

## Criterios de Sucesso

1. Zero `style=""` no `index.html`
2. Todos os temas usando CSS custom properties
3. `style.css` organizado em 9 secoes claras
4. Todas as imagens de decoracao com `loading="lazy"`
5. Preconnect do Google Fonts no `<head>`
6. `script.js` sem referencias a elementos inexistentes
7. Visual identico antes e depois da refatoracao
