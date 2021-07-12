import requests
import colors
color = colors.Colors()

def return_data_pc(postal_code):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(postal_code))
    print(color.colorIO(response.json(),'RED'))
    postal_code = response.json()
    print(color.colorIO(postal_code['localidade'],'yellow'))
    print(color.colorIO(postal_code['uf'],'yellow'))
    return postal_code

def info_poke(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    data_pokemon = response.json()
    return data_pokemon
def return_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # return_data_pc('14620000')
    # data_pokemon = info_poke('pikachu')
    # print(data_pokemon['sprites']['front_shiny'])
    print(return_response('https://www.infomoney.com.br/'))