# PDF Export Design

## Goal
Save E-book as PDF perfectly matching screen view (16-bit retro theme, backgrounds intact). Provide both native print (Ctrl+P) and JS automated button.

## Architecture & Components

### 1. Native Print (CSS)
- **Files**: `assets/css/style.css`, `assets/css/cenario.css`
- **Action**: Modify `@media print`. Remove `.world-bg`, `.ground-real`, `.bg-deco`, `.bg-cloud`, and `.deco-img` from `display: none !important`. 
- **Requirement**: User must check "Background graphics" in browser print dialog.

### 2. Automated PDF Button (JS)
- **Library**: `html2pdf.js` via CDN.
- **UI**: Floating button `Download PDF 16-bits`. Fixed position bottom-right.
- **Action**: Button click calls `html2pdf().from(document.querySelector('body')).save()`.
- **Styling**: `style.css` gets button styles (retro 8-bit button look). 

## Data Flow
User clicks button -> `html2pdf` captures `<body>` element -> Converts to canvas -> Generates PDF blob -> Triggers browser download.

## Edge Cases
- Animations might be captured mid-frame. `html2pdf` freezes frame.
- Background fixed positions might act weird in canvas rendering. We capture `body` to include `world-bg`.
