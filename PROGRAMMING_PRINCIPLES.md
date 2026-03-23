Lab03_Python

1. Модульність.
Кожне завдання винесене в окремий файл, що дозволяє не змішувати різну логіку і легко орієнтуватися в проєкті:
[task1.py](https://github.com/irynamazurova-wq/Lab03_Python/blob/master/task1.py),
[task2.py](https://github.com/irynamazurova-wq/Lab03_Python/blob/master/task2.py)

2. Single Responsibility Principle.
Кожен файл виконує одну конкретну задачу: підрахунок слів, заміна символів, пошук слова тощо. Рахує лише кількість входжень слова:
[task3.py](https://github.com/irynamazurova-wq/Lab03_Python/blob/master/task3.py)

3. Fail Fast.
Перевірка вхідних даних відбувається на початку виконання, до будь-якої обробки:
[task2.py, рядки 2–4](https://github.com/irynamazurova-wq/Lab03_Python/blob/master/task2.py#L2-L4) (перевіряє порожній рядок одразу після введення)
[task5.py, рядки 4–5](https://github.com/irynamazurova-wq/Lab03_Python/blob/master/task5.py#L4-L5) (перевіряє чи введені символи є літерами)

4. Для фільтрації слів використовуються list comprehensions замість повторюваних циклів:
[task5.py, рядок 8](https://github.com/irynamazurova-wq/Lab03_Python/blob/master/task5.py#L8),
[task7.py, рядок 5](https://github.com/irynamazurova-wq/Lab03_Python/blob/master/task7.py#L5)
