# Проект АиП:

# Импортирование библиотек
import random
from PIL import Image


# Задаем мощности (силы) и масти карт
def card_to_channel(card):
    """
    Функция заменяет буквы масти на символы
    и задает одинаковую длину для каждой карты.
    Возвращает откорректированные карты.
    card - игровая карта;
    value - мощность карты;
    color - масть карты.
    """
    if card['color'] == 'П':
        card['color'] = chr(9824)
    if card['color'] == 'Ч':
        card['color'] = chr(9825)
    if card['color'] == 'Б':
        card['color'] = chr(9826)
    if card['color'] == 'К':
        card['color'] = chr(9827)
    if card['color'] == '10':
        return card['value'] + card['color']
    else:
        return ' ' + card['value'] + card['color']


# Задаем колоду
def choice_deck():
    """
    Создаем колоду игральных карт, с помощью values и colors,
    отвечающих за мощность и масть карт, и перемешивания их в произвольном порядке (random.).
    Функция возвращает готовую к использованию колоду.
    deck - готовая к использованию колода.
    """
    values = ['7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
    colors = ['П', 'Ч', 'Б', 'К']
    deck = []
    i = 0
    while i < len(values):
        j = 0
        while j < len(colors):
            card = dict(color=' ', value=' ')
            card['color'] = colors[j]
            card['value'] = values[i]
            deck.append(card)
            j += 1
        i += 1
    random.shuffle(deck)
    return deck


# Проверяем наличие комбинаций
def combination(card1, card2):
    """
    Функция проверяет наличие комбинаций карт,
    комбинации - равность мастей или мощностей.
    card1 - первая карта комбинации;
    card2 - вторая карта комбинации.
    """
    value1 = card1['value']
    color1 = card1['color']
    value2 = card2['value']
    color2 = card2['color']
    if (value1 == value2) or (color1 == color2):
        return True
    else:
        return False


# Проверяем возможность прыжка
def if_possible(list_stack, num_stack):
    """
    Функция проверяет возможность прыжка и делает прыжок,
    исключая неправильные команды.
    num_stack - индекс карты для прыжка;
    list_stack - игровой стол.
    """
    if num_stack >= len(list_stack) - 1:
        return False
    elif type(num_stack) != int:
        return False
    else:
        card1 = list_stack[num_stack - 1]
        card2 = list_stack[num_stack + 1]
        if combination(card1, card2):
            list_stack[num_stack - 1] = list_stack[num_stack]
            del(list_stack[num_stack])
            return True
        else:
            return False


# Печатаем стол карт
def display_stack(list_stack):
    """
    Функция выводит карты со стола карт в консоль.
    list_stack - стол карт.
    """
    for i in range(len(list_stack)):
        print(card_to_channel(list_stack[i]), end=' ')


# Добавляем карты на стол и расчитываем возможность прыжка
def step_success(list_stack, deck, show=False):
    """
    Функция делает все возможные прыжки предпослдней картой
    и выводит действия прыжков в автоигре.
    list_stack - стол карт.
    deck - колода карт;
    show - позволяет видеть промежуточные действия.
    """
    list_stack.append(deck[0])
    if show:
        print(display_stack(list_stack), '\n')
    del(deck[0])
    res = if_possible(list_stack, list_stack.index(list_stack[-2]))
    if res and show:
        print(display_stack(list_stack), '\n')
    while res and len(list_stack) > 2:
        i = 1
        k = 0
        while i < len(list_stack) - 1 and k == 0:
            res = if_possible(list_stack, list_stack.index(list_stack[i]))
            if res:
                if show:
                    print(display_stack(list_stack), '\n')
                k += 1
            i += 1
    for item in list_stack:
        item = card_to_channel(item)


# Автоигра
def install_auto_mod(deck):
    """
    Автоигра используемая для определения оптимального матча в подкрутке.
    Возвращает стол карт.
    list_stack - стол карт;
    deck - колода карт.
    """
    list_stack = []
    set = deck.copy()
    i = 0
    while i < 3:
        list_stack.append(set[0])
        del(set[0])
        i += 1
    num_stack = len(list_stack) - 2
    if_possible(list_stack, num_stack)
    while len(set) > 0:
        step_success(list_stack, set, show=False)
    for item in list_stack:
        item = card_to_channel(item)
    for item in deck:
        item = card_to_channel(item)
    return list_stack


# Меню
def response_menu():
    """
    Функция печатает перечень действий игроку, фиксирует и возвращает его выбор.
    res - выбор действия игрока.
    """
    print("1. Достать карту ('1')\n2. Прыжок ('2')\n3. Автоматически закончить партию ('3')\n4. Сдаться/выйти ('4')")
    res = input()
    return res


# Прыжковое меню
def request_jump(list_stack):
    """
    Функция проверяет корректный ли индекс карты введен для прыжка и возвращает его после проверки.
    list_stack - стол карт;
    i - индекс карты которая должна совершить прыжок.
    """
    i = int(input('Укажите индекс карты которая должна совершить прыжок:'))
    while i < 1 or list_stack.index(list_stack[i]) >= list_stack.index(list_stack[-1]):
        i = int(input('Попробуйте еще раз:'))
    return i


# Ручной режим игры
def install_manual_mod(deck, max_nb_stack=5, backspin=False, show=False):
    """
    Функция позволяет вручную играть в данную карточную игру.
    Возврвщает итоговый стол карт.
    show - позволяет видеть промежуточные действия;
    backspin - проверяет включенность подкрутки;
    deck - колода карт;
    list_stack - итоговый стол карт;
    max_nb_stack - максимальное колличество кард на столе к концу игры.
    """
    if backspin:
        deck = best_consistent_exchange(deck)
    bib = deck.copy()
    img1 = Image.open('NotStonks.jpg')
    img2 = Image.open('Stonks.jpg')
    list_stack = [bib[0], bib[1], bib[2]]
    del (bib[0], bib[0], bib[0])
    print(display_stack(list_stack))
    res = response_menu()
    while res != '4' and len(bib) > 0:
        if res != '1' and res != '2' and res != '3' and res != '4':
            res = input('Введите правильную команду:')
        if res == '1':
            list_stack.append(bib[0])
            del(bib[0])
            print(display_stack(list_stack))
            res = response_menu()
        if res == '2':
            if len(list_stack) < 3:
                print('Прыжок невозможен')
                res = input('Выберете другое действие:')
            else:
                k = request_jump(list_stack)
                s = if_possible(list_stack, k)
                if not s:
                    print('Прыжок невозможен')
                print(display_stack(list_stack))
                res = response_menu()
        if res == '3':
            while len(bib) > 0:
                step_success(list_stack, bib, show)
    if res == '4':
        while len(bib) > 0:
            list_stack.append(bib[0])
            del(bib[0])
    if len(list_stack) > max_nb_stack:
        print('Проигрыш!')
        img1.show()
    else:
        print('Победа! Победа! Вместо обеда!')
        img2.show()
    list_stack = display_stack(list_stack)
    return list_stack


# Подкрутка (по умолчанию включена)
def best_consistent_exchange(deck):
    """
    Функция меняет в колоде местами такие 2 соседние карты,
    чтобы минимизировать колличество карт в конце игры. Возвращает оптимальную колоду.
    colod - оптимальная колода.
    """
    res = install_auto_mod(deck)
    w = len(res)
    i = 0
    while i < len(deck) - 1:
        qwert = deck.copy()
        qwert[i + 1], qwert[i] = qwert[i], qwert[i + 1]
        bor = install_auto_mod(qwert)
        if len(bor) <= w:
            colod = qwert.copy()
            w = len(bor)
        i += 1
    return colod


# ИТОГ
if __name__ == "__main__":
    deck = choice_deck()
    list_stack = []
    card = dict(color=' ', value=' ')
    print(install_manual_mod(deck, max_nb_stack=5, backspin=True, show=True))