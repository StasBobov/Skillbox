# def get_vector(start_point, angle, length=100, width=1):

import math
import random

resolution = (600, 600)

def _is_point(param):
    """
        Является ли параметр координатой?
    """
    return isinstance(param, Point)

def random_number(a=0, b=300):
    """
        Выдать случайное целое из диапазона [a,b]
    """
    return random.randint(a, b)

class Point:
    """
        Класс точки экрана
    """

    def __init__(self, x=None, y=None):
        self._x = random_number(1, resolution[0]) if x is None else int(x)
        self._y = random_number(1, resolution[1]) if y is None else int(y)

    def to_screen(self):
        return int(self._x), resolution[1] - int(self._y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = int(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = int(value)

    def __str__(self):
        return 'Point(x={}, y={})'.format(self.x, self.y)

class Vector:
    """Класс математического вектора"""

    def __init__(self, start_point, direction, length, width=1):
        """
            Создать вектор из точки start_point в направлении direction (градусы) длинной length
            Внимание! Параметр width в следующей версии будет удален, используйте .draw(..., width)
        """
        self.start_point = start_point
        direction = (direction * math.pi) / 180
        self.dx = math.cos(direction) * length
        self.dy = math.sin(direction) * length
        self.module = length
        self.width = width

    def _determine_module(self):
        return math.sqrt(self.dx ** 2 + self.dy ** 2)

    @property
    def end_point(self):
        return Point(self.start_point.x + self.dx, self.start_point.y + self.dy, )

    @property
    def angle(self):
        if self.dx == 0:
            if self.dy >= 0:
                return 90
            else:
                return 270
        else:
            angle = math.atan(self.dy / self.dx) * (180 / math.pi)
            if self.dx < 0:
                angle += 180
        return angle

    def add(self, vector2):
        """Сложение векторов"""
        self.dx += vector2.dx
        self.dy += vector2.dy
        self.module = self._determine_module()

    def __str__(self):
        return 'vector([%.2f,%.2f],{%.2f,%.2f})' % (self.dx, self.dy, self.angle, self.module)

    def __repr__(self):
        return str(self)

def get_vector(start_point, angle, length=100, width=1):
    """
        Получить вектор из точки start, в направлении angle, длиной length
        Внимание! Параметр width в следующей версии будет удален, используйте Vector.draw(..., width)
    """
    return Vector(start_point=start_point, direction=angle, length=length, width=width)

def vector(start, angle, length, color=(255, 255, 0), width=1):
    """
        Нарисовать вектор цветом color толщиной width
        Из точки start
        В направлении angle
        Длиной length
    """
    if not _is_point(start):
        print("'start' param must be point (x,y,)")
        return
    # _init()
    v = Vector(start_point=start, direction=angle, length=length)
    # v.draw(color=color, width=width)
    return v.end_point

    def __nonzero__(self):
        """Проверка на пустоту"""
        return int(self.module)

    def draw(self, color=COLOR_YELLOW, width=None):
        """
            Нарисовать вектор
        """
        width = width if width else self.width
        line(start_point=self.start_point, end_point=self.end_point, color=color, width=width)

    def is_tiny(self):
        """
            Очень маленький вектор?
        """
        return self.module <= 3

    def multiply(self, factor):
        """
            Умножить вектор на скалярное число
        """
        self.dx *= factor
        self.dy *= factor
        self.module = self._determine_module()

    def rotate(self, angle):
        """
            Повернуть вектор на угол
        """
        new_angle = self.angle + angle
        self.dx = math.cos(new_angle) * self.module
        self.dy = math.sin(new_angle) * self.module
        self.module = self._determine_module()

    @property
    def length(self):
        return self.module