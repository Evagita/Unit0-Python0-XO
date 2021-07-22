#!/usr/bin/env python
# coding: utf-8

# In[8]:


# функция для определения - чей ход
def player_turn(turn):
    if turn % 2 == 0:
        print(f"Ход №{turn}, ходит O")
        return "o"  
    else:
        print(f"Ход №{turn}, ходит X")
        return "x"

    
# функция для отображения игрового поля, как в задании
def show_grid():
    print("  0  1  2")
    for absc, ordi in enumerate(grid):
        print(f"{absc} {'  '.join(ordi)}")
    print("\n")

    
# функция для получения координат хода и их валидации
def get():
    while True:
        coordinates = input("Введите координаты для хода: ").split()
        
        if len(coordinates) != 2:
            print("Ошибка: для хода нужно 2 координаты.")
            continue
             
        abcs, ordi = coordinates
        
        if not (abcs.isdigit() and ordi.isdigit()):
            print("Ошибка: введены не числа.")
            continue
        
        abcs, ordi = int(coordinates[0]), int(coordinates[1])
        
        if not (abcs in range(0,3) and ordi in range(0,3)):
            print("Ошибка: несуществующие координаты.")
            continue
        
        if grid[abcs][ordi] == "x" or grid[abcs][ordi] == "o":
            print(f"Ошибка: здесь уже стоит {grid[abcs][ordi]}.")
            continue         
            
        return abcs, ordi
    

# функция для проверки выигрыша - выбрана реализация из вебинара  
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), 
                ((1, 0), (1, 1), (1, 2)), 
                ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), 
                ((0, 0), (1, 1), (2, 2)), 
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), 
                ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(grid[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print("Победа X!")
            return True
        if symbols == ["o", "o", "o"]:
            print("Победа 0!")
            return True
    return False

# тело основной программы
turn = 0
print("""Для совершения хода вводите координаты клетки. 
Например, "2 1" означает, что ход совершается 
в клетку на пересечении второй строки и первого столбца.\n""")

grid = [[" "] * 3 for i in range(0,3)]

while turn < 9:
    show_grid()
    turn += 1
    player = player_turn(turn)
    x, y = get()
    grid[x][y] = player
    if check_win():
        show_grid()
        break

print("Конец партии.")

