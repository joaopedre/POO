class Time:
    def __init__(self, nome, estado, Jogadores):
          self.__nome = nome
          self.__estado = estado
          self.__Jogadores = []
          if nome or estado=="": raise ValueError("informe o nome dos jogadores")
    def inserir(self, j):
         self.__Jogadores.append(j)
    def listar(self):
         return self.__Jogadores[:]
    def __str__(self):
         return f"Time {self.__nome} do estado {self.__estado} tem len({self.__Jogadores}) jogadores."
    
class Jogador:
     def __init__(self):
          self.__nome = ""
          self.__camisa = 0
          self.__gols = 0
    def set_nome(self, nome):
        if self.__nome != "": self.__nome = nome
        else: raise ValueError("Preencha o nome")
    def set_camisa(self,camisa):
        if self.__camisa != "": self.__camisa = camisa
        else: raise ValueError("Diga a camisa macho")
    def set_gols(self, gols):
        if self.__gols != 0: self.__gols = gols
        else: raise ValueError("Bixo ruim da peste")
    def get_nome(self): 
        return self.__nome
    def get_camisa(self): 
        return self.__camisa
    def get_gols(self): 
        return self.__gols
    def __str__(self):
        return f"Jogador {self.__nome} do número {self.__camisa} marcados {self.__gols} de gols."

class UI
    @staticmethod
    def menu():
          print("Bem Vindo ao Seleção de Times do FIFA 4090 rtx melhorado 1000000000%")
          op = 4
          while op != 5:
                op = UI.menu()
