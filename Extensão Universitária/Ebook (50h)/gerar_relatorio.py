# -*- coding: utf-8 -*-
"""
Gera relatorio.html no padrão da pasta "1 - Cartilha (50h)" do CasalFlow:
relatório ABNT + a peça (o e-book Super IA World) reproduzida na íntegra no Anexo A.

O CSS e as folhas do Anexo A são lidos do código do e-book — nada é
reescrito à mão, para a cópia não divergir do original.
"""
import io, re, os

# O script mora ao lado do relatório. O e-book é procurado subindo as pastas até achar
# ebook.html: assim a pasta do relatório pode ser reorganizada sem quebrar o script.
PASTA = os.path.dirname(os.path.abspath(__file__))


def achar_ebook(inicio):
    atual = inicio
    while True:
        if os.path.isfile(os.path.join(atual, "ebook.html")):
            return atual
        pai = os.path.dirname(atual)
        if pai == atual:
            raise SystemExit("ebook.html não encontrado em nenhuma pasta acima de " + inicio)
        atual = pai


EBOOK = achar_ebook(PASTA)
CARTILHA = r"C:\Users\mayco\Documents\GitHub\CasalFlow\.planning\Extensões Universitárias\1 - Cartilha (50h)\relatorio.html"
SAIDA = os.path.join(PASTA, "relatorio.html")

# Caminho do relatório até a raiz do e-book. O Super IA World usa imagens PNG
# referenciadas por caminho relativo; dentro do relatório elas precisam subir pastas.
PREFIXO = os.path.relpath(EBOOK, PASTA).replace(os.sep, "/")


def ler(p):
    return io.open(p, encoding="utf-8").read()


def bloco(css, inicio):
    """Devolve (ini, fim) do bloco com chaves que começa em `inicio`."""
    abre = css.index("{", inicio)
    nivel, i = 0, abre
    while True:
        if css[i] == "{":
            nivel += 1
        elif css[i] == "}":
            nivel -= 1
            if nivel == 0:
                return inicio, i + 1
        i += 1


def remover(css, padrao):
    """Remove todos os blocos que começam com `padrao`; devolve (css, removidos)."""
    removidos = []
    while True:
        m = re.search(padrao, css)
        if not m:
            return css, removidos
        ini, fim = bloco(css, m.start())
        removidos.append(css[ini:fim])
        css = css[:ini] + css[fim:]


def reescrever_urls(css, pasta_css):
    """url() relativa ao módulo CSS -> relativa à pasta do relatório."""
    def troca(m):
        aspas, alvo = m.group(1), m.group(2)
        if alvo.startswith(("data:", "http:", "https:", "#", "/")):
            return m.group(0)
        absoluto = os.path.normpath(os.path.join(pasta_css, alvo))
        rel = os.path.relpath(absoluto, PASTA).replace(os.sep, "/")
        return "url(%s%s%s)" % (aspas, rel, aspas)
    return re.sub(r"url\(\s*(['\"]?)([^'\")]+)\1\s*\)", troca, css)


# ─────────────────────────── CSS do relatório (padrão Cartilha) ───────────────────────────
cartilha = ler(CARTILHA)
camada_relatorio = cartilha.split("@layer relatorio, peca;")[1].split("@layer peca {")[0]
script_imagens = "<script>" + cartilha.split("<script>")[1].split("</script>")[0] + "</script>"

acrescimo_relatorio = """
        @layer relatorio {
            /* 11. QUADRO DE CONTEÚDO (acréscimo deste relatório)
               Três colunas com texto corrido não cabem em 12pt sem quebrar a folha;
               a ABNT admite corpo menor em tabelas e quadros. */
            .table-conteudo { font-size: 10pt; }
            .table-conteudo th, .table-conteudo td { text-align: left; vertical-align: top; padding: 5px 7px; line-height: 1.3; }
            .table-conteudo td:first-child { font-weight: bold; width: 30%; }
        }
"""

# ─────────────────────────── CSS do e-book (camada peca) ───────────────────────────
PASTA_MODULOS = os.path.join(EBOOK, "assets", "css", "modules")
ordem = ["variables", "base", "layout", "components", "themes", "animations", "print"]
fora_do_escopo, dentro_do_escopo = [], []

for nome in ordem:
    css = ler(os.path.join(PASTA_MODULOS, nome + ".css"))
    css = reescrever_urls(css, PASTA_MODULOS)
    if nome == "variables":
        # :root não é descendente do anexo; dentro do @scope não casaria com nada.
        fora_do_escopo.append("/* ── variables.css ── */\n" + css)
        continue
    css, keyframes = remover(css, r"@keyframes\s+[\w-]+\s*\{")
    css, _pages = remover(css, r"@page\s*\{")
    if keyframes:
        fora_do_escopo.append("/* ── @keyframes de animations.css (não valem dentro de @scope) ── */\n" + "\n".join(keyframes))
    dentro_do_escopo.append("/* ── " + nome + ".css ── */\n" + css)

camada_peca = """
        @layer peca {
            /* Mesmo desenho da Cartilha: o relatório estiliza elementos nus (p, li,
               h1..h6, ul, ol, table) com recuo ABNT, justificação e 12pt; o reset em
               sub-camada `base` impede esse estilo de vazar para dentro do e-book, e
               `@scope` impede o e-book de vazar para fora. `arte` vence `base` sempre.

               Atenção: o e-book também chama as próprias folhas de `.page`. É o
               `@scope` que impede a regra `.page` dele de alcançar as folhas do
               relatório. */
            @layer base, arte;

            @layer base {
                .anexo-a, .anexo-a * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
                .anexo-a, .anexo-a * { box-sizing: border-box; margin: 0; padding: 0; }

                .anexo p, .anexo li, .anexo h1, .anexo h2, .anexo h3, .anexo h4,
                .anexo h5, .anexo h6, .anexo ul, .anexo ol,
                .anexo table, .anexo th, .anexo td {
                    margin: 0;
                    padding: 0;
                    text-indent: 0;
                    text-align: inherit;
                    line-height: inherit;
                    font-size: inherit;
                    color: inherit;
                    border: 0;
                    background-color: transparent;
                }
            }

            @layer arte {
                /* ═══ Anexo A: e-book "Super IA World" ═══
                   Copiado de assets/css/modules/ por script, com as url() ajustadas
                   para a pasta do relatório. Não editar aqui: corrigir no e-book e
                   regerar este relatório. */

%FORA%

                @scope (.anexo-a) {
%DENTRO%
                }

                /* O `body` do e-book (VT323, texto #333) não existe dentro do
                   relatório; sem isto o miolo das folhas herdaria Arial e preto. */
                .page.peca-a {
                    font-family: 'VT323', monospace;
                    color: #333;
                }

                @media screen {
                    .anexo > .page { margin-bottom: 30px; }
                }
            }
        }
""".replace("%FORA%", "\n".join(fora_do_escopo)).replace("%DENTRO%", "\n".join(dentro_do_escopo))

# ─────────────────────────── Folhas do e-book (Anexo A) ───────────────────────────
indice = ler(os.path.join(EBOOK, "ebook.html"))
main = indice.split("<main")[1].split("</main>")[0]
folhas = re.findall(r"(<article class=\"page.*?</article>)", main, flags=re.S)
assert len(folhas) == 10, "esperava 10 folhas, achei %d" % len(folhas)
folhas = [f.replace('<article class="page', '<article class="page peca-a', 1) for f in folhas]
folhas = [f.replace('src="assets/', 'src="%s/assets/' % PREFIXO) for f in folhas]
anexo = "\n\n".join(folhas)

# ─────────────────────────── Relatório ───────────────────────────
P = lambda t: '<span class="pendente">%s</span>' % t


def folha(id_, numero, corpo):
    num = '        <div class="page-number">%d</div>\n' % numero if numero else ""
    return '    <section class="page" id="%s">\n%s%s\n    </section>\n' % (id_, num, corpo)


capa = """    <section class="page" id="capa" aria-label="Capa do Trabalho">
        <header>
            <img src="assets/Logo UNIP.png" alt="Logo da Universidade Paulista" class="logo-unip" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/UNIP_Logo.svg/1200px-UNIP_Logo.svg.png'">
            <div class="capa-header uppercase">
                UNIVERSIDADE PAULISTA<br>
                ICET - INSTITUTO DE CIÊNCIAS EXATAS E TECNOLOGIA<br>
                CURSO SUPERIOR DE TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS<br><br><br>
                EXTENSÃO UNIVERSITÁRIA<br><br><br>
                RELATÓRIO DE ATIVIDADE DE EXTENSÃO — EBOOK<br>
                <span style="text-transform: none;">(Super IA World: Curiosidades da IA)</span><br>
                <span style="text-transform: none;">Carga horária: 50 horas</span>
            </div>
        </header>

        <table class="table-capa" aria-label="Tabela de Autores">
            <tr><th width="70%">Nome</th><th width="30%">R.A</th></tr>
            <tr>
                <td>Maycon Douglas Inácio Silva</td>
                <td>H719CD3</td>
            </tr>
        </table>

        <footer class="capa-footer uppercase">
            São José dos Campos - SP<br>""" + P("Maio / 2026 — confirmar") + """
        </footer>
    </section>
"""

SUMARIO = [
    ("dados-cadastro", "1. Dados de Cadastro", "%P_DADOS%"),
    ("descricao-1", "2. Descrição da Atividade", "%P_DESC%"),
    ("conclusao", "3. Conclusão e Resultados Alcançados", "%P_CONC%"),
    ("comprovacao", "4. Comprovação", "%P_COMP%"),
    ("anexo-a", "Anexo A &ndash; E-book &quot;Super IA World&quot; na íntegra", "%P_ANEXO%"),
]
sumario = '    <section class="page" id="sumario">\n        <h2>Sumário</h2>\n'
for alvo, rotulo, pag in SUMARIO:
    sumario += """
        <div class="sumario-item">
            <a href="#%s">%s</a>
            <div class="sumario-dots"></div>
            <span>%s</span>
        </div>
""" % (alvo, rotulo, pag)
sumario += "    </section>\n"

paginas = []  # (id, corpo) — numeradas a partir da folha 3

paginas.append(("dados-cadastro", """        <h2>1. Dados de Cadastro</h2>

        <h3>Campus</h3>
        <p>Campus SJC Dutra - São José dos Campos (SP)</p>

        <h3>Alunos Participantes</h3>
        <table>
            <thead>
                <tr>
                    <th>Número</th>
                    <th>R.A.</th>
                    <th>Nome</th>
                    <th>Curso</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>H719CD3</td>
                    <td>Maycon Douglas Inácio Silva</td>
                    <td>Análise e Desenvolvimento de Sistemas</td>
                </tr>
            </tbody>
        </table>
        <p class="no-indent"><em>Turma: DS3A48</em></p>
        <p class="no-indent"><em>Atividade realizada individualmente, abrangendo pesquisa, redação, design e desenvolvimento da obra.</em></p>

        <h3>Período</h3>
        <p>Ano: 2026 | Semestre: 3º</p>

        <h3>Área Temática e Projeto</h3>
        <p>TRABALHO, ECONOMIA E ADMINISTRAÇÃO &middot; Programas e projetos desenvolvidos para a comunidade.</p>

        <h3>Ação</h3>
        <p>Ebook (50 horas)</p>

        <h3>Organização Parceira e Público Beneficiário</h3>
        <table class="table-dados">
            <tr><td>Organização Parceira</td><td>""" + P("informar a escola, biblioteca, curso técnico ou coletivo atendido") + """</td></tr>
            <tr><td>Público Beneficiário</td><td>Estudantes e comunidade externa interessados em Inteligência Artificial</td></tr>
        </table>"""))

paginas.append(("descricao-1", """        <h2>2. Descrição da Atividade</h2>
        <h3>2.1 Descrição Geral da Atividade</h3>
        <p>A presente atividade de extensão universitária consistiu na pesquisa, redação,
        design e desenvolvimento do e-book <strong>&quot;Super IA World: Curiosidades da
        IA&quot;</strong>, obra digital gratuita de 10 folhas em formato A4, com cerca de
        1.600 palavras, que apresenta curiosidades sobre Inteligência Artificial usando a
        estética retrô de 16 bits inspirada em <em>Super Mario World</em>.</p>

        <p>A obra aproxima o público não especialista de conceitos técnicos da área —
        dados de treinamento, alinhamento de modelos, arquitetura Transformer, tokens,
        janelas de contexto e interpretabilidade — usando a linguagem visual de um jogo
        clássico como ponto de entrada. Cada capítulo é apresentado como uma fase, com
        blocos de destaque em forma de curiosidade, dica e <em>power-up</em>, e encerra com a
        fonte utilizada. O conteúdo foi atualizado para maio de 2026.</p>

        <h4>Estrutura do conteúdo</h4>
        <p>A obra é organizada em capítulos temáticos, antecedidos por capa e índice e
        seguidos de uma folha final, conforme apresentado no Quadro 1.</p>"""))

quadro = [
    ("Mundo 1-1 — O Apetite por Dados", "Volume de dados de treinamento, leis de escala, dados curados, dados sintéticos e colapso de modelo"),
    ("Mundo 1-2 — O Fator Humano", "RLHF, IA Constitucional, DPO, cadeia de raciocínio (<em>Chain of Thought</em>) e <em>Red Teaming</em>"),
    ("Mundo 1-3 — O Motor Transformer", "Mecanismo de atenção, <em>self-attention</em>, sistemas agênticos, modelos abertos e <em>Mixture of Experts</em>"),
    ("Mundo 1-4 — Tokens e Contexto", "Tokens e espaço vetorial, teste <em>needle in a haystack</em>, janelas de contexto, RAG e <em>context caching</em>"),
    ("Fase do Chefão — A Caixa Preta", "Habilidades emergentes, interpretabilidade mecanística, <em>Sparse Autoencoders</em> e alucinações"),
    ("Bônus — A Fusão: IA + Impacto Humano", "Hiper-personalização, design centrado na dor e agência"),
    ("Mundo Especial — Referências", "Nove artigos e marcos da área, com link"),
]
linhas = "\n".join("                <tr><td>%s</td><td>%s</td></tr>" % l for l in quadro)

paginas.append(("descricao-2", """        <h2>2. Descrição da Atividade (continuação)</h2>
        <p class="figure-title">Quadro 1 – Capítulos do e-book e conceitos de Inteligência Artificial tratados</p>
        <table class="table-conteudo">
            <thead>
                <tr><th>Capítulo</th><th>Conceitos tratados</th></tr>
            </thead>
            <tbody>
%s
            </tbody>
        </table>
        <p class="caption">Fonte: Elaborado pelo autor (2026).</p>""" % linhas))

paginas.append(("descricao-3", """        <h2>2. Descrição da Atividade (continuação)</h2>
        <h4>Desenvolvimento técnico</h4>
        <p>A peça foi construída como aplicação web estática, sem framework e sem
        bibliotecas de terceiros.</p>
        <ul>
            <li><strong>HTML5 semântico:</strong> 311 linhas, estruturadas com
            <code>main</code>, <code>article</code>, <code>nav</code>, <code>aside</code> e
            <code>footer</code>, com rótulos de acessibilidade nas folhas e título da capa
            acessível a leitores de tela.</li>
            <li><strong>CSS modular em arquitetura SMACSS:</strong> 728 linhas em 9 arquivos,
            sendo sete módulos separados por responsabilidade (variáveis, base, layout,
            componentes, temas, animações e impressão), o arquivo central de importação e o
            do cenário de fundo.</li>
            <li><strong>JavaScript sem bibliotecas:</strong> 73 linhas organizadas em funções
            de responsabilidade única, incluindo o botão de exportação para PDF.</li>
            <li><strong>Ilustração:</strong> 28 imagens PNG — personagens, blocos e elementos
            de cenário da estética 16 bits —, com tratamento de imagem e composição
            realizados no Canva.</li>
            <li><strong>Temas por capítulo:</strong> cada fase recebe uma paleta de cor própria,
            aplicada por classes de tema.</li>
        </ul>

        <h4>Impressão</h4>
        <p>A obra reproduz o formato A4 exato por meio de regras de impressão
        (<code>@media print</code>), preservando as imagens e as cores de fundo na
        exportação para PDF, o que permite distribuir a versão impressa com a mesma
        diagramação da digital.</p>"""))

paginas.append(("participacao", """        <h2>2.2 Descrição da Participação de Cada Aluno</h2>
        <h4>Maycon Douglas Inácio Silva (R.A. H719CD3)</h4>
        <p>Atuou em <strong>todas as etapas da obra: pesquisa, redação, design e
        desenvolvimento</strong>, aplicando conhecimentos das disciplinas de <em>Programação
        Web</em>, <em>Engenharia de Software</em> e <em>Interface Homem-Computador</em>. Foi
        responsável por pesquisar e selecionar os conteúdos e as nove referências sobre
        Inteligência Artificial, redigir os capítulos em linguagem acessível, compor a
        identidade visual de 16 bits com tratamento das imagens no Canva, estruturar o CSS em
        arquitetura modular e codificar o suporte a impressão em A4 — reproduzido na íntegra
        no Anexo A deste relatório.</p>"""))

paginas.append(("conclusao", """        <h2>3. Conclusão e Resultados Alcançados</h2>
        <p>A atividade entregou à comunidade uma obra introdutória e gratuita sobre
        Inteligência Artificial, que usa a linguagem visual de um jogo clássico para tornar
        acessíveis conceitos técnicos da área, disponível em formato digital e em versão para
        impressão em A4.</p>

        <p>A atividade atendeu diretamente """ + P("informar o número de pessoas atendidas presencialmente e onde") + """.</p>

        <p class="no-indent">Resultados objetivos e verificáveis:</p>
        <ul>
            <li><strong>7 capítulos em 10 folhas A4</strong>, com capa, índice e folha final.</li>
            <li><strong>Nove referências</strong> com link direto para os artigos e marcos citados.</li>
            <li><strong>Versão para impressão A4</strong> fiel à versão digital.</li>
            <li><strong>Código-fonte aberto</strong> em repositório público, com histórico de versões.</li>
        </ul>

        <p class="no-indent">A atividade está alinhada aos seguintes <strong>Objetivos de
        Desenvolvimento Sustentável (ODS) da ONU</strong>:</p>
        <ul>
            <li><strong>ODS 4 (Educação de Qualidade):</strong> material didático gratuito sobre Inteligência Artificial em linguagem acessível.</li>
            <li><strong>ODS 9 (Indústria, Inovação e Infraestrutura):</strong> divulgação de conceitos centrais da inovação tecnológica recente.</li>
            <li><strong>ODS 10 (Redução das Desigualdades):</strong> acesso gratuito e código aberto, reutilizável por terceiros.</li>
        </ul>"""))

paginas.append(("conclusao-2", """        <h2>3. Conclusão e Resultados Alcançados (continuação)</h2>

        <h3>3.1 Local onde a atividade foi realizada</h3>
        <p>A obra foi desenvolvida pelo aluno e disponibilizada em repositório público.
        """ + P("Informar o local e a data da apresentação ou distribuição presencial — as Orientações da UNIP (p. 6) exigem que a atividade seja realizada presencialmente.") + """</p>

        <h3>3.2 Considerações Finais</h3>
        <ul>
            <li><strong>Dificuldades enfrentadas:</strong> a principal foi garantir que a
            exportação para PDF fosse fiel à versão digital — dimensões A4 rigorosas, imagens de
            fundo preservadas na impressão e tipografia ajustada à folha —, o que exigiu
            sucessivas correções registradas no histórico do projeto.</li>
            <li><strong>Sugestões:</strong> como a área de Inteligência Artificial evolui
            rapidamente, recomenda-se revisar periodicamente os capítulos que citam modelos e
            técnicas recentes.</li>
            <li><strong>Observações:</strong> o conteúdo da obra reflete o estado da área em
            maio de 2026, data da última atualização.</li>
        </ul>"""))

paginas.append(("comprovacao", """        <h2>4. Comprovação</h2>
        <p>A comprovação da atividade fundamenta-se na própria peça produzida, reproduzida na
        íntegra no <strong>Anexo A</strong> a partir da folha %P_ANEXO%, no repositório público
        da obra e nas capturas apresentadas a seguir.</p>
        <p class="no-indent">O anexo reproduz a peça como ela é distribuída — mesma diagramação,
        mesmo formato de impressão. Por isso as folhas do anexo não recebem o número de página do
        relatório, que cairia sobre a arte; o sumário anuncia onde o anexo começa. Imprimir apenas
        o intervalo do anexo devolve a peça pronta para uso.</p>

        <h3>Comprovação 1 — Capa e índice do e-book</h3>
        <p class="figure-title">Figura 1 – Capa e Mapa do Mundo (índice) do e-book &quot;Super IA World&quot;</p>
        <div class="image-container">
            <img src="assets/1.png" alt="Capa e índice do e-book Super IA World" class="dynamic-img"
                 title="Clique para trocar a imagem (JPG, PNG, WEBP)">
            <p class="caption">Fonte: Acervo do autor (2026) — reprodução da peça produzida na atividade.</p>
        </div>"""))

paginas.append(("comprovacao-2", """        <h2>4. Comprovação (continuação)</h2>

        <h3>Comprovação 2 — Visão geral das 10 folhas</h3>
        <p class="figure-title">Figura 2 – As 10 folhas do e-book, cada capítulo com seu tema de cor</p>
        <div class="image-container">
            <img src="assets/2.png" alt="Miniaturas das 10 folhas do e-book" class="dynamic-img"
                 title="Clique para trocar a imagem (JPG, PNG, WEBP)">
            <p class="caption">Fonte: Acervo do autor (2026) — reprodução da peça produzida na atividade.</p>
        </div>

        <h3>Demais evidências</h3>
        <ul>
            <li><strong>Código-fonte com histórico de versões:</strong> github.com/MayconDIS/E-book-Super_IA_World</li>
            <li><strong>Registro da ação presencial:</strong> """ + P("anexar lista de presença e registro fotográfico") + """</li>
            <li><strong>Carta de Apresentação institucional:</strong> """ + P("anexar, se a atividade foi realizada junto a organização parceira") + """</li>
        </ul>"""))

# Numeração: capa e sumário não levam número; o corpo começa na folha 3.
PRIMEIRA = 3
numero = {pid: PRIMEIRA + i for i, (pid, _) in enumerate(paginas)}
folha_anexo = PRIMEIRA + len(paginas)
subst = {
    "%P_DADOS%": numero["dados-cadastro"],
    "%P_DESC%": numero["descricao-1"],
    "%P_CONC%": numero["conclusao"],
    "%P_COMP%": numero["comprovacao"],
    "%P_ANEXO%": folha_anexo,
}

corpo = capa + "\n" + sumario + "\n" + "\n".join(folha(pid, numero[pid], c) for pid, c in paginas)

cabecalho = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Extensão Universitária — Ebook (50h) — Super IA World</title>
    <!--
      ────────────────────────────────────────────────────────────────────────
      RELATÓRIO DE ATIVIDADE DE EXTENSÃO UNIVERSITÁRIA (50 horas)
      UNIP · ICET · CST em Análise e Desenvolvimento de Sistemas
      Ação: Ebook

      Formato ABNT: A4, margens 3cm superior/esquerda e 2cm inferior/direita,
      Arial 12pt, parágrafo justificado com recuo de 1,5cm.
      Para gerar o PDF: abrir no Chrome, anexar as imagens da seção 4 clicando
      sobre elas (se quiser trocá-las) e imprimir (Ctrl+P) na MESMA sessão, com
      "Gráficos de segundo plano" marcado.

      O ANEXO A (folhas %P_ANEXO% a %P_ANEXO_FIM%) é o e-book. Para tirar a peça para
      distribuir: Ctrl+P, intervalo de páginas %P_ANEXO%-%P_ANEXO_FIM%, papel A4 e
      "Gráficos de segundo plano" marcado.

      O Anexo A é CÓPIA de ebook.html e assets/css/modules/, gerada por
      gerar_relatorio.py. As imagens do e-book são lidas da pasta assets/ na
      raiz do repositório: abrir este arquivo a partir do repositório.
      Se o e-book mudar, regerar este relatório — não editar o anexo à mão.

      PENDÊNCIAS: todo trecho com fundo amarelo tracejado (.pendente) depende de
      informação que só o aluno tem. Resolver todos antes de submeter.
      ────────────────────────────────────────────────────────────────────────
    -->
    <style>
        @layer relatorio, peca;
""" + camada_relatorio + acrescimo_relatorio + camada_peca + """    </style>
    <!-- Tipografia da peça (Anexo A). -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap" rel="stylesheet">
</head>
<body>

"""

rodape = """

    <!-- ═════════════ ANEXO A — O E-BOOK NA ÍNTEGRA ═════════════
         Folhas %P_ANEXO% a %P_ANEXO_FIM%. Reproduzem a peça como ela é distribuída, e por
         isso NÃO levam o número de página do relatório: ele cairia sobre a arte.
         O sumário anuncia onde o anexo começa. -->
    <div class="anexo anexo-a" id="anexo-a">
""" + anexo + """
    </div>

    """ + script_imagens + """
</body>
</html>
"""

html = cabecalho + corpo + rodape
subst["%P_ANEXO_FIM%"] = folha_anexo + len(folhas) - 1
for k, v in subst.items():
    html = html.replace(k, str(v))

io.open(SAIDA, "w", encoding="utf-8").write(html)
print("relatorio.html gerado:", SAIDA)
print("folhas do relatório: capa, sumário, %d a %d" % (PRIMEIRA, folha_anexo - 1))
print("anexo A: folhas %d a %d (%d folhas)" % (folha_anexo, subst["%P_ANEXO_FIM%"], len(folhas)))
print("pendências marcadas:", html.count('class="pendente"'))
print("tamanho:", round(len(html.encode('utf-8')) / 1024, 1), "KB")
