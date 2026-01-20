class Flowers:

    def __init__(self, name, color, stem_length, freshness, price, lifetime):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.price = price
        self.lifetime = lifetime

    def __str__(self):
        return f"{self.name} ({self.color} {self.price}р)"

    def __repr__(self):
        return f"{self.name} ({self.color}, {self.price}р)"


class Lily(Flowers):
    def __init__(self, color, stem_length, freshness, price, lifetime):
        super().__init__('Лилия', color, stem_length, freshness, price, lifetime)


class Violet(Flowers):
    def __init__(self, color, stem_length, freshness, price, lifetime):
        super().__init__('Фиолент', color, stem_length, freshness, price, lifetime)


class Tulip(Flowers):
    def __init__(self, color, stem_length, freshness, price, lifetime):
        super().__init__('Тюльпан', color, stem_length, freshness, price, lifetime)


class Gladioli(Flowers):
    def __init__(self, color, stem_length, freshness, price, lifetime):
        super().__init__('Гладиолус', color, stem_length, freshness, price, lifetime)


class Rose(Flowers):
    def __init__(self, color, stem_length, freshness, price, lifetime):
        super().__init__('Роза', color, stem_length, freshness, price, lifetime)


flower_1 = Lily('Белый', 40, 'fresh', 100, 5)
flower_2 = Violet('Фиолетовый', 50, 'fresh', 80, 7)
flower_3 = Tulip('Красный', 45, 'fresh', 110, 6)
flower_4 = Gladioli('Синий', 43, 'fresh', 90, 8)
flower_5 = Rose('Желтый', 48, 'fresh', 120, 7)

flowers = [flower_1, flower_2, flower_3, flower_4, flower_5]


class Bouquet:
    def __init__(self, flower):
        self.flower = flower

    def bouquet_price(self):
        return sum(x.price for x in self.flower)

    def avg_lifetime(self):
        return sum(x.lifetime for x in self.flower) / len(self.flower)

    def above_avg(self):
        avg_life = [x for x in self.flower if x.lifetime > bouquets.avg_lifetime()]
        avg = sorted(avg_life, key=lambda x: x.name)
        return avg

    def price_avg(self):
        return sum(x.price for x in self.flower) / len(self.flower)

    def above_price_avg(self):
        avg_price = [x for x in self.flower if x.price > bouquets.price_avg()]
        return bouquets.sort_name(avg_price)

    def below_price_avg(self):
        below_price = [x for x in self.flower if x.price < bouquets.price_avg()]
        return bouquets.sort_name(below_price)

    def color_white(self):
        color = [x for x in self.flower if x.color == 'Белый']
        return bouquets.sort_color(color)

    def color_red(self):
        color = [x for x in self.flower if x.color == 'Красный']
        return bouquets.sort_color(color)

    def sort_name(self, arg):
        return sorted(arg, key=lambda x: x.name)

    def sort_color(self, arg):
        return sorted(arg, key=lambda x: x.color)

    def sort_stem_length(self, arg):
        return sorted(arg, key=lambda x: x.stem_length)

    def sort_price(self, arg):
        return sorted(arg, key=lambda x: x.price)


bouquets = Bouquet(flowers)

print(flowers)
print(f"Стоимость букета: {bouquets.bouquet_price()}р.")
print(f"Среднее время жизни цветов: {bouquets.avg_lifetime()} дней.")
print(f"Цветы время жизни которых выше среднего {bouquets.avg_lifetime()} дней: {bouquets.above_avg()}")
print(f"Средняя стоимость цветов: {bouquets.price_avg()}р")
print(f"Цветы стоимость которых выше средней цены {bouquets.price_avg()}р: {bouquets.above_price_avg()}")
print(f"Цветы стоимость которых ниже средней цены {bouquets.price_avg()}р: {bouquets.below_price_avg()}")
print(f"Цветы цвет которых Белый: {bouquets.color_white()}")
print(f"Цветы цвет которых Красный: {bouquets.color_red()}")
print(f"Цветы отсортированные по длине стебля: {bouquets.sort_stem_length(flowers)}")
print(f"Цветы отсортированные по стоимости: {bouquets.sort_price(flowers)}")
print(f"Цветы отсортированные по названию: {bouquets.sort_name(flowers)}")
