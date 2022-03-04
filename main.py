def input_data():
    while True:
        print("Введите значение переменной:")
        try:
            return float(input())
        except ValueError as exc:
            print(f"Введеная строка не является числом. Попробуйте заново.\nПодробнее: {exc}")


def print_output(output):
    print("Результат функции = %.3f" % output)


def history_save(output_data_1, output_data_2, output_data_3):
    history_file = open("Histroy.txt", 'w')  #в этом режиме он перезапишет весь файл
    history_file.write("Входные данные: \n" "X = %d\n" "N = %d\n" % (output_data_1, output_data_2))
    history_file.write("Результат (с точностью до тысячных):\n x^n = %.3f" % output_data_3)


def main():
    x = input_data()
    n = int(input_data())
    answer = x**n
    print_output(answer)
    history_save(x, n, answer)


if __name__ == "__main__":
    main()
