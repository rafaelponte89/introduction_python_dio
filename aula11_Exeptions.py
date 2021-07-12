from datetime import timedelta
lst = [1,2]

try:
    content = open('notas.txt','r')
    division = 10/0
    lst[2]
    h = 1 + timedelta(days=20)


except SyntaxError:
    print('Invalid syntax')
except ZeroDivisionError:
    print('Division by zero not valid')
except ArithmeticError:
    print('Invalid operation arithmetic')
except IndexError:
    print('Index out of range')
except TypeError:
    print('Error of types')
except Exception as ex:
    print('Type error: {}'.format(ex))
except BaseException as ex:
    print('Type error: {}'.format(ex))
else:
    print('Without exceptions!')
finally:
    print('Always execute')
    print('Closing file!')




