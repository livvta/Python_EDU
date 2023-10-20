import turtle


# 绘制水平段
def draw_horizontal_line(draw, horizontal_length):
    turtle.pendown() if draw else turtle.penup()
    turtle.forward(horizontal_length)
    turtle.right(90)


# 绘制垂直段
def draw_vertical_line(draw, vertical_length):
    turtle.pendown() if draw else turtle.penup()
    turtle.forward(vertical_length)
    turtle.right(90)


# 组合绘制数码管
def draw_character(character, horizontal_length, vertical_length):
    draw_horizontal_line(character in ['2', '3', '4', '5', '6', '8', '9', 'a', 'b', 'd', 'e', 'f'], horizontal_length)
    draw_vertical_line(character in ['0', '1', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'd'], vertical_length)
    draw_horizontal_line(character in ['0', '2', '3', '5', '6', '8', '9', 'b', 'c', 'd', 'e'], horizontal_length)
    draw_vertical_line(character in ['0', '2', '6', '8', 'a', 'b', 'c', 'd', 'e', 'f'], vertical_length)
    turtle.left(90)
    draw_vertical_line(character in ['0', '4', '5', '6', '8', '9', 'a', 'b', 'c', 'e', 'f'], vertical_length)
    draw_horizontal_line(character in ['0', '2', '3', '5', '6', '7', '8', '9', 'a', 'c', 'e', 'f'], horizontal_length)
    draw_vertical_line(character in ['0', '1', '2', '3', '4', '7', '8', '9', 'a', 'd'], vertical_length)
    turtle.left(180)
    turtle.penup()

    turtle.fd(horizontal_length / 4)  # 设置数码管间隔


def set_pen_attributes(valid_chars):
    while True:
        date = input("请输入要显示的字符：")
        if all(char in valid_chars for char in date):
            break
        else:
            print(f"无效字符，请仅输入有效字符：{valid_chars}")

    while True:
        pen_color = input("请输入画笔颜色（例如：red、blue）：")
        if pen_color in ['red', 'blue', 'green', 'black', 'purple', 'orange']:
            break
        else:
            print("无效颜色，请输入有效颜色。")

    while True:
        try:
            horizontal_length = int(input("请输入数码管长度（整数）："))
            if horizontal_length > 0:
                break
            else:
                print("数码管长度必须是正整数。")
        except ValueError:
            print("请输入有效的数码管长度。")

    while True:
        try:
            vertical_length = int(input("请输入数码管宽度（整数）："))
            if vertical_length > 0:
                break
            else:
                print("数码管宽度必须是正整数。")
        except ValueError:
            print("请输入有效的数码管宽度。")

    return date, pen_color, horizontal_length, vertical_length


def draw_string(string, horizontal_length, vertical_length):
    string = string.lower()
    for char in string:
        draw_character(char, horizontal_length, vertical_length)


def main():
    turtle.speed(7)
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)

    valid_chars = "0123456789abcdefABCDEF"
    date, pen_color, horizontal_length, vertical_length = set_pen_attributes(valid_chars)
    turtle.pencolor(pen_color)
    draw_string(date, horizontal_length, vertical_length)
    turtle.hideturtle()
    turtle.pendown()
    turtle.done()


if __name__ == "__main__":
    main()
