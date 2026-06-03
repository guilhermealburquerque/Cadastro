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
    
    try:
        idade = int(input("  Age: "))
    except ValueError:
        print("\n  ❌ Idade inválida!")
        pausar()
        return

 # Exibir turnos (TUPLA)
    print("\n  Turnos disponíveis:")
    for i, turno in enumerate(TURNOS, 1):
        print(f"    {i}. {turno}")
 
    try:
        opcao_turno = int(input("  Escolha o turno (1-3): "))
        turno = TURNOS[opcao_turno - 1] if 1 <= opcao_turno <= 3 else "Manhã"
    except (ValueError, IndexError):
        turno = "Manhã"

# Adicionar ao dicionário e set
    alunos[ra] = {
        "nome": nome,
        "idade": idade,
        "turno": turno,
        "cursos": [],
        "notas": []
    }
    ras_cadastrados.add(ra)
    historico.append(f"Aluno cadastrado: {nome} (RA: {ra})")
 
    print(f"\n  ✅ Aluno {nome} cadastrado com sucesso!")
    pausar()
 
def listar_alunos():
    """Lista todos os alunos cadastrados."""
    cabecalho("LISTA DE ALUNOS")
 
    if not alunos:
        print("  Nenhum aluno cadastrado.")
        pausar()
        return

# LIST COMPREHENSION — nomes dos alunos em ordem
    nomes_ordenados = sorted([f"{v['nome']} (RA: {k})" for k, v in alunos.items()])
 
    print(f"  Total de alunos: {len(alunos)}\n")
    for i, entrada in enumerate(nomes_ordenados, 1):
        print(f"  {i}. {entrada}")
 
    pausar()
 
def consultar_aluno():
    """Consulta dados de um aluno pelo RA."""
    cabecalho("CONSULTAR ALUNO")
 
    ra = input("  Digite o RA: ").strip().upper()

 # Operador ternário
    mensagem = gerar_relatorio_aluno(ra) if ra in alunos else "\n  ❌ Aluno não encontrado."
    print(mensagem)
 
    if ra in alunos and alunos[ra]['cursos']:
        print(f"\n  Cursos matriculados:")
        for c in alunos[ra]['cursos']:
            print(f"    - {c}")
 
    if ra in alunos and alunos[ra]['notas']:
        print(f"\n  Notas registradas:")
        for i, nota in enumerate(alunos[ra]['notas'], 1):
            print(f"    Nota {i}: {nota:.1f} — {classificar_nota(nota)}")
 
    pausar()

def lancar_nota():
    """Lança nota para um aluno."""
    cabecalho("LANÇAR NOTA")
 
    ra = input("  RA do aluno: ").strip().upper()
 
    if ra not in alunos:
        print("\n  ❌ Aluno não encontrado.")
        pausar()
        return
 
    try:
        nota = float(input(f"  Digite a nota de {alunos[ra]['nome']} (0 a 10): "))
    except ValueError:
        print("\n  ❌ Nota inválida!")
        pausar()
        return
 
    if 0 <= nota <= 10:
        alunos[ra]['notas'].append(nota)
        historico.append(f"Nota {nota} lançada para {alunos[ra]['nome']} (RA: {ra})")
        media = calcular_media(ra)
        situacao = "Aprovado ✅" if media >= 6 else "Reprovado ❌"
        print(f"\n  ✅ Nota lançada! Classificação: {classificar_nota(nota)}")
        print(f"  Nova média: {media:.1f} — {situacao}")
    else:
        print("\n  ❌ Nota deve ser entre 0 e 10.")
 
    pausar()

# ==================== FUNÇÕES DE CURSO ====================
 
def cadastrar_curso():
    """Cadastra um novo curso."""
    cabecalho("CADASTRAR CURSO")
 
    codigo = input("  Código do curso (ex: MAT01): ").strip().upper()
 
    if codigo in codigos_cursos:
        print(f"\n  ❌ Código {codigo} já existe!")
        pausar()
        return
 
    nome = input("  Nome do curso: ").strip()
    professor = input("  Nome do professor: ").strip()
 
    try:
        carga = int(input("  Carga horária (horas): "))
    except ValueError:
        carga = 40
 
    cursos[codigo] = {
        "nome": nome,
        "professor": professor,
        "carga_horaria": carga
    }
    codigos_cursos.add(codigo)
    historico.append(f"Curso cadastrado: {nome} ({codigo})")
 
    print(f"\n  ✅ Curso '{nome}' cadastrado com sucesso!")
    pausar()

def listar_cursos():
    """Lista todos os cursos disponíveis."""
    cabecalho("LISTA DE CURSOS")
 
    if not cursos:
        print("  Nenhum curso cadastrado.")
        pausar()
        return
 
    print(f"  Total de cursos: {len(cursos)}\n")
    for cod, c in cursos.items():
        print(f"  [{cod}] {c['nome']}")
        print(f"        Professor: {c['professor']} | Carga: {c['carga_horaria']}h")
        print()
 
    pausar()

def matricular_aluno():
    """Matricula um aluno em um curso."""
    cabecalho("MATRICULAR ALUNO")
 
    if not alunos:
        print("  Nenhum aluno cadastrado.")
        pausar()
        return
 
    if not cursos:
        print("  Nenhum curso cadastrado.")
        pausar()
        return
 
    ra = input("  RA do aluno: ").strip().upper()
 
    if ra not in alunos:
        print("\n  ❌ Aluno não encontrado.")
        pausar()
        return
 
    listar_cursos()
    codigo = input("  Código do curso para matrícula: ").strip().upper()
 
    if codigo not in cursos:
        print("\n  ❌ Curso não encontrado.")
        pausar()
        return
 
    nome_curso = cursos[codigo]['nome']
 
    if nome_curso in alunos[ra]['cursos']:
        print(f"\n  ❌ Aluno já matriculado em {nome_curso}.")
    else:
        alunos[ra]['cursos'].append(nome_curso)
        historico.append(f"{alunos[ra]['nome']} matriculado em {nome_curso}")
        print(f"\n  ✅ {alunos[ra]['nome']} matriculado em {nome_curso}!")
 
    pausar()

# ==================== RELATÓRIOS ====================
 
def relatorio_geral():
    """Exibe relatório geral do sistema."""
    cabecalho("RELATÓRIO GERAL")
 
    print(f"  Sistema: {INFO_SISTEMA[0]} {INFO_SISTEMA[1]}")
    print(f"  Total de alunos: {len(alunos)}")
    print(f"  Total de cursos: {len(cursos)}")
 
    if alunos:
        # LIST COMPREHENSION — alunos aprovados (média >= 6)
        aprovados = [v['nome'] for k, v in alunos.items() if calcular_media(k) >= 6]
        reprovados = [v['nome'] for k, v in alunos.items() if 0 < calcular_media(k) < 6]
        sem_nota   = [v['nome'] for k, v in alunos.items() if calcular_media(k) == 0]
 
        print(f"\n  ✅ Aprovados ({len(aprovados)}):")
        for nome in aprovados:
            print(f"     - {nome}")
 
        print(f"\n  ❌ Reprovados ({len(reprovados)}):")
        for nome in reprovados:
            print(f"     - {nome}")
 
        print(f"\n  ⏳ Sem notas ({len(sem_nota)}):")
        for nome in sem_nota:
            print(f"     - {nome}")
 