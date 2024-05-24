# This is a sample Python script.
import datetime
from dateutil.relativedelta import relativedelta
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def default_parameters(param1, param2='p'):
    result = "Begining program execution with parameters {} and {}".format(param1, param2)
    return result


def calculate_age(year_born):
    result = datetime.date.today().year - year_born
    return result


def calculate_exact_age(year_born, month):
    month_born = datetime.datetime.strptime(month, '%B').strftime('%m')
    date_born = datetime.datetime(year_born, int(month_born), 1)
    difference_in_years = relativedelta(datetime.date.today(), date_born.date()).years
    return difference_in_years


def simple_function():
    print("Simple function")


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def generate_num():
    for i in range(6):
        yield i

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def numerical_representations():
    print("=" * 40 + " Numerical Representations " + "=" * 40 + "\n")
    # numerical representations
    print(1000000)
    print(1_000_000)
    print(0o123)  # octal
    print(0x123)  # hexadecimal
    print(4.5e-10)  # 0.000000000045
    print(0o1 + 0b1 + 0x1 + 1)
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def operators():
    print("=" * 40 + " Operators " + "=" * 40 + "\n")
    # operators
    print(6 / 2)
    print(7 / 2)
    print(7 // 3)
    print(8 // 3)  # 2.6666 sempre arredonda para baixo
    print(7 % 2)
    print(6 % 2)
    print(2 ** 3)
    print(2 + 3.0)  # float result
    print(2 + 3)  # int result

    print(0 % 2)
    print(1 % 2, 2 % 1)
    print(2 % 2, 2 % 2)
    print(3 % 2, 2 % 3)
    print(4 % 2, 2 % 4)
    print(5 % 2, 2 % 5)
    print(14 % 12, 12 % 14)

    print(8 << 2)
    print(8 * 4)

    print(8 >> 2)
    print(8 // 4)

    print(8 << 3)
    print(8 * 8)
    print(1 | 0 ^ 1 & ~0)
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def string_formating():
    print("=" * 40 + " String Formatting " + "=" * 40 + "\n")
    # string formatting
    print("Int named positions {aaa}, {bbb}".format(aaa=123, bbb=555))
    print("Int empty positions {}, {}".format(1, 2))
    print("Int position {1}, {1}".format(123, 888))
    print("Float format {1:.2f}, {0:.3f}".format(123.8888, 888.999999))
    print("Float format {1:.2f}, {0:d}".format(int(123.8888), 888.999999))
    # login = input("Enter your login: ")
    # language = input("Enter your native language: ")
    # print("Your login is {login} and you speak {language}".format(login=login, language=language))
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def type_casting():
    print("=" * 40 + " Type Casting " + "=" * 40 + "\n")
    # type casting
    milhas = '200'
    milhas_float = float(milhas)
    taxa_conversao = 0.6
    print("Milhas em quilometros: ", milhas_float * taxa_conversao)
    ano_nasc = '1988'
    ano_nasc_int = int(ano_nasc)
    ano_atual = 2023
    print("Idade Atual: ", ano_atual - ano_nasc_int)
    # Ordem dos operadores:
    # 1 - **
    # 2 - / // * %
    # 3 - + -
    # se os operadores forem os mesmos: right to left - right binding
    print(2 ** 2 ** 3)
    print(2 ** 8)  # right to left - right binding
    print(2 * 2 * 2 * 2 * 2 * 2 * 2 * 2)  # right to left - right binding
    x = 4
    y = 5
    z = 3
    print(x == y or z)
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def conditions():
    print("=" * 40 + " Conditions " + "=" * 40 + "\n")
    # conditions
    random_num = random.random()
    print(random_num)
    if random_num >= 0.5:
        print(f'Random maior {random_num}')
    elif (random_num > 0.3) and (random_num < 0.7):
        print("O numero está perto do meio")
    else:
        print(f'Random menor {random_num}')
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def iteration_structures():
    print("=" * 40 + " Iteration Structures " + "=" * 40 + "\n")
    # iteration structures
    counter = 5
    while counter <= 10:
        print("Counter: ", counter)
        counter += 1
    for n in range(1, 10):
        print(f'For {n:d}')
    print("Range with one parameter")
    for n in range(10):
        print(f'For {n:d}')
    # 1 not
    # 2 and
    # 3 or
    while True:
        random_num = random.random()
        print(random_num)
        if random_num >= 0.7:
            break
    while True:
        random_num = random.random()
        print(random_num)
        if random_num <= 0.6:
            print("Skipped this number {:.2f}", random_num)
            continue
        if random_num >= 0.7:
            break
    for i in range(10):
        pass
    else:
        print("else do for")
    if True:
        pass
    counter = 0
    while counter <= 10:
        print("Counter: ", counter)
        counter += 1
    else:
        print("Cabou")
    counter = 0
    while counter <= 10:
        print("Counter: ", counter)
        counter += 1
        if counter > 5:
            break
    else:
        print("Cabou não é printado")
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def booleans():
    print("=" * 40 + " Booleans " + "=" * 40 + "\n")
    # booleans
    a = 5
    b = 1
    c = (a > b or b < a) and a == 1
    d = a > b or b < a and a == 1
    print(c)
    print(d)
    print(a > b and a == 1)
    if 2 == 2.0:
        print("true")
    if True and 0 == 1 or not 0 == 1 and False:
        print("a")
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def list_operations():
    print("=" * 40 + " List Operations " + "=" * 40 + "\n")
    # list operations
    board_games = ["munshkin", "sintonia", "the mind", "exploding kittens", "war"]
    print(board_games)
    board_games[0], board_games[4] = board_games[4], board_games[0]
    print(board_games)
    print(board_games[9:10])
    print(board_games[:10])
    print(board_games[1:2])
    print("Slice -1")
    print(board_games[1:-2])
    print(board_games[1:-3])
    print(board_games[1:-4])
    print(board_games[1:0])
    del board_games[1]
    print(board_games)
    del board_games[2:]
    print(board_games)
    del board_games
    # print(board_games)
    # NameError: name
    # 'board_games' is not defined
    grades = [10, 9, 0, 5]
    print(grades)
    grades.append(3)
    print(grades)
    grades.insert(0, 99)
    print(grades)
    # insere no final
    grades.insert(99, 99)
    print(grades)
    primeiro = 1
    segundo = 2
    print(primeiro, segundo)
    primeiro, segundo = segundo, primeiro
    print(primeiro, segundo)
    board_games = ["munshkin", "sintonia", "the mind", "exploding kittens", "war"]
    board_games.sort()
    print(board_games)
    grades = [10, 9, 0, 5]
    grades.sort()
    print(grades)
    grades = [10, 9, 0, 5]
    grades.sort(reverse=True)
    print(grades)
    print(sorted(grades))
    board_games = ["munshkin", "sintonia", "the mind", "exploding kittens", "war"]
    if "munshkin" in board_games:
        print("Munshkin in list")
    del board_games[0]
    if "munshkin" not in board_games:
        print("Munshkin not in list anymore")
    original_name = "Mario"
    new_name = original_name
    print(original_name, new_name)
    original_name = "Luigi"
    print(original_name, new_name)
    games = ["Mario", "Zelda", "Metroid", "Pokémon"]
    games_new = games
    print(games, games_new)
    games_new[0] = "Wave Race"
    print(games, games_new)
    games = ["Mario", "Zelda", "Metroid", "Pokémon"]
    games_new = games[:]
    print(games, games_new)
    games_new[0] = "Wave Race"
    print(games, games_new)
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def number_list_memory_size():
    print("=" * 40 + " Memory Calculations " + "=" * 40 + "\n")
    # Memory calculation
    numbers = 10000000
    list_comprehension = [i for i in range(1, numbers)]
    bits_used = numbers * 32  # 32 is the amount of bits used by number in python
    bytes_used = bits_used / 8
    kilobytes_used = bytes_used / 1000
    megabytes_used = kilobytes_used / 1024
    print("Ocupiying:\n {} bits\n {} bytes\n {} kilobytes\n {} megabytes".format(bits_used, bytes_used, kilobytes_used,
                                                                                 megabytes_used))
    # print(list_comprehension)
    # list_comprehension = [i for i in range(1, 101) if i % 3 == 0]
    # print(list_comprehension)
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def list_comprehension_and_sublists():
    print("=" * 40 + " List comprehension and Sublists " + "=" * 40 + "\n")
    # list comprehension and sublists
    matrix = [["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"]]
    print(matrix)
    print(matrix[2][1])
    for row in matrix:
        print(row)
        for cell in row:
            print(cell)
    for row in matrix:
        for cell in row:
            print(cell, end=" ")
        print()
    table = [[cell for cell in range(1, 6)] for row in range(4)]
    print(table)
    games = ["Mario", "Zelda", "Metroid", "Pokémon"]
    board_games = ["munshkin", "sintonia", "the mind", "exploding kittens", "war"]
    all_games = games + board_games
    print(all_games)
    all_games = games * 2
    print(all_games)
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def string_operations():
    # string operations
    print("=" * 40 + " String Operations " + "=" * 40 + "\n")
    game = "Mario"
    print(game[0])
    print(game[:3])
    # game[0] = "a" doesn't work
    print(game.upper())
    print(game.isnumeric())
    print("10".isnumeric())
    print("10".islower())
    print("10".isspace())
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def tuples():
    print("=" * 40 + " Tuples " + "=" * 40 + "\n")
    # tuples
    empty_tuple = ()
    single_el_tuple_a = (1,)
    single_el_tuple_b = 1,
    print(single_el_tuple_a)
    print(single_el_tuple_b)
    three_el_tuple = 1, 2, 3
    three_el_tuple_b = 1, 2, 3,
    three_el_tuple_c = (1, 2, 3)
    three_el_tuple_d = (1, 2, 3,)

    #  tuples and strings are immutable
    print(three_el_tuple_c)
    print(three_el_tuple_c[2])
    print(len(three_el_tuple_c))
    three_el_tuple_c = three_el_tuple_c[0:-1]
    print("tupla depois do slice")
    print(three_el_tuple_c)
    if 1 in three_el_tuple:
        print("if element present in tuple")
    for item in three_el_tuple:
        print(item)
    new_tuple = three_el_tuple_d + (4, 55, 66)
    print(new_tuple)
    new_tuple = three_el_tuple * 5
    print(new_tuple)
    tuple_struct = ("Marco", "Joinville", 18, ["Sistemas de informação", "Engenharia de software"])
    print(tuple_struct)
    name, city, age, graduation = tuple_struct
    print(name)
    print(city)
    print(age)
    print(graduation)
    game_1 = ("Mario", 9, 200.0)
    game_2 = ("Zelda", 10, 150.0)
    game_3 = ("Metroid", 9, 100.5)
    game_list = [game_1, game_2, game_3]
    for game in game_list:
        print("{} - {} - {}".format(game[0], game[1], game[2]))
    print(abs(10 - 15))
    frequency_array = [0 for i in range(0, 101)]
    print(frequency_array)
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def dictionaries():
    print("=" * 40 + " Dictionaries " + "=" * 40 + "\n")
    # dictionaries
    person = {
        "nome": "Marco",
        "idade": 18,
        "cidade": "joinville"
    }
    keys = {
        1: "Marco",
        1.0: 18,
        (1, 2): "joinville"
    }
    person["nome"] = "Mario"
    print(person)
    person.update({"nome": "Marioo"})
    print(person)
    if "nome" in person:
        print("name key is in var person")
    del person["nome"]
    print(person)
    person["nome"] = "Mario"
    for k in person:
        print("key: ", k)
    for k in person.keys():
        print("key: ", k)
    for v in person.values():
        print("value: ", v)
    for k, v in person.items():
        print("key: ", k, " - value: ", v)
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def functions():
    # functions
    simple_function()
    print(calculate_age(1988))
    print(calculate_age(1996))
    print(calculate_exact_age(1988, "April"))
    print(calculate_exact_age(month="April", year_born=1988))
    print(default_parameters('teste'))
    print(default_parameters('PARAMVALUE1', 'PARAMVALUE2'))
    print(default_parameters('PARAMVALUE1', param2='PARAMVALUE2'))
    # missing 1 required positional argument param1 print(default_parameters(param2='PARAMVALUE2'))
    # Positional argument after keyword argument print(default_parameters(param2='PARAMVALUE2', 'PARAMVALUE1'))
    global main_var  # global keyword means: use the global var 'main_var'
    main_var = "Function"
    main_list_var.append(
        "Function")  # even with shadowing, the value is changed, so the result is the same as a global var
    main_var2 = "shadowed inside"
    main_list_var_2 = ["Function"]
    print(number+1)
    print(main_var)
    print(main_list_var)
    print(main_var2)
    print(main_list_var_2)


def return_and_none():
    print("=" * 40 + " Return and None Value " + "=" * 40 + "\n")
    # return and None value
    x = None
    if x is None:
        print('X is None')
    if x == None:
        print('X == None')
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def recursive_methods():
    print("=" * 40 + " Recursive Methods " + "=" * 40 + "\n")
    # recursive methods
    print(factorial(6))
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


def generators():
    print("=" * 40 + " Generators " + "=" * 40 + "\n")
    # generators
    num = generate_num()
    print("Generated: ", next(num))
    print("Generated: ", next(num))
    print("Generated: ", next(num))
    gen_list = list(generate_num())
    print(gen_list)
    print("*" * 40 + " End " + "*" * 50 + "\n\n")


# Same level: Type, Value, Lookup, Arithmetic
def exceptions():
    print("=" * 40 + " Exceptions " + "=" * 40 + "\n")
    # exceptions
    try:
        random_num = random.random()
        if random_num >= 0.5:
            test = int("a")
        else:
            test = 1 / 0

    except ValueError:
        print("cant cast")
    except ZeroDivisionError:
        print("zero burro")
    except:
        print("General exception")

    dict = {}
    list = []

    try:
        test = dict["a"]
    except KeyError:
        print("Key Error")
    except LookupError:
        print("Lookup Error")

    try:
        test = list[10]
    except IndexError:
        print("Index Error")
    except LookupError:
        print("Lookup Error")

    try:
        test = int('a')
    except ValueError:
        print("Value Error")

    try:
        test = int([])
    except TypeError:
        print("Type Error")

    try:
        test = 10 / 0
    except ZeroDivisionError:
        print("Zero Error")
    except ArithmeticError:
        print("Arithmetic Error")
    # random_num = random.random()
    # assert random_num >= 0.5, "Number should be greater than"
    print("*" * 40 + " End " + "*" * 50 + "\n\n")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm ', '1', '2')

    numerical_representations()

    operators()

    string_formating()

    type_casting()

    conditions()

    iteration_structures()

    booleans()

    list_operations()

    number_list_memory_size()

    list_comprehension_and_sublists()

    string_operations()

    tuples()

    dictionaries()

    print("=" * 40 + " Functions " + "=" * 40 + "\n")
    main_var = 'Main'
    main_var2 = 'Main not shadowed'
    main_list_var = ['Main']
    main_list_var_2 = ['Main']
    number = 5
    print(main_var)
    print(main_var2)
    print(main_list_var)
    print(main_list_var_2)
    print(main_list_var_2)
    print(number)
    functions()
    print(main_var)
    print(main_var2)
    print(main_list_var)
    print(main_list_var_2)
    print(number)
    print("*" * 40 + " End " + "*" * 50 + "\n\n")

    return_and_none()

    recursive_methods()

    generators()

    exceptions()
