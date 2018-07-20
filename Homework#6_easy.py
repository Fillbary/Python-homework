# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class Triangle:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.A = round(math.sqrt(int((self.y1 - self.x1)**2 + (self.y2 - self.x2)**2)))
        self.B = round(math.sqrt(int((self.z1 - self.y1)**2 + (self.z2 - self.y2)**2)))
        self.C = round(math.sqrt(int((self.x1 - self.z1)**2 + (self.x2 - self.z2)**2)))
    # Объявляенм метод находящий периметр
    def perimetr(self):
        self.perimetr = (self.A + self.B + self.C)
        return (self.perimetr)
    # Объявляем метод который находит площадь с помощью p
    def area(self):
        self.p = (self.A + self.B + self.C)/2
        self.area = round(math.sqrt(self.p*(self.p-self.A)*(self.p-self.B)*(self.p-self.C)))
        return (self.area)
    # Объявдяем метод который находит высоту зная периметр и площадь
    def heigh(self):
        self.heigh = round(int((self.area*2)/self.A))
        return (self.heigh)

my_tri = Triangle(2,0,3,3,1,4)
print("Длинна сторон A = {}, B = {}, C = {}".format(my_tri.A, my_tri.B, my_tri.C))
print("Периметр треугольника равен {}".format(my_tri.perimetr()))
print("Площадь равна {}".format(my_tri.area()))
print("Высота треугольника равна {}".format(my_tri.heigh()))
        


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapez:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy

        self.AB = bx-ax, by-ay, math.sqrt((bx-ax)**2 + (by-ay)**2)
        self.BC = cx-bx, cy-by, math.sqrt((cx-bx)**2 + (cy-by)**2)
        self.CD = dx-cx, dy-cy, math.sqrt((dx-cx)**2 + (dy-cy)**2)
        self.AD = dx-ax, dy-ay, math.sqrt((dx-ax)**2 + (dy-ay)**2)

    # проверка 
    def TrueTrapez(self): 
        if (self.BC[0]*self.AD[1] - self.BC[1]*self.AD[0] == 0) & (self.AB[2] == self.CD[2]):
            return True 
        else:
            return False

    def len(self): 
        return self.AB[2], self.BC[2], self.CD[2], self.AD[2]

    def P(self): 
        return self.AB[2] + self.BC[2] + self.CD[2] + self.AD[2]

    def S(self): 
        return 0.5 * (self.BC[2]+self.AD[2]) * math.sqrt(self.AB[2]**2 - \
              (((self.AD[2]-self.BC[2])**2 + self.AB[2]**2 - self.CD[2]**2) / \
                (2*(self.AD[2]-self.BC[2])))**2)



trapez = Trapez(2, 2, 8, 8, 4, 4, 7, 0)
if not trapez.TrueTrapez():
    print("Это трапеция не равнобедренная")
else:
    print("Длина сторон AB = {}, BC = {}, CD = {}, AD = {}.\
        format(round(tr.AB[2],2), round(tr.BC[2],2), round(tr.CD[2],2), round(tr.AD[2],2)))
    print('Периметр равен {}'.format(round(trapez.P(),2)))
    print('Площадь равна {}'.format(round(trapez.S(),2)))
