**SAPT — Suporte Adaptativo Projetado para suas Tarefas**

**Descrição**

O SAPT é um assistente pessoal de linha de comando desenvolvido em Python. Ele acolhe o usuário pelo nome e oferece um menu interativo para gerenciar uma lista de tarefas diárias, combinando tarefas pré-definidas com tarefas personalizadas adicionadas pelo próprio usuário.

**Funcionalidades**

Acolhimento personalizado — solicita o nome do usuário e exibe uma saudação.
Visualizar tarefas — exibe todas as tarefas diárias (pré-definidas + adicionadas).
Adicionar tarefa — permite incluir novas tarefas à lista.
Remover tarefa — permite excluir qualquer tarefa da lista pelo número.
Sair — encerra o programa com uma mensagem de despedida.

**Fluxograma**

Início
  └─> Acolhimento (solicita nome)
        └─> Loop principal
              ├─> 1: Ver tarefas
              ├─> 2: Adicionar tarefa
              ├─> 3: Remover tarefa
              ├─> 4: Sair ──> Fim
              └─> Entrada inválida: solicita novo número

**Descrição do fluxo:**

ElementoDescriçãoInícioInício do programaEntrada de dadosNome do usuário e escolha do menu (1–4)ProcessamentoEstruturas while True, try/except e match/caseSaídaResposta correspondente a cada opção selecionadaFimOpção 4 encerra o loop com break

**Tarefas Pré-definidas**

Ao iniciar, o SAPT já carrega as seguintes tarefas na lista:

Beber 2 litros de água
Ler
Meditação
Responder e-mails
Trabalhar/Estudar
Ir dormir na hora certa


**Como executar**

Pré-requisito: Python 3.10 ou superior (necessário para match/case).
bashpython assistente_pessoal.py
Ao iniciar, o programa solicitará seu nome e apresentará o menu de opções.

**Exemplo de uso**

Olá usuário, seja bem vindo ao SAPT...
Para começarmos o seu acolhimento, por gentileza nos informe seu nome: Maria
Olá Maria, é um prazer te conhecer! Estou aqui para te ajudar com suas tarefas diárias.

==============================
O que você gostaria de fazer hoje?:
1 - Ver minhas tarefas
2 - Adicionar nova tarefa
3 - Remover tarefa
4 - Sair
: 1

--- Tarefas Diárias ---
1 - Beber 2 litros de água
2 - Ler
3 - Meditação
4 - Responder e-mails
5 - Trabalhar/Estudar
6 - Ir dormir na hora certa

**Estrutura do Código**

assistente_pessoal.ipynb
├── Acolhimento (input de nome + saudação)
├── Listas de tarefas (pré-definidas + personalizadas)
└── Loop principal
    ├── Exibição do menu
    ├── Tratamento de erros (try/except + ValueError)
    └── match/case para cada opção (1, 2, 3, 4, _)

**Tecnologias utilizadas**

Python 3.10+
Jupyter Notebook (.ipynb)
Estruturas nativas: input, print, list, while, try/except, match/case
