from packages.modules import *

def main():
    while True:
        entry = input('@pastel> ').strip()
        command = Parser.parse(entry)
        ErrUtils.ePrint('a', 1020102010)

        if command['name'] == 'exit':
            break
        elif command['name'].strip() == '':
            continue
        else:
            try:
                module_name = f"commands.{command['name']}"
                
                if not os.path.exists(os.path.join('commands', f"{command['name']}.py")):
                    ErrUtils.ePrint(command['name'], 0x000100)
                    continue

                spec = importlib.util.spec_from_file_location(module_name, os.path.join('commands', f"{command['name']}.py"))
                module = importlib.util.module_from_spec(spec)
                
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
                
                if hasattr(module, 'default'):
                    module.default(command['args']) 
                else:
                    ErrUtils.ePrint(command['name'], 0x000400)

            except Exception as e:
                ErrUtils.ePrint(command['name'], 0x000800, e)

if __name__ == '__main__':
    main()