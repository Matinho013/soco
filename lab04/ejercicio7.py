def computegrade(score):
    if (score >= 0.9 and score <= 1.0):
        grade = "A"
    elif (score >= 0.8 and score < 0.9):
        grade = "B"
    elif (score >= 0.7 and score < 0.8):
        grade = "C"
    elif (score >= 0.6 and score < 0.7):
        grade = "D"
    elif (score >= 0 and score < 0.6):
        grade = "f"
    else:
        grade = "Score no es válida"
    return grade

try: 
    score = float(input("Ingrese la calificación (0.01 - 1.00): "))
    grade = computegrade(score)
    print("Su calificación es: ", grade)
except:
    print("Error, debe ingresar un valor numérico")
