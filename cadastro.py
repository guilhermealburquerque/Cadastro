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