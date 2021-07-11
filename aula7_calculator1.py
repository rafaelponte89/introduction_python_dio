
class Calculadora:
    def __init__(self,num1,num2):
        self.valor_a = num1
        self.valor_b = num2

    def sum(self):
        return self.valor_a + self.valor_b

    def sub(self):
        return self.valor_a - self.valor_b

    def mul(self):
        return self.valor_a * self.valor_b

    def quot(self):
        return self.valor_a / self.valor_b


calculadora = Calculadora(10,2)

print(calculadora.valor_a)
print(calculadora.sum())
print(calculadora.sub())
print(calculadora.mul())
print(calculadora.quot())
# print(sum(1,2))
# print(sum(3,4))
# print(sub(10,2))
# print(mul(10,2))
# print(quot(10,2))