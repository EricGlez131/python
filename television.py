class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.prior = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        this method turn the tv on and off with a boolean value
        :return: a boolean value
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        """
        This method changes the boolean value for __muted and stores a value with the prior volume
        in order to turn the actual volume to zero, it only works if the __status Boolean is true
        :return: a boolean value
        """
        if self.__status:
            self.__muted = not self.__muted
            if self.__volume > 0 and self.__muted:
                self.prior = self.__volume
                self.__volume = 0

    def channel_up(self):
        """
        this method changes the channel by 1 up and if its max it becomes the MIN_CHANNEL just
        like a television, it only works if the __status Boolean is true
        :return: none
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        similar to channel_up this method turn the channel variable down by 1 and if the MIN_CHANNEL it becomes
        the MAX_CHANNEL it only works if the __status Boolean is true
        :return: none
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        this method turn the __volume variable up by one and if __muted status is True it changes it false and get the
        Previous volume before it was changed if it is the MAX_VOLUME  it stays the same,
        it only works if the __status Boolean is true
        :return: none
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.prior
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self):
        """
        what this method does it similar to the volume_up it turn the volume down and also does the same with the __muted
        button and gets the previous volume if the volume is the MIN_VOLUME it stays the same
        it only work if the __status Boolean is true
        :return: none
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.prior
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        this method return the all the values in a string to display it
        :return: str
        """
        return f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]'