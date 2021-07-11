
class Calculadora:

    def sum(self, valor_a, valor_b):
        return valor_a + valor_b

    def sub(self, valor_a, valor_b):
        return valor_a - valor_b

    def mul(self, valor_a, valor_b):
        return valor_a * valor_b

    def quot(self, valor_a, valor_b):
        return valor_a / valor_b


calculadora = Calculadora()


print(calculadora.sum(10,2))
print(calculadora.sub(5,4))
print(calculadora.mul(7,8))
print(calculadora.quot(100,2))
# print(sum(1,2))
# print(sum(3,4))
# print(sub(10,2))
# print(mul(10,2))
# print(quot(10,2))