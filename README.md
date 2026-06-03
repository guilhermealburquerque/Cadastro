# Cadastro
# 🏫 EduTrack — Sistema de Gerenciamento Escolar

## 👥 Integrantes da Dupla
* **Ana Vitória Boa Hora Santos** — Turma: CCo(UNIT)
* **Guilherme Borges de Albuquerque Maranhão** — Turma: CCo (UNIT)

## 📌 Tema Escolhido
**Tema:** EduTrack
Um sistema completo de gerenciamento escolar desenvolvido em Python para o controle de fluxos de alunos, cursos, matrículas, lançamentos de notas e relatórios de desempenho em tempo real.

---

## 📄 Descrição do Sistema

### Objetivo
O **EduTrack** foi criado com o objetivo de centralizar as principais rotinas administrativas de uma instituição de ensino. O sistema opera de forma interativa via terminal, utilizando estruturas de dados robustas na memória para simular um ambiente real de backend escolar. Ele foi projetado para ser seguro contra falhas humanas (entradas inválidas) e modular para facilitar futuras expansões.

### Funcionalidades Principais
* **Gerenciamento de Alunos:** Cadastro de dados (RA único, nome, idade e turno), listagem ordenada e consulta detalhada por aluno.
* **Gerenciamento de Cursos:** Cadastro de disciplinas (código único, nome, professor e carga horária) e controle de turmas.
* **Sistema de Matrículas:** Vinculação dinâmica de alunos em múltiplos cursos sem duplicidade.
* **Controle de Notas:** Lançamento de avaliações com classificação automática de desempenho e recálculo imediato da média geral.
* **Relatório Geral:** Painel analítico que exibe o total de alunos e cursos, além de listar os estudantes nas situações de *Aprovado*, *Reprovado* ou *Em Andamento*.
* **Histórico de Atividades:** Registro cronológico (Log de eventos) de todas as principais ações realizadas no sistema.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 
* **Ambiente de Desenvolvimento (IDE):** VS Code
* **Versionamento:** Git e GitHub

### Conteúdos de Python Aplicados (Requisitos da Rubrica)
* **Estruturas Condicionais:** Uso extensivo de `if`, `elif`, `else` para controle de menus e validações de chaves.
* **Operador Ternário:** Aplicado para a classificação dinâmica da situação de aprovação do aluno em uma linha de código.
* **Estruturas de Repetição:** Laços `while` estruturando os menus contínuos e laços `for` realizando varreduras de dados.
* **Tratamento de Exceções:** Blocos `try/except` protegendo o sistema contra falhas de digitação (`ValueError` e `IndexError`).
* **Coleções (Collections):**
  * **Dicionários (`dict`):** Representação das entidades complexas de Alunos e Cursos.
  * **Tuplas (`tuple`):** Dados imutáveis do sistema, como turnos disponíveis e informações da versão.
  * **Conjuntos (`set`):** Utilizados para garantir a unicidade de RAs, códigos de disciplinas e turnos ativos, evitando duplicidades.
  * **Listas (`list`):** Armazenamento de históricos de ações e arrays internos de notas e disciplinas.
* **List Comprehension:** Utilizada para filtrar de forma rápida e elegante as listas de alunos aprovados e reprovados no painel de relatórios.
* **Funções Avançadas:** Código modularizado em mais de 10 funções, contendo uso de parâmetros, retornos de dados e uma expressão **Lambda** para classificar as notas (`Excelente`, `Bom`, `Regular`, `Insuficiente`).

---