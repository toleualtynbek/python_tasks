class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def Result(self, weight=35, thick=7):
        print(f'Масса асфальта: {(self._length * self._width * weight * thick)}')

road_1 = Road(7000, 40)
print(road_1.Result())
