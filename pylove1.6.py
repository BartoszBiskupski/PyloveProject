class Czas:
    """Stwórz klasę Czas, której konstruktor (__init__)
    będzie brał trzy opcjonalne argumenty, godzine, minuty,
    sekundy i zapisywal je w odpowiednich zmiennych w klasie."""

    def __init__(self, h=0, mins=0, sec=0):
        self.h = h
        self.mins = mins
        self.sec = sec

    def __str__(self):
#        return "Czas: h = {}m = } s={}".format(self.h, self.mins, self.sec)
        temp = "{}".format(self._get_name())
        for atr in dir(self):
            if not atr.startwith("_") and not callable(getattr(self, atr)):
                temp += "{}{} ".format(atr, getattr(self, atr))
        return temp

    @classmethod
    def _get_name(cls):
        return cls.__name__

    def set_time(self, h = None, mins = None, sec = None):
        self.h = h
        self.mins = mins
        self.sec = sec
        if h:
            self.h = h
        if mins:
            self.mins = mins
        if sec:
            self.sec = sec
            #self.sec = s or self.sec (jako alternatywa)



        def add_time(self, h=None, mins=None, sec=None):
            if s:
                if self.s + s > 59
                    self.mins += 1
                    self.s = self.s +s = 60
                else:
                    self.s += s
            if m:
                self.mins += mins
                if self.mins // 60 >= 1:
                    self.h += self.m //60
                    self.m = self.m % 60
        #
        # get_seconds(self):
        #     pass
        #
        # get_minutes(self):
        #     pass
        #
        # get_hours(self):
        #     pass


class Zegar(Czas):
    def __init__(self, time_format, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time_format = time_format




class DokladnyZegar(Zegar):
    def _init__(self, *args, ms=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.ms = ms
    def set_time(self, ms=None, **kwargs):
        super().set_time(kwargs)
        if ms:
            self.ms = ms

def mojprint():
    pass


zeg = DokladnyZegar('12H', h = 20, ms = 44 mins=44, sec=45)
print(zeg)
