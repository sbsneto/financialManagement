# cls é somente Windows, clear para macOS, Linux, BSDs etc.

def limpa():
    import os
    if 'win32' in os.sys.platform:
        os.system('cls')
    else:
        os.system('clear')