import pytest
from television import *


class Test:
    def setup_method(self):
        self.tv1 = Television()
        self.tv2 = Television()
        self.tv3 = Television()
        self.tv4 = Television()

    def teardown_method(self):
        del self.tv1
        del self.tv2
        del self.tv3
        del self.tv4

    def test_init(self):
        assert string_compare(self.tv1)

    def test_power(self):
        assert string_compare(self.tv1)
        self.tv2.power()
        assert string_compare(self.tv2, status=True)
        self.tv3.power()
        self.tv3.power()
        assert string_compare(self.tv3)

    def test_mute(self):
        self.tv1.mute()
        assert string_compare(self.tv1)
        self.tv2.power()
        self.tv2.volume_up()
        assert string_compare(self.tv2, status=True, volume=1)
        self.tv3.power()
        self.tv3.volume_up()
        self.tv3.mute()
        assert string_compare(self.tv3, status=True)
        self.tv4.power()
        self.tv4.volume_up()
        self.tv4.mute()
        self.tv4.power()
        assert string_compare(self.tv4)

    def test_channel_up(self):
        self.tv1.channel_up()
        assert string_compare(self.tv1)
        self.tv2.power()
        self.tv2.channel_up()
        assert string_compare(self.tv2, status=True, channel=1)
        self.tv3.power()
        for i in range(6):
            self.tv3.channel_up()
        assert string_compare(self.tv3, status=True, channel=2)

    def test_channel_down(self):
        self.tv1.channel_down()
        assert string_compare(self.tv1)
        self.tv2.power()
        self.tv2.channel_down()
        assert string_compare(self.tv2, status=True, channel=3)
        self.tv3.power()
        for i in range(6):
            self.tv3.channel_down()
        assert string_compare(self.tv3, status=True, channel=2)

    def test_volume_up(self):
        self.tv1.volume_up()
        assert string_compare(self.tv1)
        self.tv2.power()
        self.tv2.volume_up()
        assert string_compare(self.tv2, status=True, volume=1)
        self.tv3.power()
        self.tv3.volume_up()
        self.tv3.mute()
        self.tv3.volume_up()
        assert string_compare(self.tv3, status=True, volume=2)
        self.tv4.power()
        for i in range(6):
            self.tv4.volume_up()
        assert string_compare(self.tv4, status=True, volume=2)

    def test_volume_down(self):
        self.tv1.volume_down()
        assert string_compare(self.tv1)
        self.tv2.power()
        self.tv2.volume_down()
        assert string_compare(self.tv2, status=True, volume=0)
        self.tv3.power()
        for i in range(2):
            self.tv3.volume_up()
        self.tv3.volume_down()
        assert string_compare(self.tv3, status=True, volume=1)
        self.tv4.power()
        for i in range(2):
            self.tv4.volume_up()
        self.tv4.mute()
        self.tv4.volume_down()
        assert string_compare(self.tv4, status=True, volume=1)



def string_compare(given, status=False, channel=0, volume=0):
    return given.__str__() == f"Power = {status}, Channel = {channel}, Volume = {volume}"