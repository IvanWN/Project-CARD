# Тестики
import pytest
from Project import combination, if_possible, choice_deck, step_success

# Проверка наличия всех карт в коллоде
def test_choice_deck():
    deck = choice_deck()
    card1 = {'color': 'П', 'value': 'К'}
    card2 = {'color': 'П', 'value': '9'}
    choice_deck()
    assert card1 in deck and card2 in deck

# Проверка исправной работы комбинаций
def test_combination():
    card1 = {'color': '♣', 'value': 'Т'}
    card2 = {'color': '♢', 'value': 'Т'}
    combination(card1, card2)
    assert True
    card1 = {'color': '♣', 'value': 'Т'}
    card2 = {'color': '♣', 'value': '7'}
    combination(card1, card2)
    assert True
    card1 = {'color': '♢', 'value': 'Т'}
    card2 = {'color': '♣', 'value': '7'}
    assert not combination(card1, card2)

# Проверка корректной работы прыжков
def test_if_possible():
    num_stack = 4
    list_stack = [{'color': '♢', 'value': '9'}, {'color': '♣', 'value': '7'}, {'color': '♢', 'value': 'К'}]
    if_possible(list_stack, num_stack)
    assert not if_possible(list_stack, num_stack)

# Проверка корректного добавления первой карты из коллоды на стол и не подмешал дубляжа (Без мошенничества со стороны диллера :) )
def test_step_success_test():
    list_stack = [{'color': 'К', 'value': '10'}, {'color': 'П', 'value': 'Т'}]
    deck = [{'color': 'Б', 'value': 'Д'}, {'color': 'П', 'value': '9'}, {'color': 'Б', 'value': 'К'},
            {'color': 'Б', 'value': '9'}, {'color': 'Ч', 'value': 'Д'}, {'color': 'Ч', 'value': 'К'},
            {'color': 'Ч', 'value': '9'}, {'color': 'Б', 'value': 'В'}, {'color': 'П', 'value': 'В'},
            {'color': 'Б', 'value': '10'}, {'color': 'Б', 'value': '8'}, {'color': 'П', 'value': 'К'},
            {'color': 'Ч', 'value': '7'}, {'color': 'К', 'value': 'Д'}, ...]
    D = deck[0]
    step_success(list_stack, deck)
    assert D in list_stack and not deck[0] in list_stack


'''
deck = [{'color': 'Б', 'value': 'Д'}, {'color': 'П', 'value': '9'}, {'color': 'Б', 'value': 'К'}, {'color': 'Б', 'value': '9'}, {'color': 'Ч', 'value': 'Д'}, {'color': 'Ч', 'value': 'К'}, {'color': 'Ч', 'value': '9'}, {'color': 'Б', 'value': 'В'}, {'color': 'П', 'value': 'В'}, {'color': 'Б', 'value': '10'}, {'color': 'Б', 'value': '8'}, {'color': 'П', 'value': 'К'}, {'color': 'Ч', 'value': '7'}, {'color': 'К', 'value': 'Д'}, ...]
list_stack = [{'color': '♣', 'value': '10'}, {'color': '♠', 'value': 'Т'}]
show = True
'''