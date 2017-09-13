import json

def main(args=[]):
    try:


        f = open("Contatos.txt", encoding="utf8")
        jsonObj = json.loads(f.read())
        print(jsonObj)

    except FileNotFoundError:
        print("Ops! Arquivo não encontrado")

if __name__ == '__main__':
    main()
