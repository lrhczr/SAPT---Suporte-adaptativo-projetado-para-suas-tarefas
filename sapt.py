#acolhimento
nome = input("Olá usuário, seja bem vindo ao SAPT, seu assistente de suporte adaptato pessoalmente para suas tarefas diárias!. Para começarmos o seu acolhimento, por gentileza nos informe seu nome: ")
print(f"Olá {nome}, é um prazer te conhecer! Estou aqui para te ajudar com suas tarefas diárias. Se precisar de algo, é só me chamar!")

#tarefas pré defininas
tarefas_diarias = ["Beber 2 litros de água",
                   "Ler",
                   "Meditação",
                   "Responder e-mails",
                   "Trabalhar/Estudar",
                   "Ir dormir na hora certa"]
minha_lista = []
lista_completa = tarefas_diarias + minha_lista

#código
while True:
  print("\n" + "="*30)
  try:
    tarefas = int(input("O que você gostaria de fazer hoje?:\n"
                            "1 - Ver minhas tarefas\n"
                            "2 - Adicionar nova tarefa\n"
                            "3 - Remover tarefa\n"
                            "4 - Sair\n"
                            ": "))
  except ValueError:
        print("Por favor, digite um número válido (1-4).")
        continue
  match tarefas:
    case 1:
      print("\n--- Tarefas Diárias ---")
      for i, t in enumerate(lista_completa, 1):
        print(f"{i} - {t}")
    case 2:
      resposta = input("Você deseja adiconar algo a sua lista de afazeres? Sim/Não: ").lower()
      if resposta == "sim":
        nova_tarefa = input("O que você gostaria de adicionar?: ")
        lista_completa.append(nova_tarefa)
        print(f"'{nova_tarefa}' adicionado com sucesso!")
        print("A sua lista de afazeres atualizada é:", lista_completa)
      else:
        print("Entendido!")
    case 3:
      print("\n--- Remover Tarefa ---")
      if not lista_completa:
        print("Lista vazia, nada para remover.")
      else:
        for i, t in enumerate(lista_completa, 1):
          print(f"{i} - {t}")
        try:
          remover = int(input("Digite o número da tarefa que deseja remover: "))
          tarefa_removida = lista_completa.pop(remover - 1)
          print(f"'{tarefa_removida}' removida com sucesso!")
        except (ValueError, IndexError):
          print("Número inválido. Tente novamente.")
    case 4:
      print("SAPT agradece a preferencia, volte sempre!")
      break
    case _:
      print("Opção inválida!")
