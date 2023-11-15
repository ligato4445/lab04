from lib import count_same_elements
def test_count_same_elements():
    # Тест с тремя различными списками
    list1 = [1, 2, 3, 7, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]
    assert count_same_elements(list1, list2, list3) == 2

    # Тест с тремя одинаковыми списками
    list4 = [1, 2, 3]
    list5 = [1, 2, 3]
    list6 = [1, 2, 3]
    assert count_same_elements(list4, list5, list6) == 3

    # Тест с пустыми списками
    list7 = []
    list8 = []
    list9 = []
    assert count_same_elements(list7, list8, list9) == 0
    print("All tests passed!")

if __name__ == "__main__":
    test_count_same_elements()