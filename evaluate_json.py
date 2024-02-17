# PROGRAMA QUE EVALUA 
#SI UN ARCHIVO ES JSON
with open('json_example.json', 'r') as file:
        content = file.read()

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
            



print(show_content(content))

def set_tokens():
    tokens = {}
    with open('token.txt', 'r') as file:
        for line in file:
            key, value = line.split("\t")
            tokens[key] = value
            return tokens
            
tokens = set_tokens()
print(tokens)