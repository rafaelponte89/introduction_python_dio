from colors import Colors

color = Colors()

class Error(Exception):
    pass
class InputError(Error):
    def __init__(self,message):
        self.message = message

while True:
    try:
        print(color.colorIO('='*25,'blue'))
        input_value = int(input(color.colorIO('Enter a school grade: ','yellow')))
        if input_value > 10:
            raise  InputError('The school grade must be less than 10!')
        elif input_value < 0:
            raise InputError('School grade cannot be less than zero')
        break
    except ValueError:
        print(color.colorIO('Invalid school grade!','RED'))
    except InputError as ex:
        print(ex)
