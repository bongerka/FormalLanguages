# 1-ый практикум. Вариант 1.
Задача: Даны α и натуральные числа k,l, такие что 0 <= l < k. Проверить, содержит ли язык L слова, чья длина равна l по модулю k.
Алгоритм: Закодируем каждое регулярное выражение таким образом [x0, x1, ..., xk-1], где xn = True, если существует некоторое число a, такое что существует слово длины а * k + n, которое принадлежит языку, задаваемому данным регулярным выражением, и xn = False, если таких слов нет. Пустое слово = [True, False, False, ..., False], любой элемент алфавита = [False, True, False, False, ..., False]. Реализация суммы языков x и y O(k): рассмотрим индекса массивов i, в результирующем массиве(res) в i будет стоять x[i] | y[i](если слово принадлежало х или у, то принадлежит и сумме). Конкатенация O(k^2): рассмотрим всевозможные пары элементов из x, y; если x[i] = True и x[j] = True, то res[(i + j) % (max(len(x), len(y)))] = True. Звезда Клини O(k^3): применяется конкатенация массива с собой не более, чем k раз, и учитывается, что пустое слово задано этим регулярным выражением. Если результат не обновился после очередной конкатенации, то цикл останавливается. Создаем массив answer, в который поэлементно добавляем символы регулярного выражения: (1) если это буква, то кодируем ее массивом и добавляем в answer. (2) Если операция, то достаем два последних элемента из answer и производим операцию. В конце останется один массив, где ответ лежит в answer[0][l](True или False).

Запуск программы: python3 src/main.py reg_expr mod remainder

Проверка покрытия: pytest --cov-report term --cov=src/modules tests/
