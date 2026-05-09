# Plano de Execução - Fase 7: Auditoria de UAT Final

## Objetivo
Validar todos os critérios de aceite definidos no `REQUIREMENTS.md` para garantir que o projeto está pronto para o lançamento oficial.

## Tarefas (Ondas)

### Onda 1: Validação Técnica e Funcional
- [ ] **T01**: Verificar se o sumário dinâmico no JS está mapeando todos os capítulos corretamente.
- [ ] **T02**: Testar a responsividade em resoluções comuns (1920x1080, 1366x768, Tablet).
- [ ] **T03**: Validar o contraste de cores no "Modo Chefão" (fundo escuro).

### Onda 2: Validação de Exportação
- [ ] **T04**: Simular impressão PDF e verificar se os `bricks.avif` e `cover-map.png` são renderizados sem erros.
- [ ] **T05**: Garantir que as quebras de página (`page-break-after`) estão funcionando em todos os navegadores principais.

### Onda 3: SEO e Metadados
- [ ] **T06**: Validar tags Open Graph e Twitter Cards para compartilhamento social.
- [ ] **T07**: Verificar se o `author` e `description` estão corretos.

## Critérios de Verificação
1. Todos os links do sumário funcionam (scroll suave).
2. O PDF gerado tem menos de 5MB.
3. Nota de acessibilidade (Lighthouse) > 90.
