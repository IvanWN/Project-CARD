# Пробник проект АиП:

import random # Импортирование библиотек
from PIL import Image

def card_to_channel(card): # Задаем мощности (силы) и масти карт
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

def show_success(deck): # Печатаем карты
    for i in range(len(deck)):
        print(card_to_channel(deck[i]), end = ' ')
    print('\n')

def choice_deck(): # Задаем колоду
    values = ['7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
    colors = ['П', 'Ч', 'Б', 'К']
    deck = []
    i = 0
    while i < len(values):
        j = 0
        while j < len(colors):
            card = {'color': ' ' , 'value' : ' '}
            card['color'] = colors[j]
            card['value'] = values[i]
            deck.append(card)
            j += 1
        i += 1
    random.shuffle(deck)
    return deck

def combination(card1, card2): # Проверяем наличие комбинаций
    value1 = card1['value']
    color1 = card1['color']
    value2 = card2['value']
    color2 = card2['color']
    if (value1 == value2) or (color1 == color2):
        return True
    else:
        return False

def if_possible(list_stack, num_stack): # Проверяем возможность прыжка
    if num_stack >= len(list_stack) - 1:
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

def display_stack(list_stack): # Печатаем стол карт
    for i in range(len(list_stack)):
        print(card_to_channel(list_stack[i]), end = ' ')
    return ''

def step_success(list_stack, deck, show = False): # Добавляем карты на стол и расчитываем возможность прыжка
    list_stack.append(deck[0])
    if show:
        print(display_stack(list_stack), '\n') #!!!!!
    del(deck[0])
    res = if_possible(list_stack, list_stack.index(list_stack[-2]))
    if res and show:
        print(display_stack(list_stack), '\n')
    while res == True and len(list_stack) > 2:
        i = 1
        k = 0
        while i < len(list_stack) - 1 and k == 0:
            res = if_possible(list_stack, list_stack.index(list_stack[i]))
            if res == True:
                if show:
                    print(display_stack(list_stack), '\n')
                k += 1
            i += 1
    for item in list_stack:
        if item['color'] == chr(9824):
            item['color'] = 'П'
        if item['color'] == chr(9825):
            item['color'] = 'Ч'
        if item['color'] == chr(9826):
            item['color'] = 'Б'
        if item['color'] == chr(9827):
            item['color'] = 'К'

def install_auto_mod(deck, show = False): # Автоигра
    list_stack = []
    if show:
        print(display_stack(deck), '\n')
    set = deck.copy()
    num_stack = len(list_stack) - 2
    s = if_possible(list_stack, num_stack)
    if s and show:
        print(display_stack(list_stack), '\n')
    while len(set) > 0: # !!!!!!
        if show:
            step_success(list_stack, set, show = True)
        else:
            step_success(list_stack, set, show = False)
    return list_stack

def response_menu(): # Меню
    print("1. Достать карту ('1')\n2. Прыжок ('2')\n3. Автоматически закончить партию ('3')\n4. Сдаться/выйти ('4')")
    res = input()
    return res

def request_jump(list_stack): # Прыжковое меню
    i = int(input('Укажите индекс карты которая должна совершить прыжок:'))
    while i < 1 or list_stack.index(list_stack[i]) >= list_stack.index(list_stack[-1]):
        i = int(input('Попробуйте еще раз:'))
    return i

def install_manual_mod(deck, max_nb_stack = 2, backspin = False): # Ручной режим игры
    if backspin:
        deck = best_consistent_exchange(deck)
    bib = deck.copy()
    img1 = Image.open('NotStonks.jpg')  # Открываем фото реакций
    img2 = Image.open('Stonks.jpg')
    list_stack = [bib[0], bib[1], bib[2]]
    del(bib[0], bib[0], bib[0])
    print(display_stack(list_stack))
    res = response_menu()
    while res != '4' and len(bib) > 0:
        if res != '1' and res != '2' and res != '3' and res != '4':
            res = input('Попробуйте еще раз:')
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
                if s == False:
                    print('Прыжок невозможен')
                print(display_stack(list_stack))
                res = response_menu()
        if res == '3':
            num_stack = len(list_stack) - 2
            q = if_possible(list_stack, num_stack)
            if q:
                print(display_stack(list_stack))
            while len(bib) > 0:
                step_success(list_stack, bib, show = True)
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

def launching_success(mod, show = False, max_nb_stack = 2): # Выбор режима игры
    deck = choice_deck()
    if mod == 'auto':
        list_stack = install_auto_mod(deck, show)
    elif mod == 'manual':
        list_stack = install_manual_mod(deck, max_nb_stack)
    return list_stack

def best_consistent_exchange(deck): # Подкрутка (по умолчанию включена)
    res = install_auto_mod(deck, show = False)
    w = len(res)
    i = 0
    while i < len(deck) - 1:
        qwert = deck.copy()
        a = qwert[i]
        qwert[i] = qwert[i + 1]
        qwert[i + 1] = a
        bor = install_auto_mod(qwert, show = False)
        if len(bor) <= w:
            colod = qwert.copy()
            w = len(bor)
        i += 1
    return colod

if __name__=="__main__": # ИТОГ
    deck = choice_deck()
    list_stack = []
    card = {'value' : ' ' , 'color' : ' '}
    print(install_manual_mod(deck, max_nb_stack = 5, backspin = False))