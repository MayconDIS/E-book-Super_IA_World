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
      const originalText = btnPdf.innerText;
      btnPdf.innerText = "GERANDO...";
      
      const element = document.body;
      
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
