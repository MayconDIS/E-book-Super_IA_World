# PDF Export Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Allow users to export the e-book as a PDF identically matching the screen view, natively via print and via a floating JS button.

**Architecture:** Update `@media print` CSS rules to stop hiding background layers. Inject `html2pdf.js` via CDN into `index.html` and add a sticky download button. Write a script function that captures `<main>` (or `body`) to create the PDF on click.

**Tech Stack:** HTML5, CSS3, JavaScript, html2pdf.js

---

### Task 1: Update CSS for Native Print and JS Styles

**Files:**
- Modify: `assets/css/style.css`
- Modify: `assets/css/cenario.css`

- [ ] **Step 1: Remove `display: none` from backgrounds in style.css**

Find the `@media print` block at the end of `assets/css/style.css`.
Remove the properties that hide the background layers from the selector:
```css
.world-bg, #pipe-container, .pipe-collar, .ground-real,
.deco-img, .footer-page {
display: none !important;
}
```
Replace with:
```css
/* Only hide elements that should definitely not print, like UI components if any */
#pipe-container, .pipe-collar, .footer-page {
display: none !important;
}
/* Keep .world-bg, .ground-real, .deco-img visible */
```

- [ ] **Step 2: Add styles for the floating PDF button in style.css**

Add this to `assets/css/style.css` (before `@media print`):
```css
#btn-pdf {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: var(--color-accent-red);
  color: #fff;
  font-family: 'Press Start 2P', cursive;
  font-size: 10pt;
  padding: 15px;
  border: 4px solid #000;
  box-shadow: 4px 4px 0px #000;
  cursor: pointer;
  z-index: 1000;
  transition: transform 0.2s;
}

#btn-pdf:hover {
  transform: scale(1.05);
}

@media print {
  #btn-pdf { display: none !important; }
}
```

- [ ] **Step 3: Remove `display: none` from backgrounds in cenario.css**

Find `@media print` in `assets/css/cenario.css`.
Change:
```css
@media print {
.world-bg,
.ground-real,
.bg-deco,
.bg-cloud {
display: none !important;
}
```
To:
```css
@media print {
/* Keep backgrounds visible for exact printing */
body {
padding-bottom: 0 !important;
overflow: visible !important;
}
}
```

- [ ] **Step 4: Commit CSS updates**
```bash
git add assets/css/style.css assets/css/cenario.css
git commit -m "style: enable backgrounds in print media and add pdf button style"
```

### Task 2: Update HTML with Library and Button

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add the floating button**

Add the button right before `</main>` or just inside `<body>` at the end:
```html
    <button id="btn-pdf">BAIXAR PDF</button>
```

- [ ] **Step 2: Add html2pdf library**

In `<head>` or before `</body>`, add the CDN:
```html
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
```

- [ ] **Step 3: Commit HTML updates**
```bash
git add index.html
git commit -m "feat: add PDF download button and html2pdf library"
```

### Task 3: Implement JavaScript Logic

**Files:**
- Modify: `assets/js/script.js`

- [ ] **Step 1: Add click listener to button**

At the end of `assets/js/script.js`, add:
```javascript
document.addEventListener('DOMContentLoaded', () => {
    const btnPdf = document.getElementById('btn-pdf');
    if(btnPdf) {
        btnPdf.addEventListener('click', () => {
            // Optional: change button text while generating
            const originalText = btnPdf.innerText;
            btnPdf.innerText = "GERANDO...";
            
            const element = document.body; // Capture entire body to include fixed backgrounds
            
            const opt = {
                margin:       0,
                filename:     'Super_IA_World_Ebook.pdf',
                image:        { type: 'jpeg', quality: 0.98 },
                html2canvas:  { scale: 2, useCORS: true, scrollY: 0 },
                jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
            };

            html2pdf().set(opt).from(element).save().then(() => {
                btnPdf.innerText = originalText;
            });
        });
    }
});
```

- [ ] **Step 2: Test the functionality**
Open `index.html` in the browser, verify the button appears. Click it, check if PDF downloads and contains backgrounds. Check `Ctrl+P` and verify backgrounds are visible when "Background graphics" is checked.

- [ ] **Step 3: Commit JS updates**
```bash
git add assets/js/script.js
git commit -m "feat: implement html2pdf logic for button click"
```
