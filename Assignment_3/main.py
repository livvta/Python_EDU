def division():
    while True:
        try:
            num1 = float(input("请输入被除数："))
            num2 = float(input("请输入除数："))

            if num2 == 0:
                print("错误：除数不能为零\n")
                continue
            else:
                result = num1 / num2
                print(f"计算结果：{num1} / {num2} = {result}\n")
                break

        except ValueError:
            print("错误：请输入有效数字\n")


def divisibility_check():
    while True:
        try:
            a = ''
            num = int(input("请输入整数"))

            if num % 2 == 0:
                a += '2'
            if num % 3 == 0:
                if a != '':
                    a += '和'
                a += '3'
            if num % 5 == 0:
                if a != '':
                    a += '和'
                a += '5'

            result = "能被{}整除".format(a)

            if a != '':
                print(result, "\n")
                break

            else:
                print("不能被2、3、5整除\n")
                break

        except ValueError:
            print("错误：输入不合法\n")


def main():
    while True:
        print("请选择功能：")
        print("1. 计算两个数字的商")
        print("2. 判断数字的整除性")
        print("输入 'E' 或 'e' 退出程序")

        choice = input("请输入功能选项：")
        if choice == "1":
            division()
        elif choice == "2":
            divisibility_check()
        elif choice.lower() == 'e':
            exit()
        else:
            print("错误：无效选项。请重新输入\n")


if __name__ == "__main__":
    main()
