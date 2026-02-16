

class TelevisionSystem:
    def __init__(self):
        self.__tv = "TV is Off"
        self.__volume = 0
        self.__max_volume = 100
        self.__tv_channel = 1
        self.__tv_max_channel= 50


    def get_tv_status(self):
        return self.__tv

    def get_tv_volume(self):
        return self.__volume

    def turn_on_tv(self):
        self.__tv = "TV is On"

    def turn_off_tv(self):
        self.__volume = 0
        self.__tv_channel = 1
        self.__tv = "TV is Off"

    def get_tv_channel(self):
        return self.__tv_channel

    def increase_volume(self):
        if self.__tv == "TV is Off":
            return None
        if self.__volume < self.__max_volume:
            self.__volume = self.__volume + 1
        else:
            raise ValueError("Volume is the max level")

    def decrease_volume(self):
        if self.__tv == "TV is Off":
            return None
        if self.__volume > 0:
            self.__volume = self.__volume - 1

        else:
            raise ValueError("Volume cannot be lower than 0")


    def next_channel(self):
        if self.__tv == "TV is Off":
            return None

        if self.__tv_channel < self.__tv_max_channel:
            self.__tv_channel = self.__tv_channel + 1

        elif self.__tv_channel == self.__tv_max_channel:
            self.__tv_channel = 1

    def previous_channel(self):
        if self.__tv == "TV is Off":
            return None
        if self.__tv_channel == 1:
            self.__tv_channel = self.__tv_max_channel

        elif self.__tv_channel <= self.__tv_max_channel:
            self.__tv_channel = self.__tv_channel - 1



