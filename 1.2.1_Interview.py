def main():
    print("Hola, bienvenido a un juego de entrevistas que consiste en una serie de preguntas que determinarán tu visión del mundo.")
    user_responses = questions()
    save_to_file(user_responses)

def questions():   
    user_responses = {}
    user_responses['name'] = input("Como te llamas: ")
    user_responses['age'] = int(input("Cuántos años tiene: "))
    if user_responses['age'] >= 18: 
        user_responses['job'] = input("Cuál es tu ocupación: ")
        user_responses['marriage'] = input("Tienes una esposa S or N: ")
        if user_responses['marriage'] == "S":
            user_responses['marriageLength'] = int(input("Cuanto tiempo llevas casada: "))
            print(f"¿Tu esposa todavía te ama después de {user_responses['marriageLength']} años?")
        user_responses['bankAgency'] = input("¿Cómo se llama tu agencia bancaria?: ")
        user_responses['bankPass'] = input("¿Cuál es el nombre de usuario y contraseña de su servicio bancario?: ")
        user_responses['ssid'] = int(input("¿Cuál es tu número de seguro social?: "))
    user_responses['number'] = input("Cuál es tu número de teléfono: ")
    user_responses['favColor'] = input("Cuál es tu color favorito: ")
    user_responses['spammerOpinion'] = input("¿Qué opinas de los estafadores en línea?: ")
    
    return user_responses

def save_to_file(user_responses):
    with open(r'C:\Users\P6\Downloads\user_interview_responses.txt', 'w') as file:
        for key, value in user_responses.items():
            file.write(f"{key}: {str(value)}\n")

main()
