def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()


def input_data():
    print('Для работы с рациональными числами введите -> 1,комплексными введите -> 2 :')
    data_type = get_value()
    if data_type == '1':
        print('Введите первое число (формата: "1 + 1j"):')
        left_value = get_value()
        print('Введите второе число (формата: "1 + 1j"):')
        right_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    elif data_type == '2':
        print('Введите первое число (формата: "5/11"):')
        left_value = get_value()
        print('Введите второе число (формата: "5/11"):')
        right_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    return (data_type, left_value, oper, right_value)