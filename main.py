# используется для сортировки
from operator import itemgetter

class Computer:
    """Компьютор"""
    def __init__(self, id, manufacturer, os, microprocessor_id):
        self.id = id
        self.manufacturer = manufacturer
        self.os = os
        self.microprocessor_id = microprocessor_id
class Microprocessor:
    """Микропроцессор"""
    def __init__(self, id, PartNumber, cost):
        self.id = id
        self.PartNumber = PartNumber
        self.cost = cost
# Компьюторы
Computers = [
    Computer(1, 'HP', 'Windows OS', 11),
    Computer(2, 'ASUS', 'Windows OS', 22),
    Computer(3, 'Apple', 'MAC OS', 33),
    Computer(4, 'Lenovo', 'Windows OS', 44),
    Computer(5, 'Acer', 'Windows OS', 55)
]
# Микропроцессоры
Microprocessors = [
    Microprocessor(11, 'Intel core i3', 30),
    Microprocessor(22, 'Intel core i7', 50),
    Microprocessor(33, 'Apple M3', 60),
    Microprocessor(44, 'Intel core i10', 60),
    Microprocessor(44, 'Intel core i5', 40)
]
def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [(b.PartNumber, b.cost, c.manufacturer)
        for b in Microprocessors
        for c in Computers
        if c.microprocessor_id == b.id]
    print('Задание 1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    print('\nЗадание 2')
    res_12_unsorted = []
    # Перебираем все опраторы
    for c in Computers:
        c_microprocessors = list(filter(lambda i: i[2]==c.manufacturer, one_to_many))
        if len(c_microprocessors) > 0:
            b_cost = [cost for _,cost,_ in c_microprocessors]
            b_cost_sum = sum(b_cost)
            res_12_unsorted.append((c.manufacturer, b_cost_sum))            
            # Сортировка по суммарной странице
    
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
if __name__ == '__main__':
    main()


"""
Задание 1
[('Intel core i7', 50, 'ASUS'), ('Apple M3', 60, 'Apple'), ('Intel core i3', 30, 'HP'), ('Intel core i10', 60, 'Lenovo'), ('Intel core i5', 40, 'Lenovo')]

Задание 2
[('Lenovo', 100), ('Apple', 60), ('ASUS', 50), ('HP', 30)]
"""