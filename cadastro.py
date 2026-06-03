# ============================================================
#   SISTEMA ESCOLAR — EduTrack
#   Laboratório de Programação em Python
# ============================================================
 
# ==================== ESTRUTURAS DE DADOS ====================

# TUPLAS — dados fixos do sistema
TURNOS = ("Manhã", "Tarde", "Noite")
SITUACOES = ("Aprovado", "Reprovado", "Em andamento")
INFO_SISTEMA = ("EduTrack", "v1.0", "2025")

# DICIONÁRIOS — alunos e cursos cadastrados 
alunos = {}       # { ra: { nome, idade, turno, cursos, notas } }
cursos = {}       # { codigo: { nome, carga_horaria, professor } }

# SETS — RAs e códigos únicos (evita duplicação)
ras_cadastrados = set()
codigos_cursos = set()

# LISTAS — histórico de atividades
historico = []

# ==================== FUNÇÕES AUXILIARES ====================
 
def cabecalho(titulo):
    """Exibe um cabeçalho formatado."""
    print("\n" + "=" * 50)
    print(f"  {titulo}")
    print("=" * 50)

def pausar():
    """Pausa e espera o usuário."""
    input("\n  Pressione ENTER para continuar...")

def gerar_relatorio_aluno(ra):
    """Retorna string com relatório completo do aluno."""
    if ra not in alunos:
        return "Aluno não encontrado."
    a = alunos[ra]
    media = calcular_media(ra)
    situacao = "Aprovado" if media >= 6 else ("Em andamento" if media == 0 else "Reprovado")
    relatorio = (
        f"\n  RA: {ra}"
        f"\n  Nome: {a['nome']}"
        f"\n  Idade: {a['idade']} anos"
        f"\n  Turno: {a['turno']}"
        f"\n  Cursos matriculados: {len(a['cursos'])}"
        f"\n  Média geral: {media:.1f}"
        f"\n  Situação: {situacao}"
    )
    return relatorio

def calcular_media(ra):
    """Retorna a média das notas do aluno. Função com retorno."""
    if ra not in alunos or not alunos[ra]['notas']:
        return 0.0
    notas = alunos[ra]['notas']
    return sum(notas) / len(notas)

# LAMBDA — classifica a nota
classificar_nota = lambda n: "Excelente" if n >= 9 else ("Bom" if n >= 7 else ("Regular" if n >= 5 else "Insuficiente"))

# ==================== FUNÇÕES DE ALUNO ====================
 
def cadastrar_aluno():
    """Cadastra um novo aluno no sistema."""
    cabecalho("CADASTRAR ALUNO")
 
    ra = input("  Digite o RA do aluno: ").strip().upper()
    
    if ra in ras_cadastrados:
        print(f"\n  ❌ RA {ra} já cadastrado!")
        pausar()
        return

    nome = input("  Nome completo: ").strip()
    if not nome:
        print("\n  ❌ Nome não pode ser vazio!")
        pausar()
        return