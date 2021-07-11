from aula7_television import Television
from aula7_calculator1 import Calculadora
from aula8_contador_letras import letter_counter

if __name__ == '__main__':
    television = Television();
    print(television.on)
    television.power()
    print(television.on)
    calculadora = Calculadora(5,10)
    print(calculadora.sum())
    animal = ['fish','cat','lion']
    print('Letters Counter : {}'.format(letter_counter(animal)))