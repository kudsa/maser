
from tkinter import *
 
# Создаем окно
root = Tk()
# Устанавливаем название окна
root.title("PythonicWay Snake")
 
# Запускаем окно
root.mainloop()
# ширина экрана
WIDTH = 800
# высота экрана
HEIGHT = 600

# Размер сегмента змейки

SEG_SIZE = 20

# Переменная отвечающая за состояние игры

IN_GAME = True
# создаем экземпляр класса Canvas (его мы еще будем использовать) и заливаем все зеленым цветом
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()
# Наводим фокус на Canvas, чтобы мы могли ловить нажатия клавиш
c.focus_set()
class Snake(object):
    def __init__(self, segments):
        self.segments = segments
         
        # список доступных направлений движения змейки
        self.mapping = {"Down": (0, 1), "Up": (0, -1),
                                "Left": (-1, 0), "Right": (1, 0) }
        # изначально змейка двигается вправо
        self.vector = self.mapping["Right"]
     
    def move(self):
         """ Двигает змейку в заданном направлении """
          
         # перебираем все сегменты кроме первого
         for index in range(len(self.segments)-1):
              segment = self.segments[index].instance
              x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
              # задаем каждому сегменту позицию сегмента стоящего после него
              c.coords(segment, x1, y1, x2, y2)
          
         # получаем координаты сегмента перед "головой"
         x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
          
         # помещаем "голову" в направлении указанном в векторе движения
         c.coords(self.segments[-1].instance,
                       x1 + self.vector[0]*SEG_SIZE,
                       y1 + self.vector[1]*SEG_SIZE,
                       x2 + self.vector[0]*SEG_SIZE,
                       y2 + self.vector[1]*SEG_SIZE)
     
    def change_direction(self, event):
        """ Изменяет направление движения змейки """
 
        # event передаст нам символ нажатой клавиши
        # и если эта клавиша в доступных направлениях 
        # изменяем направление
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
 
    def add_segment(self):
        """ Добавляет сегмент змейке """
 
        # определяем последний сегмент
        last_seg = c.coords(self.segments[0].instance)
         
        # определяем координаты куда поставить следующий сегмент
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
         
        # добавляем змейке еще один сегмент в заданных координатах
        self.segments.insert(0, Segment(x, y))  
# создаем набор сегментов
segments = [Segment(SEG_SIZE, SEG_SIZE),
            Segment(SEG_SIZE*2, SEG_SIZE),
            Segment(SEG_SIZE*3, SEG_SIZE)]
 
# собственно змейка
s = Snake(segments)
def create_block():
    """ Создает блок в случайной позиции на карте """
    global BLOCK
    posx = SEG_SIZE * (random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE))
    posy = SEG_SIZE * (random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE))
     
    # блок это кружочек красного цвета
    BLOCK = c.create_oval(posx, posy,
                          posx + SEG_SIZE,
                          posy + SEG_SIZE,
                          fill="red")
c.bind("<KeyPress>", s.change_direction)