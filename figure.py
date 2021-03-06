class Circle:
    def __init__(self, x0, y0, r, count_under_circles=0):
        self.__x0 = x0
        self.__y0 = y0
        self.__count_under_circles = count_under_circles
        if r < 0:
            raise ValueError("Ввели отрицательный радиус")
        elif r == 0:
            raise ValueError("Полученная окружность является точкой, r=0")
        else:
            self.__r = r


    @property
    def x0(self):
        return self.__x0

    @property
    def y0(self):
        return self.__y0

    @property
    def r(self):
        return self.__r

    @property
    def count_under_circles(self):
        return self.__count_under_circles

    @r.setter
    def r(self, value):
        if value < 0:
            raise ValueError
        else:
            self.__r = value

    @y0.setter
    def y0(self, value):
        self.__y0 = value

    @x0.setter
    def x0(self, value):
        self.__x0 = value

    def to_str(self):
        return [str(self.__x0), str(self.__y0), str(self.__r)]

    def __str__(self):
        return "x="+str(self.__x0)+" y="+str(self.__y0)+" r="+str(self.__r)+" under="+str(self.count_under_circles)

    @count_under_circles.setter
    def count_under_circles(self, value):
        self.__count_under_circles = value
