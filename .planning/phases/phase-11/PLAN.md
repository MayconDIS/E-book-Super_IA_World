# Plano de Execução - Fase 11: Organização Estrutural de Arquivos (GSD)

## Objetivo
Organizar a estrutura do repositório e do código-fonte para seguir padrões profissionais de desenvolvimento, separando assets, componentes e documentação legada.

## Tarefas (Ondas)

### Onda 1: Estrutura de Pastas
- [ ] **T01**: Criar diretório `assets/` e subpastas `img/`, `pdf/`, `css/`, `js/`.
- [ ] **T02**: Mover imagens (`.png`, `.avif`) para `assets/img/`.
- [ ] **T03**: Mover arquivos PDF para `assets/pdf/`.
- [ ] **T04**: Mover `style.css` para `assets/css/` e `script.js` para `assets/js/`.
- [ ] **T05**: Mover a pasta `example/` para um diretório de arquivo ou removê-la se não for mais necessária (arquivamento GSD).

### Onda 2: Refatoração de Caminhos
- [ ] **T06**: Atualizar referências no `index.html` para os novos caminhos dos assets.
- [ ] **T07**: Atualizar referências de imagem no `style.css`.

### Onda 3: Organização do HTML
- [ ] **T08**: Adicionar comentários estruturais no `index.html` (Separando Header, Chapters, Footer).
- [ ] **T09**: Garantir que cada "página" (`article`) tenha um identificador único e consistente.

## Critérios de Verificação
1. O site carrega perfeitamente após a movimentação dos arquivos.
2. A raiz do projeto contém apenas arquivos de configuração (`.gitignore`, `index.html`, `README.md`) e pastas estruturadas.
3. O build de impressão (PDF) continua funcionando.
