from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
#inicio contadores
cant_correctos = 0
cant_incorrectos = 0
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = int(input("resultado: "))
    #verifico el operador para realizar la cuenta
    match operator:
        case "+":
           result_computer = number_1 + number_2
        case "-":
            result_computer = number_1 - number_2
        case "*":
            result_computer = number_1 * number_2
        case "/":
            result_computer = number_1 / number_2
     
    print(result_computer == result)
    if(result_computer == result):
        cant_correctos += 1
    else:
        cant_incorrectos += 1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos. Cantidad de aciertos: {cant_correctos} , cantidad de incorrectos: {cant_incorrectos}")