import utils.parser as Parser

def main():
    while True:
        command = input('@pastel> ')
        cmdProperties = Parser.parse(command)
        print(cmdProperties)
        
        if cmdProperties['name'] == 'hello':
            print("Hello World!")
        elif cmdProperties['name'] == 'exit':
            break

if __name__ == '__main__':
    main()