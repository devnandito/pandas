import os, re, csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_menu():
    print('''Seleccionar una opción:
         1. Procesar csv
         2. Salir''')

if __name__ == '__main__':
    get_menu()
    while True:
        options = input("Options: ")
        if options == "1":
            file_open = os.path.join(BASE_DIR, '20231018_email_res.csv')
            handle = open(file_open)
            array = []
            for line in handle:
                emailsearch = '([a-z]+-*[a-z]*@bcp\.gov\.py)'
                # emailsearch = '([a-z]+@bcp\.gov\.py)'
                stuff = re.findall(emailsearch, line)
                for x in stuff:
                    array.append(x)
            # for i in array:
            #     print("Original: ",i)
            res = []
            [res.append(x) for x in array if x not in res]
            res = [x for x in res if x not in 'dcs-bcp@bcp.gov.py']
            res = [x for x in res if x not in 'dcs@bcp.gov.py']
            res = [x for x in res if x not in 'info@bcp.gov.py']
            res = [x for x in res if x not in 'informes@bcp.gov.py']
            res = [x for x in res if x not in 'py@bcp.gov.py']
            res = [x for x in res if x not in 'sau@bcp.gov.py']
            # for item in res:
            #     print("Sin duplicados: ", item)
            file = os.path.join(BASE_DIR, '20231018_email_resp.csv')
            with open(file, 'w+') as f:
                writer = csv.writer(f)
                # writer.writerow(('email',))
                for i in res:
                    writer.writerow((i,))

        if options == "2":
            break