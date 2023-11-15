def count_same_elements(*lists):
    # Создаем множество из первого списка, чтобы иметь набор уникальных элементов
    common_elements = set(lists[0])

    # Проходим по каждому остальному списку
    for lst in lists[1:]:
        # Обновляем множество common_elements, оставляя только элементы, которые есть и в текущем списке
        common_elements.intersection_update(lst)

    # Возвращаем количество одинаковых элементов
    return len(common_elements)


# Пример использования функции
list1 = [1, 2, 3, 7, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

result = count_same_elements(list1, list2, list3)
print("количество одинаковых элементов ", result)  # Выведет: 1, так как только элемент 5 присутствует во всех трех списках