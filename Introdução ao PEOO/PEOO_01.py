class Aluno:    
    def __init__(self):    #construtor
        self.matrícula = ''
        self.nome = ''
    def ano_ingresso(self): # método
        return int(self.matrícula[0:4])
a = Aluno()
a.nome = "Rafela"
a.matrícula = "20231011110987"
b = Aluno()
b.nome = "João"
b.matrícula ="20241011110678"

print(a.nome, a.matrícula, a.ano_ingresso())
print(b.nome, b.matrícula, b.ano_ingresso())