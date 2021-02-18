
# 8.1 Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9

from hashlib import sha1

def substr_count(string):

    str_length = len(string)
    assert str_length, f'String must be not empty'

    # substr = []
    substr_hash = []

    for pos_1 in range(str_length):
        for pos_2 in range(pos_1 + 1, str_length + 1):
            # subs = string[pos_1:pos_2]
            # print(f'{subs=}, {pos_1=}, {pos_2=}')
            # subs_hash = sha1(string[pos_1:pos_2].encode("utf-8")).hexdigest()
            # print(subs_hash)

            # if subs_hash != sha1(string.encode("utf-8")).hexdigest():
            #     substr.append(subs)
            #     substr_hash.append(subs_hash)
            #     print(f'{substr=}, {substr_hash=}')

            # substr_hash.append(sha1(string[pos_1:pos_2].encode("utf-8")).hexdigest())
            substr_hash.append(hash(string[pos_1:pos_2]))
            
            # print(f'{substr_hash=}')

    # вычитаем из длины множества уникальных эдементов единицу (вместо того,
    # чтобы проверять каждую подстроку if'ом, не является ли она строкой целиком):

    return len(set(substr_hash)) - 1


str_ = input("Введите строку: ")

print(f"Количество подстрок во введённой строке: {substr_count(str_)}")
