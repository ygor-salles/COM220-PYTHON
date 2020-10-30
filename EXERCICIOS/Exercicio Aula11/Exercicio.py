#definir as nosssa excptions

class UserNameDuplicado(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class IdadeMenorQuePermitida(Exception):
    pass

class EmailInvalido(Exception):
    pass

#classe para conter os dados dos usuários

class User:
    def __init__(self, userName, email):
        self.__userName = userName
        self.__email = email
    
    def getUserName(self):
        return self.__userName
    
    def getEmail(self):
        return self.__email
    
listaExemplo = [
    ("paulo", "paulo@gmail.com", 21),
    ("maria", "maria@gmail.com", 19),
    ("antonio", "antonio@gmail.com", 25),
    ("pedro", "pedro@gmail.com", 15),
    ("marisa", "maria", 23),
    ("ana", "ana@gmail.com", -3),
    ("maria", "maria2@gmail.com", 27),
]

cadastro = {}

for username , email, idade in listaExemplo:
    try:
        if username in cadastro:
            raise UserNameDuplicado()
        if idade < 0:
            raise IdadeInvalida()
        if idade < 18:
            raise IdadeMenorQuePermitida()

        emailPartes = email.split('@')
        if len(emailPartes) != 2 or not emailPartes[0] or not emailPartes[1]:
            raise EmailInvalido()
    
    except UserNameDuplicado:
        print('Username %s já está em uso'%username)
    except IdadeInvalida:
        print('Idade inválida: %d'%idade)
    except IdadeMenorQuePermitida:
        print('Usuário %s tem idade inferior a permitida'%username)
    except EmailInvalido:
        print('%s não é um endereço de e-mail válido'%email)
    
    else:
        cadastro[username] = User(username, email)
        
        