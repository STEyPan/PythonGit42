# Операторы
# Операторы - это особые команды языка, которые можно вызывать,
# через закрепленные за ними символы
# + сложение
# - вычитание
# Операнды - это непосредственно переменные, которые принимает участвие в операции
# Стандартный вид операции: <операнд> <оператор> <операнд>

# Группы операторов по кол-ву операндов:
# Унарные операторы:
# Инверсия (-var), отрицание (-var), логическое отрицание (not var)
# Проверка на True/False(var), Индексатор(var[i]), Присвоение по индексу(var[i] = k),
# Удаление по индексу(del var[i])
# Бинарные операторы:
# Математические операции (var+var. var-var, var*var, var/var, var//var)
# Логические операции (var < var, var > var, var == var, var != var)
# Присвоение (var = var, var += var, var -= var, var *= var...)

from oper import Oper

if __name__ == "__main__":
    var_1 = Oper(10)
    var_2 = Oper(0)
    var_3 = Oper(11)

    if var_1:
        print(f"var_1 is True")
    if var_2:
        print(f"var_2 is True")
    else:
        print(f"var_2 is False")

    if var_1 != "Hello":
        print(f"var_1 is False")

    print(var_3)