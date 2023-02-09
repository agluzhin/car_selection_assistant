class Car:
    car_inf = {}
    type = ['Хэтчбек', 'Седан', 'Универсал', 'Купе', 'Внедорожник', 'Кабриолет', 'Электромобиль', 'Родстер']

    def __init__(self):
        class_names = ["MersedesEQ", "AMG", "MayBach"]
        print("Выберите класс автомобиля:")
        for name in class_names:
            print(name)

    class MersedesEQ:
        car_inf = {
            # model: engine_power
            'EQE': 215,
            'EQS': 385
         }

    class AMG:
        car_inf = {
            'A-Класс': 110,
            'E-Класс': 320,
            'GLA': 224,
            'GLC': 375,
            'G-Класс': 430,
            'CLA': 310,
            'CLS': 320,
            'GT': 320,
            'SL': 320
        }

    class MayBach:
        car_inf = {
            'S-Класс': 270
        }


car_a = Car()
x = input()
if x == 'MersedesEQ':
    print('Список автомобилей:')
    for i in car_a.MersedesEQ.car_inf:
        print(i)
    z = input()
    if z in car_a.MersedesEQ.car_inf:
        print('Тип автомобиля:', car_a.type[6])
        print('Мощность двигателя:', car_a.MersedesEQ.car_inf[z])
    else:
        print('Ошибка. Начните сначала.')
elif x == 'AMG':
    print('Список автомобилей:')
    for i in car_a.AMG.car_inf:
        print(i)
    z = input()
    if z in car_a.AMG.car_inf:
        if z == 'CLA' or z == 'GT' or z == 'CLS':
            print('Тип автомобиля:', car_a.type[3])
            print('Мощность двигателя:', car_a.AMG.car_inf[z])
        elif z == 'GLA' or z == 'G-Класс':
            print('Тип автомобиля:', car_a.type[4])
            print('Мощность двигателя:', car_a.AMG.car_inf[z])
        elif z == 'A-Класс':
            print('Тип автомобиля:', car_a.type[0], car_a.type[1])
            print('Мощность двигателя:', car_a.AMG.car_inf[z])
        elif z == 'E-Класс':
            print('Тип автомобиля:', car_a.type[1], car_a.type[2], car_a.type[5], car_a.type[3])
            print('Мощность двигателя:', car_a.AMG.car_inf[z])
        elif z == 'GLC':
            print('Тип автомобиля:', car_a.type[3], car_a.type[4])
            print('Мощность двигателя:', car_a.AMG.car_inf[z])
        elif z == 'SL':
            print('Тип автомобиля:', car_a.type[7])
            print('Мощность двигателя:', car_a.AMG.car_inf[z])
    else:
        print('Ошибка. Начните сначала.')
elif x == 'MayBach':
    print('Список автомобилей:')
    for i in car_a.MayBach.car_inf:
        print(i)
    z = input()
    if z in car_a.MayBach.car_inf:
        print('Тип автомобиля:', car_a.type[1])
        print('Мощность двигателя:', car_a.MayBach.car_inf[z])
    else:
        print('Ошибка. Начните сначала.')
else:
    print('Что-то пошло не так... Попробуйте ещё раз.')
