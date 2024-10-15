first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [abs(len(i) - len(j)) for i, j in zip(first, second) if len(i) - len(j) != 0]
second_result = [True if len(first[i]) == len(second[i]) else False for i in range(0, len(first))]

print(first_result)
print(second_result)
