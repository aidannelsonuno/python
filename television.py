class Television:
    '''
    A class for representing the functions of a television.
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        A method for initializing an instance of Television.
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        '''
        A method to toggle television power between on and off.
        '''
        self.__status = False if self.__status else True
        
    def mute(self) -> None:
        '''
        A method to toggle television muting between on and off.
        '''
        if self.__status:
            self.__muted = False if self.__muted else True

    def channel_up(self) -> None:
        '''
        A method to cycle the television channel in the positive direction.
        '''
        if self.__status:
            self.__channel = self.__channel + 1 if self.__channel < self.MAX_CHANNEL else self.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        A method to cycle the television channel in the negative direction.
        '''
        if self.__status:
            self.__channel = self.__channel - 1 if self.__channel > self.MIN_CHANNEL else self.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        A method to increase the television volume if it isn't at its maximum.
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        A method to decrease the television volume if it isn't at its minimum.
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        A method to display the power, channel and volume aspects of the television.
        :return: Television's power, channel, and volume values.
        '''
        true_volume = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {true_volume}"
