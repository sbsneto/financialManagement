from menus import cabecalho, menu_secundario, menu_principal, consultas
from workoutClass import Workout
from tratarErros import leia_int, leia_str
from exercicioClass import Exercicio
import time
import os

exercicios = []
workouts = []


def cadastrarWorkout(nomeTreino, exercicioAtual: Exercicio):
    workoutAtual = Workout(nomeTreino)
    workoutAtual.setTreino(exercicioAtual)

    if(len(workouts) == 0):
        print(len(workouts))
        print(workoutAtual)
        workouts.append(workoutAtual)
        print(len(workouts))
        exercicio1 = workoutAtual.getExercicios()
        exercicio1[0].getName()
    else:
        for i in range(len(workouts)):
            workoutExist = ''
            if(workoutExist != nomeTreino):
                workouts.setNomeTreino(nomeTreino)
                for c in range(len(workouts.getExercicios())):
                    exercicios = Exercicio([workouts.getExercicios()])
                    if(exercicios[c].getName() != exercicio.getName()):
                        print(
                            'Exercicio já cadastrado favor inserir um treino diferente!')
                    else:
                        workouts[i].append()
                        print('Exercicio cadastrado com sucesso!')
            else:
                for c in range(len(workouts[i].getExercicios())):
                    exercicios = Exercicio([workouts[i].getExercicios()])
                    if(exercicios.getName[c] == exercicio.getName()):
                        print(
                            'Exercicio já cadastrado favor inserir um treino diferente!')
                    else:
                        workouts.setExercicios[i](exercicio)


while True:
    cabecalho()
    menu_principal()
    op = leia_int('Escolha a opção desejada: ')
    os.system("cls")
    if op == 1:
        while True:
            cabecalho()
            menu_secundario()
            op2 = leia_int('Escolha a opção desejada: ')
            if (op2 == 1):
                os.system("cls")
                nameGrupoMuscular = ''
                exercicio = Exercicio
                cabecalho()
                nameGrupoMuscular = leia_str(
                    'Insira o grupo Muscular: ')
                nameGrupoMuscular.upper
                nomeExercicio = leia_str(
                    'Insira o nome do Exercicio: '
                )
                repeticoes = leia_str(
                    'Insira o número de repetições ou o tempo de duração: '
                )
                peso = leia_str(
                    'Insira o peso: '
                )
                exercicio(nomeExercicio.upper(),
                          repeticoes.upper(), peso.upper())
                cadastrarWorkout(nameGrupoMuscular.upper(), exercicio)
            elif (op2 == 2):
                break
            else:
                print("ERRO! Opção invalida ! ")
    elif op == 2:
        print('Opção 2 selecionada')
    elif op == 3:
        print('Opção 3 selecionada')
    elif op == 4:
        print('Opção 3 selecionada')
    elif op == 5:
        break
