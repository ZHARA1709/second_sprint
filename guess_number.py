from random import randint


def say_hello():
    print('Привет')

number = randint(1, 100)
say_hello()
print('Угадайте число от 1 до 100')

while True:
    guess = int(input())

    if guess == number:
        break

    elif guess > number:
        print('Ваше число больше загаданного')

    elif guess < number:
        print('Ваше число меньше загаданного')

print('Вы угадали число')