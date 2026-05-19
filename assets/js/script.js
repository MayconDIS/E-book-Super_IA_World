/**
 * script.js
 * Lógica principal da aplicação estruturada sob os princípios de Clean Code:
 * - Nomenclatura descritiva.
 * - Separação de responsabilidades (Single Responsibility).
 * - Funções pequenas focadas em apenas uma tarefa.
 */

document.addEventListener("DOMContentLoaded", initializeApplication);

function initializeApplication() {
    setupPdfExportButton();
    setupSidebarScrollTracking();
}

/**
 * Configura o botão de exportar para PDF.
 */
function setupPdfExportButton() {
    const btnPdf = document.getElementById("btn-pdf");
    if (btnPdf) {
        btnPdf.addEventListener("click", () => window.print());
    }
}

/**
 * Configura o observer para atualizar o sidebar ativo baseado no scroll.
 */
function setupSidebarScrollTracking() {
    const sidebarLinks = document.querySelectorAll("#sidebar a");
    const sections = document.querySelectorAll("article h2[id]");

    if (!sidebarLinks.length || !sections.length) {
        return;
    }

    const observerOptions = {
        rootMargin: "-30% 0px -70% 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        handleIntersectingSections(entries, sidebarLinks);
    }, observerOptions);

    sections.forEach((section) => observer.observe(section));
}

/**
 * Atualiza os links do sidebar conforme as seções ficam visíveis na tela.
 * 
 * @param {IntersectionObserverEntry[]} entries 
 * @param {NodeListOf<Element>} sidebarLinks 
 */
function handleIntersectingSections(entries, sidebarLinks) {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            updateActiveSidebarLink(entry.target.id, sidebarLinks);
        }
    });
}

/**
 * Alterna a classe 'active' no link correspondente à seção atual.
 * 
 * @param {string} activeSectionId 
 * @param {NodeListOf<Element>} sidebarLinks 
 */
function updateActiveSidebarLink(activeSectionId, sidebarLinks) {
    sidebarLinks.forEach((link) => {
        const isMatchingLink = link.getAttribute("href") === `#${activeSectionId}`;
        link.classList.toggle("active", isMatchingLink);
    });
}
