# На 1000г. мяса
#
# Нитритная соль: 10
# Поваренная соль: 15
# Стартовые культуры: 0,5
# Моносахара: 5
# 2 дня на каждые 500 г.


def nitro_salt(m):
    # 1000 : 10 = m : x
    try:
        m = int(m)
    except ValueError:
        m = 0
    return int(10 * m / 1000)

