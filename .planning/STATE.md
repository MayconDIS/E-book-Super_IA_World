# Estado do Projeto

## Resumo da Sessão Atual
- **Data**: 15/05/2026
- **Status**: Exportação em PDF e refatoração concluída com sucesso. 
- **Próximo Passo**: Realizar o Deploy / Lançamento do e-book e empacotamento final.

## Decisões Recentes
- Uso da funcionalidade nativa `window.print()` ao invés da dependência pesada `html2pdf.js`.
- O layout web foi refatorado para usar o tamanho estrito A4 (`21cm x 29.7cm`) com escalonamento de fontes, garantindo simetria 1:1 entre a tela e a versão impressa.
- Os elementos decorativos de cenário (`world-bg`, `ground-real`, etc.) foram liberados para o PDF, com a recomendação ao usuário de marcar "Gráficos de fundo".
- Bug do script `IntersectionObserver` corrigido, movendo a lógica do botão PDF para cima.

## Verificação GSD (UAT)
- [x] O botão "BAIXAR PDF" funciona perfeitamente independente da barra lateral.
- [x] O tamanho e paddings do `.page` respeitam limites físicos A4 e não vazam do container.
- [x] Estilos de impressão (`@media print`) acionados corretamente para remover elementos de interface.

## Pontos de Bloqueio
- Nenhum identificado.

## Notas Técnicas
- O `index.html` usa um sistema de `article.page` que facilita a exportação para PDF via Print-to-PDF.
- Toda modificação de fonte ou bloco de capítulo deve obedecer os limites estabelecidos de 29.7cm para não gerar páginas em branco ou cortadas na impressão.
