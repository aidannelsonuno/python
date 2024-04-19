class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        self.__status = False if self.__status else True
        
    def mute(self):
        if self.__status:
            self.__muted = False if self.__muted else True

    def channel_up(self):
        if self.__status:
            self.__channel += 1 if self.__channel < self.MAX_CHANNEL else self.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__channel -= 1 if self.__channel > self.MIN_CHANNEL else self.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        true_volume = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {true_volume}"


    #test
