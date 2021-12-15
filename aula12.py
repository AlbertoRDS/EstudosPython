import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://www.facebook.com/login.php?skip_api_login=1&api_key=341066977483941&kid_directed_site=0&app_id=341066977483941&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fredirect_uri%3Dhttps%253A%252F%252Fvtexid.vtex.com.br%252FVtexIdAuthSiteKnockout%252FReceiveAuthorizationCode.ashx%26scope%3Demail%26client_id%3D341066977483941%26state%3DeyJhbGciOiJFUzI1NiIsImtpZCI6IjNGNzg2NUMyNjMyM0Y2OTZCQTE0Q0U0RTI4QzU0Q0RBMjU3RTY5OTUiLCJ0eXAiOiJqd3QifQ.eyJzdWIiOiJCNUJFQzFBQUFENzk5ODg3RTY0OEI2RDgyNTQwMTY4RjlCNEQxRDQzOTNDNTQ5ODY0OEExNDg4RTM5NDVEODYzIiwiaXNzIjoidG9rZW4tZW1pdHRlciIsImV4cCI6MTYzOTQyNzc0NiwicHJvdmlkZXIiOiJGYWNlYm9vayIsImVycm9yVXJsIjoiaHR0cHM6Ly93d3cudXNlcmVzZXJ2YS5jb20vYXBpL3Z0ZXhpZC9vYXV0aC9lcnJvciIsImlhdCI6MTYzOTQyNzE0NiwianRpIjoiODUzMmU2MjAtMjAyNi00NDAzLThiNjctNTcyNmI4OWRlOWI3In0.dWT4ICG_9rOs1XYUJeOXCPoZDDDkI3Gvb3uh5cUuXhRoG8VfRzAWETbraRxMRHboyP4O4Kb5U9uBywInxCWsqQ%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df3f44afa-7c0e-4e24-a855-f7df41969db6%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fvtexid.vtex.com.br%2FVtexIdAuthSiteKnockout%2FReceiveAuthorizationCode.ashx%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJhbGciOiJFUzI1NiIsImtpZCI6IjNGNzg2NUMyNjMyM0Y2OTZCQTE0Q0U0RTI4QzU0Q0RBMjU3RTY5OTUiLCJ0eXAiOiJqd3QifQ.eyJzdWIiOiJCNUJFQzFBQUFENzk5ODg3RTY0OEI2RDgyNTQwMTY4RjlCNEQxRDQzOTNDNTQ5ODY0OEExNDg4RTM5NDVEODYzIiwiaXNzIjoidG9rZW4tZW1pdHRlciIsImV4cCI6MTYzOTQyNzc0NiwicHJvdmlkZXIiOiJGYWNlYm9vayIsImVycm9yVXJsIjoiaHR0cHM6Ly93d3cudXNlcmVzZXJ2YS5jb20vYXBpL3Z0ZXhpZC9vYXV0aC9lcnJvciIsImlhdCI6MTYzOTQyNzE0NiwianRpIjoiODUzMmU2MjAtMjAyNi00NDAzLThiNjctNTcyNmI4OWRlOWI3In0.dWT4ICG_9rOs1XYUJeOXCPoZDDDkI3Gvb3uh5cUuXhRoG8VfRzAWETbraRxMRHboyP4O4Kb5U9uBywInxCWsqQ%23_%3D_&display=page&locale=pt_BR&pl_dbl=0')
    print(response)
    #retorna_dados_cep('08142760')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny'])

