# Este programa muestra los characteres encontrados en un archivo json

def read_file(file_to_read):
    with open(file_to_read, 'r') as file:
            content = file.read()
            return content
    
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

def main():
    file = read_file('json_example.json')
    show_content(file)

if __name__ == '__main__':
    main()