document.addEventListener("DOMContentLoaded", () => {
    const sidebarList = document.getElementById("toc-list");
    const sections = document.querySelectorAll("article h2");

    sections.forEach((sec, index) => {
        // Garantir ID
        const id = `chapter-${index + 1}`;
        sec.id = id;

        // Criar link
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = `#${id}`;
        a.textContent = sec.textContent;
        
        li.appendChild(a);
        sidebarList.appendChild(li);
    });
});
