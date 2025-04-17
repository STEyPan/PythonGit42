# У вас есть длинная клумба. На этой клумбе разные цветы.
# Есть места под новые, однако цветы не могут ужиться друг с другом, если между ними нет расстояния,
# хотя бы на 1 посадочное место.


# def flower_bed(flowers):
#
#     countEmpty = 0
#     max_flowers = []
#
#     for step in flowers:
#         if step in "0":
#             countEmpty += 1
#         else:
#             countEmpty -= 1
#             max_flowers.append(countEmpty)
#             countEmpty = -1
#
#     max_flowers.append(countEmpty)
#
#     return max(max_flowers) if max(max_flowers) > 0 else 0
#
# print(flower_bed("11100111011111"))

def flower_bed(flowers):

    countEmpty = 0
    max_flowers = 0

    for step in flowers:
        if step in "0":
            countEmpty += 1
        else:
            countEmpty -= 1
            if countEmpty > max_flowers:
                max_flowers = countEmpty
            countEmpty = -1
    if countEmpty > max_flowers:
        max_flowers = countEmpty

    return max_flowers


print(flower_bed("001001"))