# Este programa lee los caracteres de un archivo json
# Despues les asigna un token unicode
# Por ultimo imprime los valores de caracter y token
# Ademas crea un archivo .txt con dichos valores


# Esta funcion lee un archivo y devuelve su contenido
def read_file(file_to_read):
    with open(file_to_read, 'r') as file:
            content = file.read()
            return content
    
# Esta funcion tokeniza los caracteres del archivo   
def tokenize_content(file):
    tokens_list= {}
    for character in file:
        value = ord(character)
        tokens_list[character] = value
    return tokens_list


# imprime el contenido del archivo y su token
def show_content_tokens(file,tokens):
    for character in file:
        if character == chr(10):
            print(f'{tokens[character]}=[Enter]')
        elif character == chr(32):
            print(f'{tokens[character]}=[SPACE]')
        else:
            print(f'{tokens[character]}={character}')

def write_document(file, tokens):
    with open('salida.txt', 'w') as output:
        for character in file:
            output.write(f'{tokens[character]}={character}\n')
        return output
        
        


def main():
    file = read_file('json_example.json')
    tokens = tokenize_content(file)
    show_content_tokens(file, tokens)
    write_document(file, tokens)

main()