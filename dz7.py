
#                                             Задание 1

song = input()

volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']

parts = song.split()

itog = list()

for item in parts:
    k = 0
    for letter in item:
        if letter in volwes:
            k += 1
    itog.append(k)
if len(set(itog)) == 1:
    print('True')
else:
    print('False')
#________________________________________________________________________________________


#                                             Задание 2

def print_operation_table(operation, num_rows=4, num_columns=4):
    for i in range(1, num_rows + 1):
        answer = []
        for j in range(1, num_columns + 1):
            answer.append(str(operation(i, j)))
        print("     ".join(answer))
 
 
print_operation_table(lambda x, y: x * y)

def print_operation_table(operation, num_rows=4, num_columns=4):
    for i in range(1, num_rows + 1):
        answer = []
        for j in range(1, num_columns + 1):
            answer.append(str(operation(i, j)))
        print("     ".join(answer))
 
 
print_operation_table(lambda x, y: x ** y)
