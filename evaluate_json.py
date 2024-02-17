# PROGRAMA QUE EVALUA 
#SI UN ARCHIVO ES JSON

def read_file():
    with open('json_example.json', 'r') as file:
            content = file.read()
            return content

# imprimir el contenido del carchivo caracter por caracter
def show_content(file):
    for character in file:
        if character =='\n':
            print('[Enter]')
        elif character == '\t':
            print('[Tab]')
        elif character == ' ':
            print('[Espacio]')
        else:
            print(character)
        


def is_json(file):
        for character in file:
            if character == '{':
                return True
            




def set_tokens():
    tokens = {}
    with open('token.txt', 'r') as file:
        content = file.readlines()
        
        for line in content:
            value,  key = line.strip().split("=")
            tokens[key] = value
        return tokens
            
def get_tokens(tokens, file):
    for character in file:
        if character in tokens:
            print(tokens[character])
        else: 
            print(f'no se encontro token de {character}')

file = read_file()
print(show_content(file))
tokens = set_tokens()
print(tokens)
get_tokens(tokens, file)