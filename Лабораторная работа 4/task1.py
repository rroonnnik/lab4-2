class Shape:
    def __init__(self, color: str) -> None:
        self.color = color

    def area(self) -> float:
        return 0.0

    def perimeter(self) -> float:
        return 0.0

    def __str__(self) -> str:
        return f"Фигура цвета {self.color}"

    def __repr__(self) -> str:
        return f"Shape(color='{self.color}')"



class Circle(Shape):
    def __init__(self, color: str, radius: float) -> None:
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        # Перегрузка: расчёт площади круга по формуле πr²
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        # Перегрузка: периметр круга — это длина окружности 2πr
        import math
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        return f"Круг цвета {self.color}, радиус {self.radius}"

    def __repr__(self) -> str:
        return f"Circle(color='{self.color}', radius={self.radius})"



class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float) -> None:
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self) -> float:
        # Перегрузка: площадь прямоугольника — произведение ширины и высоты
        return self.width * self.height

    def perimeter(self) -> float:
        # Перегрузка: периметр прямоугольника — сумма всех сторон
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return f"Прямоугольник цвета {self.color}, {self.width}x{self.height}"

    def __repr__(self) -> str:
        return f"Rectangle(color='{self.color}', width={self.width}, height={self.height})"



if __name__ == "__main__":
    # Write your solution here
    # Создаём объекты разных фигур
    circle = Circle("красный", 5.0)
    rectangle = Rectangle("синий", 4.0, 6.0)

    # Демонстрируем работу методов
    print(circle)  # __str__
    print(repr(circle))  # __repr__
    print(f"Площадь круга: {circle.area():.2f}")  # Перегруженный метод area
    print(f"Периметр круга: {circle.perimeter():.2f}")  # Перегруженный метод perimeter

    print("\n" + "-" * 30 + "\n")

    print(rectangle)  # __str__
    print(repr(rectangle))  # __repr__
    print(f"Площадь прямоугольника: {rectangle.area():.2f}")  # Перегруженный метод area
    print(f"Периметр прямоугольника: {rectangle.perimeter():.2f}")  # Перегруженный метод perimeter