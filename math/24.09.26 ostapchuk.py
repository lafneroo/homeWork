def weigh(left, right, fake, sign):
    w_left = 0
    for coin in left:
        if coin == fake:
            w_left = w_left + (1 if sign == 'Т' else -1)

    w_right = 0
    for coin in right:
        if coin == fake:
            w_right = w_right + (1 if sign == 'Т' else -1)

    if w_left > w_right:
        return '>'
    if w_left < w_right:
        return '<'
    return '='


def find_fake(fake, sign):
    r1 = weigh([1,2,3,4], [5,6,7,8], fake, sign)

    if r1 == '=':
        r2 = weigh([9,10,11], [1,2,3], fake, sign)

        if r2 == '=':
            r3 = weigh([12], [1], fake, sign)
            if r3 == '>':
                return (12, 'Т')
            else:
                return (12, 'Л')

        if r2 == '<':
            r3 = weigh([9], [10], fake, sign)
            if r3 == '<':
                return (9, 'Л')
            if r3 == '>':
                return (10, 'Л')
            return (11, 'Л')

        if r2 == '>':
            r3 = weigh([9], [10], fake, sign)
            if r3 == '>':
                return (9, 'Т')
            if r3 == '<':
                return (10, 'Т')
            return (11, 'Т')

    if r1 == '>':
        r2 = weigh([1,2,5], [3,6,9], fake, sign)

        if r2 == '=':
            r3 = weigh([7], [8], fake, sign)
            if r3 == '<':
                return (8, 'Л')
            if r3 == '>':
                return (7, 'Л')
            return (4, 'Т')

        if r2 == '>':
            r3 = weigh([1], [2], fake, sign)
            if r3 == '>':
                return (1, 'Т')
            if r3 == '<':
                return (2, 'Т')
            return (6, 'Л')

        if r2 == '<':
            r3 = weigh([5], [9], fake, sign)
            if r3 == '<':
                return (5, 'Л')
            return (3, 'Т')

    if r1 == '<':
        r2 = weigh([1,2,5], [3,6,9], fake, sign)

        if r2 == '=':
            r3 = weigh([7], [8], fake, sign)
            if r3 == '<':
                return (7, 'Т')
            if r3 == '>':
                return (8, 'Т')
            return (4, 'Л')

        if r2 == '<':
            r3 = weigh([1], [2], fake, sign)
            if r3 == '<':
                return (1, 'Л')
            if r3 == '>':
                return (2, 'Л')
            return (6, 'Т')

        if r2 == '>':
            r3 = weigh([5], [9], fake, sign)
            if r3 == '>':
                return (5, 'Т')
            return (3, 'Л')


print("Проверяем все 24 гипотезы...")
ok = True

for coin in range(1, 13):
    for sign in ['Т', 'Л']:
        result = find_fake(coin, sign)
        expected = (coin, sign)
        if result != expected:
            print("Ошибка:", coin, sign, "->", result)
            ok = False

if ok:
    print("Все 24 гипотезы найдены верно!")

print()
print("Пример: монета 6 лёгкая")
print("Ответ:", find_fake(6, 'Л'))