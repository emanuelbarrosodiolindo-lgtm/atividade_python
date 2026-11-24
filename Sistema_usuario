  logado = False
  usuario_logado = ""
  usuarios = []
  
  while True:
      print("\033c", end="")
      print("SISTEMA DE USUÁRIOS\n")
  
      if not logado:
          print("=== LOGIN ===")
          login = input("Digite seu login: ")
          senha = input("Digite sua senha: ")
  
          if login == "usuario1" and senha == "12345":
              print("\nLogin realizado com sucesso!")
              usuario_logado = login
              logado = True
              input("ENTER para continuar...")
          else:
              input("\nLogin ou senha incorretos! ENTER para tentar novamente.")
  
      else:
          print("=== MENU PRINCIPAL ===")
          print("Usuário logado:", usuario_logado)
          print("1 - Inserir usuário")
          print("2 - Pesquisar usuário")
          print("3 - Remover usuário")
          print("4 - Listar todos os usuários")
  
          opcao = input("\nEscolha uma opção: ")
  
          if opcao == "1":
              nome = input("\nDigite o nome do usuário: ")
  
              if nome in usuarios:
                  print("Usuário já cadastrado!")
              else:
                  usuarios.append(nome)
                  print("Usuário cadastrado com sucesso!")
  
              input("\nENTER para continuar...")
  
          elif opcao == "2":
              nome = input("\nDigite o nome que deseja pesquisar: ")
  
              if nome in usuarios:
                  print("Usuário encontrado!")
              else:
                  print("Usuário não encontrado!")
  
              input("\nENTER para continuar...")
  
          elif opcao == "3":
              nome = input("\nDigite o nome que deseja remover: ")
  
              if nome in usuarios:
                  usuarios.remove(nome)
                  print("Usuário removido com sucesso!")
              else:
                  print("Usuário não encontrado!")
  
              input("\nENTER para continuar...")
  
          elif opcao == "4":
              print("\n=== LISTA DE USUÁRIOS ===")
  
              if len(usuarios) == 0:
                  print("Nenhum usuário cadastrado.")
              else:
                  for nome in usuarios:
                      print("-", nome)
  
              input("\nENTER para continuar...")
  
          else:
              input("\nOpção inválida! ENTER para continuar...")
