# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать план проекта по этапам/или создать kanban доску для работы над данным проектом
# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
# Требования:
# 1. Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# 2. Игра должна быть реализована как консольное приложение.
# Классы:
# Класс `Hero`:
# - Атрибуты:
# - Имя (`name`)
# - Здоровье (`health`), начальное значение 100
# - Сила удара (`attack_power`), начальное значение 20
# - Методы:
# - `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
# - `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
# Класс `Game`:
# - Атрибуты:
# - Игрок (`player`), экземпляр класса `Hero`
# - Компьютер (`computer`), экземпляр класса `Hero`
# - Методы:
# - `start()`: начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атаковал {other.name} и нанес {damage} повреждений.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Битва начинается!")

        # Первый атакующий - рандомно
        if random.choice([True, False]):
            turn = "player"
            print(f"{self.player.name} атакует первым!")
        else:
            turn = "computer"
            print(f"{self.computer.name} атакует первым!")

        while self.player.is_alive() and self.computer.is_alive():
            if turn == "player":
                self.player.attack(self.computer)
                print(f"Здоровье {self.computer.name}: {self.computer.health}")
                if not self.computer.is_alive():
                    print(f"В этом раунде {self.computer.name} повержен! {self.player.name} победил!")
                    break
                turn = "computer"
            else:
                self.computer.attack(self.player)
                print(f"Здоровье {self.player.name}: {self.player.health}")
                if not self.player.is_alive():
                    print(f"В этом раунде {self.player.name} повержен! {self.computer.name} победил!")
                    break
                turn = "player"

player_name = input("Введите имя вашего героя: ")
computer_name = "Компьютер"
game = Game(player_name, computer_name)
game.start()
