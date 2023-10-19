from PIL import Image, ImageDraw, ImageFont
import secrets, string

def get_special_chars(chars):
    tmp = ""
    for char in chars:
        if char == "`":
            continue
        elif char == "@":
            continue
        elif char in "{":
            continue
        elif char in "}":
            continue
        elif char in "^":
            continue
        elif char in "[":
            continue
        elif char in "]":
            continue
        elif char in "(":
            continue
        elif char in ")":
            continue
        elif char in "'":
            continue
        elif char in '"':
            continue
        elif char in '~':
            continue
        elif char in '|':
            continue
        else:
            tmp += char
    
    return tmp

def get_pwd(letters, digits, special_chars, pwd_len):
    pwd = ""
    alphabet = letters + digits + special_chars
    for i in range(pwd_len):
        pwd += ''.join(secrets.choice(alphabet))
    
    return pwd

def get_menu():
    print('''Seleccionar una opción:
         1. Generar password
         2. Salir''')

def underline(text):
    txt = "\u0332".join(text)
    return txt
    
def create_file(name, gree, pwd_length, username, pwd, usr, pss, system):
    f = open("/mnt/c/Users/dsaldivar/Documents/14_python/"+name, "+w")
    list1 = [gree+",", 
             f"\nPor este medio envió las credenciales de acceso a SIPAP {system}",
             "\nTener en cuenta las siguientes políticas de seguridad al cambiar la contraseña:",
             "\n- No debe ser una palabra que pueda estar en algún diccionario, ni relacionado al Nombre del usuario o entidad.",
             "\n- No debe ser correlativo al anterior, ni similar a las ultimas 10 contraseñas.",
             f"\n- Debe contener por lo menos una mayúscula, una minúscula, un número y un carácter especial y de longitud mínima de {pwd_length} caracteres.",
             "\n- Vigencia mínima de contraseña, de 1(un) día. Un solo cambio por día es posible.",
             "\n- Escriba su contraseña en un bloc de notas para luego copiar y pegar en el sistema.",
             "\nCredenciales:",
             "\n",
             f"\n{underline(usr)}",
             f"\n{username}",
             f"\n{underline(pss)}",
             f"\n{pwd}",
             "\n",
             "\nFavor dar acuse.",
             "\nGracias.",
             "\nSaludos cordiales."
             ]
    for i in list1:
        f.write(i)
    
    f.close()

if __name__ == '__main__':
    letters = string.ascii_letters
    digits = string.digits
    chars = string.punctuation
    special_chars = get_special_chars(chars)
    get_menu()

    while True:
        options = input("Options: ")
        if options =="1":
            name = input("Input name image: ")
            username = input("Username: ")
            system = input("System: ")
            pwd_length = int(input("Length: "))
            greetings = input("Greetings: ")
            
            img = Image.open("/mnt/c/Users/dsaldivar/Documents/14_python/bg.png")
            imgname = "/mnt/c/Users/dsaldivar/Documents/14_python/"+name+".png"
            I1 = ImageDraw.Draw(img)
            pwd = get_pwd(letters, digits, special_chars, pwd_length)


            usr = "Usuario:"
            pss = "Contraseña:"

            text = f'''
            {greetings},
            Por este medio envió las credenciales de acceso a SIPAP {system},
            Tener en cuenta las siguientes políticas de seguridad al cambiar la contraseña:
            - No debe ser una palabra que pueda estar en algún diccionario, ni relacionado al Nombre del usuario o entidad.
            - No debe ser correlativo al anterior, ni similar a las ultimas 10 contraseñas.
            - Debe contener por lo menos una mayúscula, una minúscula, un número y un carácter especial y de longitud mínima de {pwd_length} caracteres.
            - Vigencia mínima de contraseña, de 1(un) día. Un solo cambio por día es posible.
            - Escriba su contraseña en un bloc de notas para luego copiar y pegar en el sistema.

            {underline(usr)}
            {username}
            {underline(pss)} 
            {pwd}
            
            Favor dar acuse.
            Gracias.
            Saludos cordiales, '''

            filename = name+".txt"
            create_file(filename, greetings, pwd_length, username, pwd, usr, pss, system)

            myFont = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 18)

            I1.text((10,10), text, font=myFont, fill=(0,0,0))
            img.show()
            img.save(imgname)
            print(pwd)
            
        if options == "2":
            break
            

