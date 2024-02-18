# PROGRAMA QUE EVALUA 
#SI UN ARCHIVO ES JSON

tokens_list= {}


# Esta funcion lee un archivo y devuelve su contenido
def read_file(file_to_read):
    with open(file_to_read, 'r') as file:
            content = file.read()
            return content
    
# Esta funcion tokeniza los caracteres del archivo   
def tokenize_content(file):
    for character in file:
        value = ord(character)
        tokens_list[character] = value
    return tokens_list
        

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

# imprime el contenido del archivo y su token
def show_content_tokens(file,tokens):
    for character in file:
        print(f'{character} = {tokens[character]}')

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
    file = read_file('json_example.json')
    show_content(file)
    tokens = tokenize_content(file)
    show_content_tokens(file, tokens)

    





main()