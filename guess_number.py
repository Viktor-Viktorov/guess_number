from random import randint


guess_number = randint(1, 100)
print(guess_number)


while True:
    num_player = int(input('ВВедите число от 0 до 100: '))
    
    if num_player > guess_number:
        print('Ваше число больше того, что загадано')
    elif num_player < guess_number:
        print('Ваше число меньше того, что загадано')
    elif num_player == guess_number:
        break
print('Отличная интуиция! Вы угадали число :')