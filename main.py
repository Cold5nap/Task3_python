from figure import Circle
from sys import argv


def matrix_int_from_file(direct):
    try:
        file = open(direct)
        data = file.read()
        file.close()

        data = data.split('\n')
        pop_count = 0
        for i in range(len(data)):
            if data[i - pop_count] == '':
                data.pop(i - pop_count)
                pop_count += 1

        pop_count = 0
        for i in range(len(data)):
            data.append(data.pop(i - pop_count).split(' '))
            pop_count += 1

        int_data = []
        for rows in range(len(data)):
            int_data.append([])
            for ch in range(len(data[rows])):
                int_data[rows].append(int(data[rows][ch]))

        return int_data
    except FileNotFoundError:
        print("Not Found")


def list_max_under_circles(circles):
    in_circles = []
    size = len(circles)
    for i in range(size):
        x0_c1 = circles[i].x0
        y0_c1 = circles[i].y0
        r_c1 = circles[i].r
        count_in_circles = 0
        for j in range(size):
            x0_c2 = circles[j].x0
            y0_c2 = circles[j].y0
            r_c2 = circles[j].r
            if (not circles[i] == circles[j]
                    and x0_c1 + r_c1 >= x0_c2 + r_c2
                    and x0_c2 - r_c2 >= x0_c1 - r_c1
                    and y0_c1 + r_c1 >= y0_c2 + r_c2
                    and y0_c2 - r_c2 >= y0_c1 - r_c1):
                count_in_circles += 1
        in_circles.append(count_in_circles)

    print(in_circles)

    max_number = in_circles[0]
    for i in range(len(circles)):
        if max_number < in_circles[i]:
            max_number = in_circles[i]

    under_circles = []
    for i in range(len(in_circles)):
        circles[i].count_under_circles = in_circles[i]
        if max_number == in_circles[i]:
            under_circles.append(circles[i])

    return under_circles


def circle_max_square(circles):
    max_circle = circles[0]
    for i in range(len(circles)):
        if max_circle.r < circles[i].r:
            max_circle = circles[i]
    return max_circle


def main():
    direct = "input\input" + argv[1] + ".txt"
    matrix = matrix_int_from_file(direct).copy()

    circles = []
    for circle in matrix:
        circle = Circle(circle[0], circle[1], circle[2])
        circles.append(circle)

    print("input01 - одна окружность в ответе(есть окружность которая относится к нескольким)\n" +
          "input02 - содержит отрицательный радиус\n" +
          "input03 - пересечение окружностей\n" +
          "input04 - 3 большие окружности с касаниями \n" +
          "input05 - содержит точки, а не окружности")

    print("x0, y0, radius")
    for row in matrix:
        print(row)

    print("Наибольшее кол-во подокружностей: ")
    under_circles = list_max_under_circles(circles)
    for i in range(len(under_circles)):
        print(under_circles[i].__str__())

    print("Окружность с наибольшей площадью:")
    total_circle = circle_max_square(under_circles)
    print(total_circle.__str__())

#9
if __name__ == '__main__':
    main()
