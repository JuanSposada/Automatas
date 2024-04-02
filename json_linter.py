#!/usr/bin/env python3
#
# --Json Linter--
# Juan Sebastian Moreno Posada
# al22760047.AT.ite.DOT.edu.DOT.mx
# Apr/1/2024
#
#

tokens_array = []
tokens_string =[]

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
        # condicion para agrupar el string
        tokens_list[character] = value
        tokens_array.append(value)
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

# Esta funcion escribe en un archivo salida.txt los tokens y caracteres
def write_document(file, tokens):
    with open('salida.txt', 'w') as output:
        for character in file:
            if character == chr(10):
                output.write(f'{tokens[character]}=[ENTER]\n')
            elif character == chr(32):
                output.write(f'{tokens[character]}=[SPACE]\n')
            else:
                output.write(f'{tokens[character]}={character}\n')
        return output
        
# Comprueba que el archivo es json        
def is_json(array):
        if array[0] == 123:
            True
        else:
            print('no es archivo json')
            exit()

# tokeniza los elementos string
def tokenize_string(array):
    tokens= []
    agrupados = False
    for value in array:
        if (value >= 65 and value<= 90) or (value >= 97 and value <=122):
            if not agrupados:
                tokens.append(200)
                agrupados = True
        else:
            agrupados = False
            tokens.append(value)
    return tokens

# tokeniza los elementos int
def tokenize_int(array):
    tokens = []
    agrupados = False
    for value in array:
        if (value >= 48 and value <= 57):
            if not agrupados:
                tokens.append(201)
                agrupados = True
        else: 
            agrupados = False
            tokens.append(value)
    return tokens


# comprueba que ls string esten cerrados con comilla
def is_string(array):
    flag = True 
    for value in array:
        if value == 34:
            flag = not flag
            print(flag)
    if flag == False:
        print("ERROR: las comillas no se cerraron")
        exit();




# Definicion de la funcion main
def main():
    file = read_file('json_example.json')
    tokens = tokenize_content(file)
    is_json(tokens_array)
    print(tokens_array)
    tokenize_string(tokens_array)
    show_content_tokens(file, tokens)
    write_document(file, tokens)
    print(tokens_array)
    print(is_string(tokens_array))
    group_string = tokenize_string(tokens_array)
    print(group_string)
    group_int = tokenize_int(group_string)
    print(group_int)



if __name__ == '__main__':
    main()