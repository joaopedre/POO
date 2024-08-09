from datetime import datetime

class paciente:
    def __init__(self, nome, cpf, telefone, nasc):
        if nome =="": raise ValueError("Informe um nome")
        if nasc > datetime.now(): raise ValueError("Informe uma data")
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nasc
    def idade(self):
        hoje = datetime.now()
        tempo = hoje - self.__nascimento
        dias = tempo.days
        anos = dias // 365
        resto = dias % 365
        meses = resto // 30
        return f"{anos} ano(s), {meses} mes(es)"
    
        
    