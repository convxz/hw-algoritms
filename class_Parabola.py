from math import sqrt, asin, radians
from turtle import *


class Parabola:
    """
    класс Парабола
    """

    def __init__(self, a = 0, b = 0, c = 0) -> None:
        """
        создание функции
        a, b, c: коэффициенты функции
        """
        self.a = a
        self.b = b
        self.c = c
        self.ver = -b / 2 / a
        if a > 0:
            self.branches_up = True
        else:
            self.branches_up = False

    def find_roots(self) -> list[list[float]]:
        """
        находит корни  уравнения
        """
        a = self.a
        b = self.b
        c = self.c
        __D = b**2 - 4 * a * c
        if a:
            if __D > 0:
                x1 = complex((-b - sqrt(__D)) / (2 * a), 0)
                x2 = complex((-b + sqrt(__D)) / (2 * a), 0)
                return 
            elif __D == 0:
                x = complex(-b / (2 * a), 0)
                return [[x.real, x.imag], [x.real, x.imag]]
            else:
                a = -b / (2*a)
                b = sqrt(-__D) / (2 * a)
                x1 = complex(a, b)
                x2 = complex(a, -b)
                return [[x1.real, x1.imag], [x2.real, x2.imag]]

    def display(self, scale):
        a = self.a
        b = self.b
        c = self.c

        def val(x):
            return a * x ** 2 + b * x + c
        
        def draw_line(x1, y1, x2, y2):
            """
            Функция рисует отрезок с координатами первой точки [x1, y1] и координатами второй точки [x2, y2]
            :param x1: координата х первой точки
            :param y1: координата у первой точки
            :param x2: координата х второй точки
            :param y2: координата у второй точки
            :param c: цвет линии
            :return: None
            """
            penup()
            goto(x1, y1)
            pendown()
            goto(x2, y2)
        
        def decart_plane(scale, xcenter = 0, ycenter = 0):
            """
            Функция рисует оси координат
            :param xcenter: координата x центра
            :param ycenter: координата у центра
            :param scale: масштаб
            :param c: цвет
            :return: None
            """
            screensize(700, 540)
            screen = screensize()
            tracer(0)
            lenx = leny = int(screen[0] * 0.9)
            # рисование оси Ох
            draw_line(xcenter - lenx // 2, ycenter, xcenter + lenx // 2, ycenter)
            # рисование оси Оy
            draw_line(xcenter, ycenter - leny // 2, xcenter, ycenter + leny // 2)
            n = lenx // scale
            if n % 2 != 0:
                n -= 1
            dx = 3
            dy = 3
            count = 0
            for i in range(n + 1):
                draw_line(xcenter - (n // 2 - i) * scale, ycenter - dy, xcenter - (n // 2 - i) * scale, ycenter + dy)
                if ((-n // 2) + i) != 0:
                    write((-n // 2) + i)
                    count += 1
            for i in range(n + 1):
                draw_line(xcenter - dx, ycenter - (n // 2 - i) * scale, xcenter + dx, ycenter - (n // 2 - i) * scale)
                write((-n // 2) + i)
            return count

        d = decart_plane(scale)
        h = d/100       
        x0 = -(d//2)    
        for i in range(100):
            draw_line((x0 + h * i) * scale, (val(x0 + h * i))*scale, (x0 + h * (i + 1)) * scale, val((x0 + h * (i + 1)))*scale)


class Triangle:
    """
    класс Треугольник
    """

    def __init__(self, a: list[int], b: list[int], c: list[int]):
        if len(a) == 2:
            side_a = sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
            side_b = sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)
            side_c = sqrt((a[0] - c[0])**2 + (a[1] - c[1])**2)
            if side_a + side_b > side_c and side_a + side_c > side_b and side_c + side_b > side_a:
                p = (side_a + side_b + side_c) / 2
                self.area = sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
                self.side_a, self.side_b, self.side_c = side_a, side_b, side_c
                if side_a == side_b or side_a == side_c or side_b == side_c:
                    self.is_isosceles = True
                    if side_a == side_c:
                        self.is_right = True
                    else:
                        self.is_right = False
                else:
                    self.is_isosceles = False
                    self.is_right = False

    def angles(self):
        sina = self.area/(2 * self.side_b * self.side_c)
        sinb = self.area/(2 * self.side_a * self.side_c)
        sinc = self.area/(2 * self.side_a * self.side_b)
        return [asin(sina), asin(sinb), asin(sinc)]
                
    
if __name__ == "__main__":
    a = Parabola(1, 4, 4)
    print(a.find_roots()) 
    b = Triangle([-1, 3], [-2, -1], [2, 3])
    print(b.side_a, b.side_b, b.side_c)
    print(b.area, b.angles())
    # mainloop()