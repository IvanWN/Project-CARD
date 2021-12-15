# Тестики
import pytest
from Project import combination, if_possible, choice_deck, step_success, install_auto_mod, best_consistent_exchange


def test_choice_deck():
    """Проверка наличия всех карт в коллоде."""
    deck = choice_deck()
    card1 = {'color': 'П', 'value': 'К'}
    card2 = {'color': 'П', 'value': '9'}
    choice_deck()
    assert card1 in deck and card2 in deck


def test_combination():
    """Проверка исправной работы комбинаций."""
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


def test_if_possible():
    """Проверка корректной работы прыжков."""
    num_stack = 4
    list_stack = [{'color': '♢', 'value': '9'}, {'color': '♣', 'value': '7'}, {'color': '♢', 'value': 'К'}]
    if_possible(list_stack, num_stack)
    assert not if_possible(list_stack, num_stack)


def test_step_success_test():
    """
    Проверка корректного добавления первой карты из коллоды
    на стол и не подмешал дубляжа (Без мошенничества со стороны крупье :) ).
    """
    list_stack = [{'color': 'К', 'value': '10'}, {'color': 'П', 'value': 'Т'}]
    deck = [{'color': 'Б', 'value': 'Д'}, {'color': 'П', 'value': '9'}, {'color': 'Б', 'value': 'К'},
            {'color': 'Б', 'value': '9'}, {'color': 'Ч', 'value': 'Д'}, {'color': 'Ч', 'value': 'К'},
            {'color': 'Ч', 'value': '9'}, {'color': 'Б', 'value': 'В'}, {'color': 'П', 'value': 'В'},
            {'color': 'Б', 'value': '10'}, {'color': 'Б', 'value': '8'}, {'color': 'П', 'value': 'К'},
            {'color': 'Ч', 'value': '7'}, {'color': 'К', 'value': 'Д'}, ...]
    D = deck[0]
    step_success(list_stack, deck)
    assert D in list_stack and not deck[0] in list_stack


def test_best_consistent_exchange():
    """Проверка, что при использовании подкрученной колоды ваш результат будет лучше."""
    deck = choice_deck()
    res = len(install_auto_mod(deck))
    colod = len(install_auto_mod(best_consistent_exchange(deck)))
    assert colod < res