# PROGRAMA QUE EVALUA 
#SI UN ARCHIVO ES JSON
with open('json_example.json', 'r') as file:
        content = file.read()

# imprimir el contenido del carchivo caracter por caracter
def show_content(file):
    for character in file:
        print(character)


def is_json(file):
        for character in file:
            if character == '{':
                return True
            

print(show_content(content))
