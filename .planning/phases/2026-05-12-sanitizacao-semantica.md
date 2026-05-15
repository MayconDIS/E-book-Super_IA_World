# Sanitizacao Semantica do E-book — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eliminar CSS inline, introduzir CSS custom properties, reorganizar stylesheet, melhorar performance e corrigir JS — mantendo visual identico.

**Architecture:** HTML monolitico limpo com zero `style=""`, CSS organizado em 9 secoes com variaveis, imagens com lazy loading, JS funcional.

**Tech Stack:** HTML5, CSS3 (custom properties), JavaScript vanilla — sem build tools.

---

### Task 1: Adicionar CSS Custom Properties no style.css

**Files:**
- Modify: `assets/css/style.css:1-4`

- [ ] **Step 1: Adicionar bloco `:root` com variaveis no topo do style.css, antes do reset**

Substituir as linhas 1-4 (`@import` + `* { margin: 0... }`) por:

```css
/* ============================================
   1. RESET & BASE
   ============================================ */

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

@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
@import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; scroll-behavior: smooth; }
```

- [ ] **Step 2: Verificar que o visual nao mudou**

Abrir `index.html` no navegador. As custom properties ainda nao estao sendo usadas, entao o visual permanece identico.

- [ ] **Step 3: Commit**

```bash
git add assets/css/style.css
git commit -m "feat: add CSS custom properties for theme colors"
```

---

### Task 2: Refatorar temas para usar custom properties

**Files:**
- Modify: `assets/css/style.css:229-288`

- [ ] **Step 1: Substituir os blocos de tema hardcoded por versoes com variaveis**

Substituir tudo de `/* === Temas Semânticos por Capítulo === */` ate o fim do `.boss-box .highlight` por:

```css
/* ============================================
   6. TEMAS POR CAPITULO (custom properties)
   ============================================ */

.theme-data { background-color: var(--color-data-bg); }
.theme-data .retro-box { background-color: var(--color-data-bg); }
.theme-data .retro-box h2 { color: var(--color-data-heading); border-bottom-color: var(--color-data-accent); }
.theme-data h2 + p::first-letter { color: var(--color-data-accent); }
.theme-data .highlight { background-color: var(--color-data-accent); color: #000; }

.theme-human { background-color: var(--color-human-bg); }
.theme-human .retro-box { background-color: var(--color-human-bg); }
.theme-human .retro-box h2 { color: var(--color-human-heading); border-bottom-color: var(--color-human-accent); }
.theme-human h2 + p::first-letter { color: var(--color-human-accent); }
.theme-human .highlight { background-color: var(--color-human-accent); color: #fff; }

.theme-engine { background-color: var(--color-engine-bg); }
.theme-engine .retro-box { background-color: var(--color-engine-bg); }
.theme-engine .retro-box h2 { color: var(--color-engine-heading); border-bottom-color: var(--color-engine-accent); }
.theme-engine h2 + p::first-letter { color: var(--color-engine-accent); }
.theme-engine .highlight { background-color: var(--color-engine-accent); color: #fff; }

.theme-tokens { background-color: var(--color-tokens-bg); }
.theme-tokens .retro-box { background-color: var(--color-tokens-bg); }
.theme-tokens .retro-box h2 { color: var(--color-tokens-heading); border-bottom-color: var(--color-tokens-accent); }
.theme-tokens h2 + p::first-letter { color: var(--color-tokens-accent); }
.theme-tokens .highlight { background-color: var(--color-tokens-accent); color: #fff; }

.theme-impact { background-color: var(--color-impact-bg); }
.theme-impact .retro-box { background-color: var(--color-impact-bg); }
.theme-impact .retro-box h2 { color: var(--color-impact-heading); border-bottom-color: var(--color-impact-accent); }
.theme-impact h2 + p::first-letter { color: var(--color-impact-accent); }
.theme-impact .highlight { background-color: var(--color-impact-accent); color: #fff; }

.theme-archive { background-color: #e5d3b3; }
.theme-archive .retro-box { background-color: #fdf5e6; }
.theme-archive .retro-box h2 { color: #8b4513; border-bottom-color: #deb887; }
.theme-archive h2 + p::first-letter { color: #deb887; }

.theme-victory { background-color: var(--color-victory-bg); }
.theme-victory .retro-box { background-color: var(--color-victory-bg); }
.theme-victory .retro-box h2 { color: var(--color-victory-heading); border-bottom-color: var(--color-victory-accent); }
.theme-victory h2 + p::first-letter { color: var(--color-victory-accent); }

.theme-vanilla { background-color: #fcfcfc; }
.theme-vanilla .retro-box { background-color: #fcfcfc; }
.theme-vanilla .retro-box h2 { color: #000; border-bottom-color: #000; }

.boss-box { background-color: var(--color-boss-bg); color: #fff; border-color: var(--color-boss-heading); }
.boss-box h2 { color: var(--color-boss-heading); border-bottom-color: var(--color-boss-heading); }
.boss-box p { color: #eee; }
.boss-box h2 + p::first-letter { color: var(--color-boss-accent); text-shadow: 3px 3px 0px #000; }
.boss-box .highlight { background-color: var(--color-boss-accent); color: #000; }
```

- [ ] **Step 2: Verificar que as cores dos temas permanecem identicas**

Abrir no navegador e comparar cada capitulo.

- [ ] **Step 3: Commit**

```bash
git add assets/css/style.css
git commit -m "refactor: themes use CSS custom properties"
```

---

### Task 3: Reorganizar style.css em secoes numeradas

**Files:**
- Modify: `assets/css/style.css` (reorganizar todo o arquivo)

- [ ] **Step 1: Reescrever style.css completo com secoes organizadas**

O arquivo inteiro sera reescrito na seguinte ordem:

```
1. RESET & BASE         — :root, imports, *, body
2. LAYOUT               — #pipe-container, .pipe-collar, #sidebar, main, .page
3. TIPOGRAFIA           — h1, h2, p, .highlight, first-letter
4. COMPONENTES          — .retro-box, .powerup-block, .q-block, .fonte-box, .footer-page, .deco-img, .fig-*
5. PAGINAS ESPECIAIS    — .page.cover, .cover-*, .book-index, .boss-box, .boss-list, .end-*, .ref-*
6. TEMAS POR CAPITULO   — custom properties themes
7. UTILIDADES           — .theme-*-block, .bonus-*, .block-content-text
8. ANIMACOES            — @keyframes
9. PRINT / PDF          — @media print
```

Reescrever `assets/css/style.css` completo:

```css
/* ============================================
   1. RESET & BASE
   ============================================ */

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

@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
@import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; scroll-behavior: smooth; }

body {
  font-family: 'VT323', monospace;
  display: flex;
  justify-content: center;
  position: relative;
  margin: 0;
  overflow-x: hidden;
  color: #333;
}

/* ============================================
   2. LAYOUT
   ============================================ */

#pipe-container {
  width: 260px;
  position: fixed;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 20;
}

.pipe-collar {
  width: calc(100% + 24px);
  height: 40px;
  margin-left: -12px;
  background-color: #00a800;
  background-image: linear-gradient(to right, #00a800 10%, #5ce430 30%, #00a800 60%, #005800 90%);
  border: 6px solid #000;
  border-bottom: 0;
  z-index: 21;
  position: relative;
}

#sidebar {
  width: 100%;
  background-color: #00a800;
  background-image: linear-gradient(to right, #00a800 10%, #5ce430 30%, #00a800 60%, #005800 90%);
  border: 6px solid #000;
  box-shadow: 8px 8px 0px rgba(0,0,0,0.5);
  font-family: 'Press Start 2P', cursive;
  max-height: 70vh;
  overflow-y: auto;
}

#sidebar::-webkit-scrollbar { width: 12px; }
#sidebar::-webkit-scrollbar-track { background: #008000; border-left: 2px solid #000; }
#sidebar::-webkit-scrollbar-thumb { background: #5c94fc; border: 2px solid #000; }

.sidebar-content { padding: 15px; }
#sidebar h3 { font-size: 10pt; margin-bottom: 20px; color: #fff; text-shadow: 2px 2px 0 #000; text-align: center; line-height: 1.4; border-bottom: 4px dashed #000; padding-bottom: 10px; }
#sidebar ul { list-style: none; }
#sidebar li { margin-bottom: 15px; }
#sidebar a { color: #f8d820; text-shadow: 1px 1px 0 #000; text-decoration: none; font-size: 8pt; line-height: 1.5; transition: color 0.2s, padding-left 0.2s; display: block; }
#sidebar a:hover { color: #fff; padding-left: 5px; }

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
  padding: 40px 0;
  width: 100%;
  position: relative;
  z-index: 10;
}

.page {
  background-image: url('../figures/bloco-tijolo.png');
  background-repeat: repeat;
  background-size: 80px;
  width: 100%;
  max-width: 21cm;
  min-height: 29.7cm;
  padding: 1cm;
  box-shadow: 15px 15px 0px rgba(0, 0, 0, 0.4);
  position: relative;
  display: flex;
  flex-direction: column;
  page-break-after: always;
  margin-bottom: 40px;
}

/* ============================================
   3. TIPOGRAFIA
   ============================================ */

h1, h2 { font-family: 'Press Start 2P', cursive; text-transform: uppercase; line-height: 1.6; }
h1 { font-size: 28pt; text-align: center; color: var(--color-accent-red); -webkit-text-stroke: 2px #000; text-shadow: 6px 6px 0px #000; animation: bounce 2s ease-in-out infinite; margin-bottom: 0.5cm; }
h2 { font-size: 14pt; color: #000; margin-bottom: 0.6cm; text-align: center; border-bottom: 4px solid #000; padding-bottom: 15px; }

p { text-align: left; line-height: 1.4; font-size: 18pt; margin-bottom: 0.5cm; color: #000; font-family: 'VT323', monospace; }

h2 + p::first-letter {
  font-family: 'Press Start 2P', cursive;
  font-size: 40pt;
  float: left;
  margin-right: 12px;
  line-height: 1;
  color: var(--color-accent-red);
  text-shadow: 3px 3px 0px #000;
}

.highlight { background-color: var(--color-highlight-default); color: #fff; padding: 2px 8px; border: 2px solid #000; font-weight: bold; font-size: 18pt; box-shadow: 2px 2px 0px #000; }

/* ============================================
   4. COMPONENTES
   ============================================ */

.retro-box {
  background-color: var(--color-retro-bg);
  border: 8px solid #000;
  box-shadow: inset -5px -5px 0px rgba(0,0,0,0.2), inset 5px 5px 0px rgba(255,255,255,0.5);
  padding: 1cm 1.2cm;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  position: relative;
}

.powerup-block, .q-block {
  border: 4px solid #000;
  padding: 15px;
  margin: 20px 0;
  box-shadow: 4px 4px 0 #000;
  background-color: #fff;
}

.fonte-box {
  margin-top: auto;
  font-size: 10pt;
  text-align: center;
  color: #666;
  border-top: 2px dashed #000;
  padding-top: 10px;
}

.footer-page {
  position: absolute;
  bottom: 3.5cm;
  right: 2.7cm;
  font-family: 'Press Start 2P', cursive;
  font-size: 12pt;
  color: #000;
}

.deco-img {
  position: absolute;
  image-rendering: pixelated;
  z-index: 15;
  pointer-events: none;
  filter: drop-shadow(4px 4px 0px rgba(0,0,0,0.3));
}

.fig-shy-guy { bottom: 1.5cm; right: 1.2cm; width: 65px; }
.fig-spiny { bottom: 1.8cm; left: 1.2cm; width: 65px; }
.fig-cogumelo-v { top: 1.2cm; right: 1.2cm; width: 55px; }
.fig-cogumelo-g { top: 1.2cm; right: 1.2cm; width: 55px; }
.fig-planta { bottom: 0.5cm; right: 1.5cm; width: 100px; }
.fig-estrela { top: 1.2cm; right: 1.2cm; width: 60px; animation: float 3s ease-in-out infinite; }
.fig-boo { top: 2cm; left: 1.2cm; width: 70px; opacity: 0.7; }
.fig-bob-omb { bottom: 1.5cm; right: 1.2cm; width: 70px; }
.fig-flor-fogo { top: 1.2cm; left: 1.2cm; width: 55px; }
.fig-flor-gelo { top: 1.2cm; left: 1.2cm; width: 55px; }
.fig-goomba { bottom: 1.2cm; left: 1.5cm; width: 50px; }
.fig-bowser { bottom: 0.5cm; right: 0.5cm; width: 180px; z-index: 16; }
.fig-toad { bottom: 1.5cm; left: 1.2cm; width: 65px; }
.fig-yoshi { bottom: 1.5cm; right: 1.2cm; width: 85px; transform: scaleX(-1); }
.fig-moedas { bottom: 1.2cm; left: 1.2cm; width: 45px; transform: scaleX(-1); animation: shine 2s infinite; }

/* ============================================
   5. PAGINAS ESPECIAIS
   ============================================ */

.page.cover {
  background-image: url('../img/capa.png');
  background-size: cover;
  background-position: center;
  image-rendering: pixelated;
  padding: 3cm 1cm;
}

.cover-box {
  background-color: transparent;
  border: none;
  box-shadow: none;
  display: flex;
  flex-direction: column;
  height: 100%;
  position: relative;
  justify-content: center;
  align-items: center;
}

.cover-text-container {
  position: absolute;
  top: 29%;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  width: auto;
  white-space: nowrap;
}

.cover-subtitle {
  color: #fff;
  text-shadow: 4px 4px 0 #000;
  font-size: 20px;
  animation: blink 1.5s step-end infinite;
  margin: 0;
  font-family: 'Press Start 2P', cursive;
}

.cover-author-badge {
  background: rgba(0,0,0,0.8);
  padding: 8px 20px;
  border: 2px solid #fff;
  border-radius: 8px;
  color: #fff;
  text-shadow: 2px 2px 0 #000;
  font-family: 'VT323', monospace;
}

.cover-author-main { font-size: 18px; }
.cover-author-footer { font-size: 16px; }

.cover-footer-container {
  position: absolute;
  bottom: 3%;
  left: 50%;
  transform: translateX(-50%);
  width: auto;
  white-space: nowrap;
}

.book-index {
  list-style: none;
  margin-top: 1cm;
  padding-left: 0;
  font-family: 'Press Start 2P', cursive;
  width: 100%;
}

.book-index li {
  margin-bottom: 20px;
  font-size: 10pt;
  border-bottom: 4px dashed #000;
  padding-bottom: 15px;
  text-align: center;
  line-height: 1.6;
}

.book-index a {
  color: #000;
  text-decoration: none;
  transition: color 0.2s;
}

.book-index a:hover { color: var(--color-accent-red); }

.index-mario-img {
  width: 300px;
  image-rendering: pixelated;
  margin-top: 80px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.boss-list {
  font-family: 'VT323', monospace;
  font-size: 18pt;
  margin-bottom: 0.8cm;
  padding-left: 1.5cm;
  color: #eee;
}

.ref-box {
  background-color: #fff;
  color: #000;
  border: 4px solid #000;
  padding: 1.5cm;
}

.ref-list {
  margin-top: 0.5cm;
  font-family: 'VT323', monospace;
  font-size: 13pt;
  text-align: center;
}

.ref-link-title { font-size: 13pt; }
.ref-link-desc { font-size: 10pt; }

.end-box {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  flex-grow: 1;
}

.end-img {
  width: 200px;
  image-rendering: pixelated;
  margin-bottom: 20px;
}

.end-title {
  color: #000;
  font-size: 24pt;
}

.end-footer-text {
  margin-top: 0.5cm;
  font-family: 'Press Start 2P', cursive;
  font-size: 8pt;
  color: #555;
}

/* ============================================
   6. TEMAS POR CAPITULO (custom properties)
   ============================================ */

.theme-data { background-color: var(--color-data-bg); }
.theme-data .retro-box { background-color: var(--color-data-bg); }
.theme-data .retro-box h2 { color: var(--color-data-heading); border-bottom-color: var(--color-data-accent); }
.theme-data h2 + p::first-letter { color: var(--color-data-accent); }
.theme-data .highlight { background-color: var(--color-data-accent); color: #000; }

.theme-human { background-color: var(--color-human-bg); }
.theme-human .retro-box { background-color: var(--color-human-bg); }
.theme-human .retro-box h2 { color: var(--color-human-heading); border-bottom-color: var(--color-human-accent); }
.theme-human h2 + p::first-letter { color: var(--color-human-accent); }
.theme-human .highlight { background-color: var(--color-human-accent); color: #fff; }

.theme-engine { background-color: var(--color-engine-bg); }
.theme-engine .retro-box { background-color: var(--color-engine-bg); }
.theme-engine .retro-box h2 { color: var(--color-engine-heading); border-bottom-color: var(--color-engine-accent); }
.theme-engine h2 + p::first-letter { color: var(--color-engine-accent); }
.theme-engine .highlight { background-color: var(--color-engine-accent); color: #fff; }

.theme-tokens { background-color: var(--color-tokens-bg); }
.theme-tokens .retro-box { background-color: var(--color-tokens-bg); }
.theme-tokens .retro-box h2 { color: var(--color-tokens-heading); border-bottom-color: var(--color-tokens-accent); }
.theme-tokens h2 + p::first-letter { color: var(--color-tokens-accent); }
.theme-tokens .highlight { background-color: var(--color-tokens-accent); color: #fff; }

.theme-impact { background-color: var(--color-impact-bg); }
.theme-impact .retro-box { background-color: var(--color-impact-bg); }
.theme-impact .retro-box h2 { color: var(--color-impact-heading); border-bottom-color: var(--color-impact-accent); }
.theme-impact h2 + p::first-letter { color: var(--color-impact-accent); }
.theme-impact .highlight { background-color: var(--color-impact-accent); color: #fff; }

.theme-archive { background-color: #e5d3b3; }
.theme-archive .retro-box { background-color: #fdf5e6; }
.theme-archive .retro-box h2 { color: #8b4513; border-bottom-color: #deb887; }
.theme-archive h2 + p::first-letter { color: #deb887; }

.theme-victory { background-color: var(--color-victory-bg); }
.theme-victory .retro-box { background-color: var(--color-victory-bg); }
.theme-victory .retro-box h2 { color: var(--color-victory-heading); border-bottom-color: var(--color-victory-accent); }
.theme-victory h2 + p::first-letter { color: var(--color-victory-accent); }

.theme-vanilla { background-color: #fcfcfc; }
.theme-vanilla .retro-box { background-color: #fcfcfc; }
.theme-vanilla .retro-box h2 { color: #000; border-bottom-color: #000; }

.boss-box { background-color: var(--color-boss-bg); color: #fff; border-color: var(--color-boss-heading); }
.boss-box h2 { color: var(--color-boss-heading); border-bottom-color: var(--color-boss-heading); }
.boss-box p { color: #eee; }
.boss-box h2 + p::first-letter { color: var(--color-boss-accent); text-shadow: 3px 3px 0px #000; }
.boss-box .highlight { background-color: var(--color-boss-accent); color: #000; }

/* ============================================
   7. UTILIDADES
   ============================================ */

.block-content-text { margin-bottom: 0; font-size: 14pt; }

.theme-green-block { background-color: #2ecc71; border-color: #000; }
.theme-blue-block { background-color: #3498db; color: #fff; }
.theme-orange-block { background-color: #f39c12; }
.theme-purple-block { background-color: #9b59b6; color: #fff; }
.theme-red-block { background-color: #c0392b; }

.bonus-list {
  font-family: 'VT323', monospace;
  font-size: 16pt;
  margin-bottom: 0.5cm;
  padding-left: 1.5cm;
}

.bonus-sublist {
  font-family: 'VT323', monospace;
  font-size: 14pt;
  margin-top: 10px;
  padding-left: 1cm;
  list-style: circle;
}

.bonus-highlight-green { color: #2ecc71; }
.bonus-highlight-blue { color: #3498db; }
.bonus-highlight-yellow { color: #f1c40f; }
.bonus-highlight-red { color: #e74c3c; }

.bonus-q-block {
  background-color: #273c75;
  color: #fff;
  border-color: #fbc531;
}

/* ============================================
   8. ANIMACOES
   ============================================ */

@keyframes shine { 0%, 100% { filter: brightness(1); } 50% { filter: brightness(1.5) drop-shadow(0 0 10px gold); } }
@keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }
@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
@keyframes blink { 0% { opacity: 1; } 50% { opacity: 0; } 100% { opacity: 1; } }

/* ============================================
   9. PRINT / PDF
   ============================================ */

@media print {
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;

  body {
    background: white !important;
    display: block !important;
  }

  .world-bg, #pipe-container, .ground-real {
    display: none !important;
  }

  .page {
    width: 21cm !important;
    height: 29.7cm !important;
    margin: 0 !important;
    box-shadow: none !important;
    page-break-after: always !important;
    break-after: page !important;
    padding: 1cm !important;
  }

  .retro-box {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
}
```

- [ ] **Step 2: Verificar que o visual permanece identico**

Abrir no navegador e comparar.

- [ ] **Step 3: Commit**

```bash
git add assets/css/style.css
git commit -m "refactor: reorganize style.css into 9 numbered sections"
```

---

### Task 4: Eliminar CSS inline do index.html — Capa e Indice

**Files:**
- Modify: `index.html:60-88`

- [ ] **Step 1: Substituir o HTML da capa com classes semanticas (sem style="")**

Substituir as linhas 60-71 por:

```html
<article class="page cover" aria-labelledby="title-1">
  <div class="retro-box cover-box">
    <div class="cover-text-container">
      <p class="cover-subtitle">&#9658; O CONHECIMENTO LIBERTA</p>
      <div class="cover-author-badge cover-author-main">PLAYER: Entusiasta de Tecnologia</div>
    </div>
    <div class="cover-footer-container">
      <div class="cover-author-badge cover-author-footer">Autor: Maycon Douglas</div>
    </div>
  </div>
</article>
```

- [ ] **Step 2: Substituir o HTML do indice com classe semantica**

Substituir a linha 86 (img do Mario) por:

```html
<img src="assets/img/Mario e Yoshi.png" alt="Mario e Yoshi" class="index-mario-img">
```

- [ ] **Step 3: Verificar capa e indice no navegador**

Visual deve permanecer identico.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "refactor: remove inline CSS from cover and index"
```

---

### Task 5: Eliminar CSS inline do index.html — Capitulos 1-4

**Files:**
- Modify: `index.html:90-176`

- [ ] **Step 1: Substituir blocos com style="" por classes nos capitulos 1-4**

Cap 1 (linhas 96-104): substituir os blocos por:

```html
<div class="q-block">
  <p class="block-content-text"><strong>CURIOSIDADE:</strong> Os modelos agora usam <em>"Curated Data"</em>. Em vez de lerem toda a internet (incluindo lixo digital), eles focam em raciocínio lógico, livros técnicos e código de alta qualidade.</p>
</div>
```

```html
<div class="powerup-block theme-green-block">
  <p class="block-content-text"><strong>ITEM SECRETO: Model Collapse</strong> — Se uma IA for treinada apenas com dados de outras IAs, ela começa a esquecer fatos raros e a cometer erros bizarros. O toque humano ainda é o "filtro de realidade" indispensável.</p>
</div>
```

Cap 2 (linhas 118-131):

```html
<div class="powerup-block">
  <p class="block-content-text"><strong>POWER-UP: DPO</strong> — Em 2026, o <em>Direct Preference Optimization</em> substituiu o RLHF complexo, permitindo que a IA aprenda preferências humanas diretamente matematicamente, sem precisar de um "modelo de recompensa" separado.</p>
</div>
```

```html
<div class="q-block theme-blue-block">
  <p class="block-content-text"><strong>DICA DO PLAYER: Chain of Thought</strong> — Quer que a IA resolva problemas complexos? Peça para ela "pensar passo a passo". Isso ativa neurônios de raciocínio sequencial que seriam ignorados em respostas diretas.</p>
</div>
```

Cap 3 (linhas 141-153):

```html
<div class="q-block">
  <p class="block-content-text"><strong>SISTEMA AGÊNTICO:</strong> Em 2026, não falamos mais apenas de "Chat". Os modelos são Agentes que usam o Transformer para planejar e executar ações em ferramentas externas (como seu navegador ou terminal).</p>
</div>
```

```html
<div class="powerup-block theme-orange-block">
  <p class="block-content-text"><strong>POWER-UP: Open Source</strong> — Em 2026, modelos como <strong>Llama 4</strong> e <strong>Gemma 4</strong> alcançaram o nível do GPT-5, permitindo que qualquer desenvolvedor rode uma Super IA em seu próprio hardware.</p>
</div>
```

Cap 4 (linhas 162-176):

```html
<div class="powerup-block">
  <p class="block-content-text"><strong>NEEDLE IN A HAYSTACK:</strong> O teste definitivo de 2026. Colocamos uma informação aleatória no meio de 1 milhão de tokens. Se a IA a encontra, sua "atenção" é perfeita. Gemini e Claude agora gabaritam esse teste.</p>
</div>
```

```html
<div class="q-block theme-purple-block">
  <p class="block-content-text"><strong>ESTRATÉGIA: RAG</strong> — Mesmo com janelas gigantes, o <em>Retrieval-Augmented Generation</em> ainda é usado para buscar dados em tempo real na web, garantindo que a IA nunca fique desatualizada.</p>
</div>
```

- [ ] **Step 2: Verificar capitulos 1-4 no navegador**

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "refactor: remove inline CSS from chapters 1-4"
```

---

### Task 6: Eliminar CSS inline do index.html — Chefao, Bonus, Referencias, Final

**Files:**
- Modify: `index.html:178-257`

- [ ] **Step 1: Substituir blocos com style="" por classes no capitulo 5 (Chefao)**

Linha 184 (`<ul style="font-family:...">`):

```html
<ul class="boss-list">
  <li>&#128300; <strong>Mapeamento de Conceitos:</strong> Identificaram o grupo de neurônios que ativa apenas para "Engenharia Genética" ou "Mentira".</li>
  <li>&#127753; <strong>Intervenção Direta:</strong> Ao "pinçar" esses neurônios, podemos forçar a IA a falar apenas de um assunto ou mudar seu tom.</li>
</ul>
```

Linha 190 (`style="background-color: #c0392b;"`):

```html
<div class="powerup-block theme-red-block">
  <p class="block-content-text"><strong>ALERTA DE BOSS: Alucinações</strong> — Nunca confie 100%. A IA é uma máquina de probabilidade, não de verdade. Ela pode gerar mentiras que parecem perfeitamente lógicas. Verifique sempre as fontes!</p>
</div>
```

- [ ] **Step 2: Substituir blocos com style="" por classes no Bonus**

Linhas 206-215 (`<ul style="...">` e `<ul style="...">`):

```html
<ul class="bonus-list">
  <li>&#128269; <strong class="bonus-highlight-green">Engenharia de Demanda Satisfeita</strong>: Não se trata de "vender", mas de usar LLMs para minerar dores reais. A IA analisa padrões em fóruns e redes sociais para encontrar lacunas de conhecimento, transformando a "curiosidade" em uma solução específica que as pessoas realmente buscam.</li>
  <li>&#128230; <strong class="bonus-highlight-blue">Ecossistemas de Valor Sintético</strong>: O fim do "produto único". Com a IA, criamos jornadas: um guia rápido (entrada), complementos dinâmicos (estímulo) e agentes especializados (mentoria). O valor não está no texto, mas na <strong>arquitetura da solução</strong>.</li>
  <li>&#127912; <strong class="bonus-highlight-yellow">Design Centrado na Dor</strong>: A IA permite que o produto se adapte ao usuário, e não o contrário. Exemplos de impacto real:
    <ul class="bonus-sublist">
      <li><strong>TDAH Infantil</strong>: IAs que ajustam o traço e a complexidade de livros de colorir para reduzir a sobrecarga cognitiva.</li>
      <li><strong>Cognição na Terceira Idade</strong>: Estímulos visuais nostálgicos gerados por IA para auxiliar na recuperação de memórias.</li>
    </ul>
  </li>
</ul>
```

Linha 217 (`<strong style="color: #e74c3c;">`):

```html
<p>O segredo final? O sucesso digital nasce do tripé: <strong class="bonus-highlight-red">Oferta Clara + Criativo de Impacto + Página Simples</strong>. A IA é o motor potente, mas o propósito humano é o volante que define a direção do sucesso.</p>
```

Linha 219 (`style="background-color: #273c75; color: #fff; border-color: #fbc531;"`):

```html
<div class="q-block bonus-q-block">
  <p class="block-content-text"><strong>CONCEITO MASTER: Agência</strong> — O futuro não é o chat, é a agência. IAs que não esperam ordens, mas que buscam proativamente atingir os objetivos que você definiu. O player agora é um Diretor.</p>
</div>
```

- [ ] **Step 3: Substituir blocos com style="" por classes nas Referencias**

Linha 229 (`style="background-color: #fff; color: #000; border: 4px solid #000; padding: 1.5cm;"`):

```html
<div class="retro-box ref-box">
```

Linha 232 (`<ul class="book-index" style="...">`):

```html
<ul class="book-index ref-list">
```

Linhas 233-241 (cada `<strong style="font-size: 13pt;">` e `<br><span style="font-size: 10pt;">`):

```html
<li><a href="https://arxiv.org/abs/1706.03762" target="_blank"><strong class="ref-link-title">Attention Is All You Need (2017)</strong></a><br><span class="ref-link-desc">Vaswani et al. O motor de toda IA moderna e do sistema de "Atenção".</span></li>
<li><a href="https://arxiv.org/abs/2001.08361" target="_blank"><strong class="ref-link-title">Scaling Laws for Neural LMs (2020)</strong></a><br><span class="ref-link-desc">Kaplan et al. A prova matemática de que mais dados e computação geram inteligência.</span></li>
<li><a href="https://arxiv.org/abs/2212.08073" target="_blank"><strong class="ref-link-title">Constitutional AI (2022)</strong></a><br><span class="ref-link-desc">Anthropic. Como o Claude se auto-regula com uma "Constituição" ética.</span></li>
<li><a href="https://arxiv.org/abs/2305.18290" target="_blank"><strong class="ref-link-title">Direct Preference Optimization (2023)</strong></a><br><span class="ref-link-desc">Rafailov et al. A técnica que simplificou o alinhamento humano (DPO).</span></li>
<li><a href="https://www.nature.com/articles/s41586-024-07546-0" target="_blank"><strong class="ref-link-title">Model Collapse (Nature 2024)</strong></a><br><span class="ref-link-desc">Shumailov et al. O alerta sobre o uso excessivo de dados sintéticos.</span></li>
<li><a href="https://www.anthropic.com/research/mapping-mind-language-model" target="_blank"><strong class="ref-link-title">Mapping the Mind of LLMs (2024)</strong></a><br><span class="ref-link-desc">A descoberta dos SAEs para abrir a "Caixa Preta" da inteligência artificial.</span></li>
<li><a href="https://arxiv.org/abs/2005.11401" target="_blank"><strong class="ref-link-title">Retrieval-Augmented Generation (2020)</strong></a><br><span class="ref-link-desc">Lewis et al. A estratégia de conectar a IA a dados externos (RAG).</span></li>
<li><a href="https://arxiv.org/abs/2201.11903" target="_blank"><strong class="ref-link-title">Chain-of-Thought Prompting (2022)</strong></a><br><span class="ref-link-desc">Wei et al. O segredo de pedir para a IA "pensar passo a passo".</span></li>
<li><a href="https://deepmind.google/technologies/gemini/static/pdf/Gemini_1_5_Report.pdf" target="_blank"><strong class="ref-link-title">Multimodal Technical Reports</strong></a><br><span class="ref-link-desc">Benchmarks de janelas de contexto e capacidades multimodais de 2024-2026.</span></li>
```

- [ ] **Step 4: Substituir blocos com style="" por classes na pagina Final**

Linha 248 (`style="justify-content: center; align-items: center; text-align: center; flex-grow: 1;"`):

```html
<div class="retro-box end-box">
```

Linha 249 (`style="width: 200px; image-rendering: pixelated; margin-bottom: 20px;"`):

```html
<img src="assets/img/star.png" alt="Estrela do Mario" class="end-img">
```

Linha 250 (`style="color: #000; font-size: 24pt;"`):

```html
<h2 id="title-end" class="end-title">FASE COMPLETA!</h2>
```

Linha 252 (`style="width: 200px; image-rendering: pixelated; margin-bottom: 20px;"`):

```html
<img src="assets/img/mario.png" alt="Mario" class="end-img">
```

Linha 253 (`style="margin-top: 0.5cm; font-family: 'Press Start 2P', cursive; font-size: 8pt; color: #555;"`):

```html
<p class="end-footer-text">PONTUAÇÃO: 99999<br>2026</p>
```

- [ ] **Step 5: Verificar todas as paginas no navegador**

- [ ] **Step 6: Commit**

```bash
git add index.html
git commit -m "refactor: remove all inline CSS from boss, bonus, refs and end pages"
```

---

### Task 7: Adicionar lazy loading nas imagens e preconnect de fonts

**Files:**
- Modify: `index.html:24-33,247-252`

- [ ] **Step 1: Adicionar preconnect do Google Fonts no `<head>`**

Antes de `<link href="https://fonts.googleapis.com/css2...">`, adicionar:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

- [ ] **Step 2: Adicionar `loading="lazy"` e `decoding="async"` nas imagens de decoracao**

Substituir as imagens do `.world-bg` (linhas 33-49) para incluir lazy loading:

```html
<div class="world-bg">
  <img src="assets/figures/nuvem.png" class="bg-cloud" style="top: 10%; left: -200px; width: 120px; animation-delay: 0s;" loading="lazy" decoding="async">
  <img src="assets/figures/nuvem.png" class="bg-cloud" style="top: 25%; left: -200px; width: 100px; animation-delay: 10s;" loading="lazy" decoding="async">
  <img src="assets/figures/nuvem.png" class="bg-cloud" style="top: 50%; left: -200px; width: 140px; animation-delay: 18s;" loading="lazy" decoding="async">
  <img src="assets/figures/bloco-interrogacao.png" class="bg-deco bg-block-1" alt="Bloco ?" loading="lazy" decoding="async">
  <img src="assets/figures/bloco-interrogacao.png" class="bg-deco bg-block-2" alt="Bloco ?" loading="lazy" decoding="async">
  <img src="assets/figures/bloco-interrogacao.png" class="bg-deco bg-block-3" alt="Bloco ?" loading="lazy" decoding="async">
  <img src="assets/figures/bloco-tijolo.png" class="bg-deco bg-brick-1" alt="Tijolinho" loading="lazy" decoding="async">
  <img src="assets/figures/bloco-tijolo.png" class="bg-deco bg-brick-2" alt="Tijolinho" loading="lazy" decoding="async">
  <img src="assets/figures/toad.png" class="bg-deco bg-toad" alt="Toad" loading="lazy" decoding="async">
  <img src="assets/figures/yoshi.png" class="bg-deco bg-yoshi" alt="Yoshi" loading="lazy" decoding="async">
  <img src="assets/figures/flor-fogo.png" class="bg-deco bg-flower-fire" alt="Flor de Fogo" loading="lazy" decoding="async">
  <img src="assets/figures/flor-gelo.png" class="bg-deco bg-flower-ice" alt="Flor de Gelo" loading="lazy" decoding="async">
  <img src="assets/figures/bullet-bill.png" class="bg-deco bg-bullet" alt="Bullet Bill" loading="lazy" decoding="async">
  <img src="assets/figures/bullet-bill.png" class="bg-deco bg-bullet-2" alt="Bullet Bill" loading="lazy" decoding="async">
</div>
```

Nota: as imagens de world-bg ainda possuem `style=""` para posicionamento individual. Isso e aceitavel pois sao estilos de instancia unica (posicao especifica por nuvem/elemento).

- [ ] **Step 3: Adicionar `loading="lazy"` e `decoding="async"` nas imagens de conteudo**

Na imagem do indice (`Mario e Yoshi.png`) e nas imagens do final (`star.png`, `mario.png`), adicionar `loading="lazy" decoding="async"`.

- [ ] **Step 4: Verificar que imagens carregam normalmente**

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "perf: add lazy loading, async decoding and font preconnect"
```

---

### Task 8: Corrigir script.js

**Files:**
- Modify: `assets/js/script.js`

- [ ] **Step 1: Reescrever script.js para observar scroll e destacar capitulo ativo no sidebar**

```javascript
document.addEventListener("DOMContentLoaded", () => {
  const sidebarLinks = document.querySelectorAll("#sidebar a");
  const sections = document.querySelectorAll("article h2[id]");

  if (!sidebarLinks.length || !sections.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          sidebarLinks.forEach((link) => {
            link.classList.toggle(
              "active",
              link.getAttribute("href") === `#${id}`
            );
          });
        }
      });
    },
    { rootMargin: "-30% 0px -70% 0px" }
  );

  sections.forEach((section) => observer.observe(section));
});
```

Adicionar no `style.css` (secao 2. LAYOUT, apos `#sidebar a:hover`):

```css
#sidebar a.active { color: #fff; padding-left: 5px; }
```

- [ ] **Step 2: Verificar que a sidebar destaca o capitulo ativo ao scrollar**

- [ ] **Step 3: Commit**

```bash
git add assets/js/script.js assets/css/style.css
git commit -m "fix: rewrite script.js to highlight active chapter in sidebar"
```

---

### Task 9: Verificacao final e commit

**Files:**
- All modified files

- [ ] **Step 1: Verificar zero `style=""` no index.html (exceto world-bg)**]

```bash
grep -n 'style="' index.html | grep -v 'world-bg' | grep -v 'bg-cloud' | grep -v 'bg-deco'
```

Esperado: sem resultados (as unicas excesoes sao os posicionamentos de instancia unica nas imagens de world-bg).

- [ ] **Step 2: Verificar que todas as custom properties estao definidas e usadas**

```bash
grep -c 'var(--color-' assets/css/style.css
```

Esperado: 20+ usos.

- [ ] **Step 3: Verificar que style.css tem os 9 cabecalhos de secao]

```bash
grep -c '===========' assets/css/style.css
```

Esperado: 9.

- [ ] **Step 4: Teste visual completo no navegador]

- [ ] **Step 5: Commit final]

```bash
git add -A
git commit -m "refactor: semantic sanitization complete — zero inline CSS, custom properties, organized stylesheet, lazy loading, fixed JS"
```
