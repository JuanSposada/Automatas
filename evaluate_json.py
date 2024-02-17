# PROGRAMA QUE EVALUA 
#SI UN ARCHIVO ES JSON

def read_file():
    with open('json_example.json', 'r') as file:
            content = file.read()
            return content

# imprimir el contenido del carchivo caracter por caracter
def show_content(file):
    for character in file:
        if character == chr(10):
            print('[Enter]')
        elif character == '\t':
            print('[Tab]')
        elif character == chr(32):
            print('[Espacio]')
        else:
            print(character)
        

# funcion que evalua si es un archivo json, si lo es devuelve true
def is_json(file):
        for character in file:
            if character == '{':
                return True
            



#asigna la lista de tokens externa a un diccionario
def set_tokens():
    tokens = {}
    with open('token.txt', 'r') as file:
        content = file.readlines()
        
        for line in content:
            value,  key = line.strip().split("=")
            key = key.replace('\\n', '\n')
            key = key.replace(' ', '[ESPACIO]')
            key = key.replace('\\t', '\t')
            tokens[key] = value
        return tokens

# Si existe obtiene los tokens del diccionario para mostrarlos
def get_tokens(tokens, file):
    for character in file:
        if character in tokens:
            print(tokens[character])
        else: 
            print(f'no se encontro token de {character}')

#imprime los tokens en le diccionario
def print_tokens(tokens):
    for key, value in tokens.items():
        print(f'{key} = {value}')

# funcion principal
def main():
    file = read_file()
    print(show_content(file))
    tokens = set_tokens()
    print_tokens(tokens)
    get_tokens(tokens, file)
    print(tokens['\t'])




main()