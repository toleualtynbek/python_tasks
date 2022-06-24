class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Star drawing with {self.title} pen!")

class Pencil(Stationery):
    def draw(self):
        print(f"Star drawing with {self.title} pencil!")

class Marker(Stationery):
    def draw(self):
        print(f"Star drawing with {self.title} marker!")

stat_1 = Stationery()
stat_1.draw()
pen = Pen("Parker")
pen.draw()

