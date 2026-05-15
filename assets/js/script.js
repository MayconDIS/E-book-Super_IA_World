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
  // PDF Export Logic
  const btnPdf = document.getElementById('btn-pdf');
  if(btnPdf) {
    btnPdf.addEventListener('click', () => {
      window.print();
    });
  }
});
