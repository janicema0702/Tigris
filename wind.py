# TODO: Can create synthetic wind profiles for testing in RocketPy

class Gust:

    def __init__(self, speed, height, width):
        self.speed = speed
        self.start = height - width / 2
        self.end = height + width / 2
        self.width = width

    def get_wind_speed(self, h):
        if h < self.start or h > self.end:
            return 0
        elif h >= self.start and h <= self.start + self.speed * 25 / 9:
            return (h - self.start) * 9 / 25
        elif h >= self.end - self.speed * 25 / 9 and h <= self.end:
            return (self.end - h) * 9 / 25
        else:
            return self.speed

class WindProfile:

    def __init__(self, gusts):
        self.gusts = gusts

    def get_wind_speed(self, h):
        wind = 19.7*h/5300 + 10.9 # Linearly increasing wind speed, low altitudes (h < 5 km)
        for gust in self.gusts:
            wind += gust.get_wind_speed(h)
        return wind
    
agust = Gust(15, 310, 100)