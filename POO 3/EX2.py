class círculo:
    def __init__(self):
        self.__raio = 0
    def set_raio(self, v):
        if self.__raio > 0: self.__raio == v
        else: raise ValueError("o valor não pode ser negativooo!!")
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        return 3.14 * self.__raio ** 2
    def calc_circunferencia(self):
        return 2 * 3.14 * self.__raio
c = círculo()
class UI:
    @staticmethod
    def main():
        c.set_raio(float(input("Digite o raio: "))
        print(c.calc_area() , c.calc_circunferencia())

UI.main()