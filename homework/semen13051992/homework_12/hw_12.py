class Bouquet:

    def __init__(self, name, color, stem_length, freshness, price, lifetime):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.price = price
        self.lifetime = lifetime

    def __str__(self):
        return f"{self.name} {self.color} {self.price}р,"

    def __repr__(self):
        return f"{self.name}({self.color}, {self.price}р)"


class Lily(Bouquet):
    def __init__(self, name, color, stem_length, freshness, price, lifetime):
        super().__init__( name, color, stem_length, freshness, price, lifetime)


class Violet(Bouquet):
    def __init__(self, name, color, stem_length, freshness, price, lifetime):
        super().__init__( name, color, stem_length, freshness, price, lifetime)


class Tulip(Bouquet):
    def __init__(self, name, color, stem_length, freshness, price, lifetime):
        super().__init__(name, color, stem_length, freshness, price, lifetime)


class Gladioli(Bouquet):
    def __init__(self, name, color, stem_length, freshness, price, lifetime):
        super().__init__(name, color, stem_length, freshness, price, lifetime)


class Rose(Bouquet):
    def __init__(self, name, color, stem_length, freshness, price, lifetime):
        super().__init__(name, color, stem_length, freshness, price, lifetime)


flower_1 = Lily('Лилия', 'Белый', 50, 'fresh', 100, 5)
flower_2 = Violet('Фиолент','Фиолетовый', 50, 'fresh', 80, 7)
flower_3 = Tulip('Тюльпан','Красный', 50, 'fresh', 110, 6)
flower_4 = Gladioli('Гладиолус','Синий', 50, 'fresh', 90, 8)
flower_5 = Rose('Роза','Желтый', 50, 'fresh', 120, 7)

bouquet = [flower_1, flower_2, flower_3, flower_4, flower_5]


class Bouquet:
    def __init__(self, flower):
        self.flower = flower

    def bouquet_price(self):
        return sum(x.price for x in self.flower)

    def avg_lifetime(self):
        return sum(x.lifetime for x in self.flower) / len(self.flower)

    def above_avg(self):
        avg_life = bouquets.avg_lifetime()
        return [x.name for x in self.flower if x.lifetime > avg_life]

    def price_avg(self):
        return sum(x.price for x in self.flower) / len(self.flower)

    def above_price_avg(self):
        avg_price = bouquets.price_avg()
        return [x.name for x in self.flower if x.price > avg_price]

    def below_price_avg(self, tolerance=0):
        return [x.name for x in self.flower if x.price < bouquets.price_avg()]

    def color_white(self):
        return [x.name for x in self.flower if x.color == 'Белый']

    def color_red(self):
        return [x.name for x in self.flower if x.color == 'Красный']


bouquets = Bouquet(bouquet)

print(bouquet)
print(f"Стоимость букета: {bouquets.bouquet_price()} р.")
print(f"Среднее время жизни цветов: {bouquets.avg_lifetime()} дней.")
print(f"Цветы время жизни которых выше среднего {bouquets.avg_lifetime()} дней: {bouquets.above_avg()}")
print(f"Средняя стоимость цветов : {bouquets.price_avg()}р")
print(f"Цветы стоимость которых выше средней цены {bouquets.price_avg()}р : {bouquets.above_price_avg()}")
print(f"Цветы стоимость которых ниже средней цены {bouquets.price_avg()}р : {bouquets.below_price_avg()}")
print(f"Цветы цвет которых Белый : {bouquets.color_white()}")
print(f"Цветы цвет которых Красный : {bouquets.color_red()}")