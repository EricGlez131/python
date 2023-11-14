from pytest import *
from television import *


class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__() == "Power = [False], Channel = [0], Volume = [0]"
        self.tv1.power()
        self.tv1.channel_up()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = [True], Channel = [1], Volume = [2]"

    def test_power(self):
        pass

    def test_mute(self):
        pass

    def test_channel_up(self):
        pass

    def test_channel_down(self):
        pass

    def test_volume_up(self):
        pass

    def test_volume_down(self):
        pass
