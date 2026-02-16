import unittest

from src.television_system.television import TelevisionSystem


class TestTelevision(unittest.TestCase):

    def setUp(self):
        self._my_television = TelevisionSystem()


    def test_tv_is_off_upon_creation(self):
        tv_status = self._my_television.get_tv_status()
        self.assertEqual(tv_status, "TV is Off")


    def test_tv_volume_is_zero_upon_creation(self):
        tv_volume = self._my_television.get_tv_volume()
        self.assertEqual(tv_volume, 0)

    def test_tv_comes_on_when_switched_on(self):
        self._my_television.turn_on_tv()
        tv_status = self._my_television.get_tv_status()

        self.assertEqual(tv_status,"TV is On")


    def test_tv_turns_off_after_turning_it_on(self):
        self.assertEqual("TV is Off",self._my_television.get_tv_status())
        self._my_television.turn_on_tv()
        tv_status = self._my_television.get_tv_status()

        self.assertEqual(tv_status,"TV is On")

        self._my_television.turn_off_tv()
        tv_second_status = self._my_television.get_tv_status()

        self.assertEqual(tv_second_status,"TV is Off")


    def test_that_upon_creation_tv_channel_is_at_1(self):
        self._my_television.turn_on_tv()
        tv_channel = self._my_television.get_tv_channel()

        self.assertEqual(1,tv_channel)

    def test_previous_channel_decreases(self):
        self._my_television.turn_on_tv()
        self._my_television.next_channel()
        self._my_television.next_channel()

        self.assertEqual(self._my_television.get_tv_channel(), 3)

        self._my_television.previous_channel()
        self.assertEqual(self._my_television.get_tv_channel(), 2)


    def test_that_tv_volume_increases(self):
        self._my_television.turn_on_tv()
        tv_status = self._my_television.get_tv_status()
        tv_volume = self._my_television.get_tv_volume()

        self.assertEqual(tv_status,"TV is On")
        self.assertEqual(tv_volume,0)

        self._my_television.increase_volume()

        tv_second_volume = self._my_television.get_tv_volume()
        print(tv_second_volume)
        self.assertEqual(tv_second_volume,1)



    def test_that_tv_volume_decreases(self):
        self._my_television.turn_on_tv()
        tv_status = self._my_television.get_tv_status()
        tv_volume = self._my_television.get_tv_volume()

        self.assertEqual(tv_status, "TV is On")
        self.assertEqual(tv_volume, 0)


        for count in range (3):
            self._my_television.increase_volume()

        tv_second_volume = self._my_television.get_tv_volume()
        self.assertEqual(tv_second_volume, 3)

        self._my_television.decrease_volume()

        self.assertEqual(self._my_television.get_tv_volume(),2)


    def test_tv_does_not_increase_more_than_100(self):
        self._my_television.turn_on_tv()
        self.assertEqual(self._my_television.get_tv_status(),"TV is On")

        for count in range(100):
            self._my_television.increase_volume()

        tv_volume = self._my_television.get_tv_volume()
        self.assertEqual(tv_volume, 100)

        with self.assertRaises(ValueError):
            self._my_television.increase_volume()


    def test_tv_does_not_decrease_less_than_0(self):
        self._my_television.turn_on_tv()
        tv_volume = self._my_television.get_tv_volume()

        self.assertEqual(tv_volume, 0)

        self._my_television.increase_volume()
        self._my_television.increase_volume()

        self._my_television.decrease_volume()
        self._my_television.decrease_volume()

        with self.assertRaises(ValueError):
            self._my_television.decrease_volume()


    def test_that_if_tv_is_volume_will_not_increase(self):

        tv_status = self._my_television.get_tv_status()

        self.assertEqual(tv_status, "TV is Off")

        self._my_television.increase_volume()
        self._my_television.increase_volume()
        self._my_television.increase_volume()

        tv_volume = self._my_television.get_tv_volume()

        self.assertEqual(tv_volume, 0)


    def test_that_volume_drops_to_default_if_tv_is_turned_off(self):
        self._my_television.turn_on_tv()

        self._my_television.increase_volume()
        self._my_television.increase_volume()
        self._my_television.increase_volume()

        self.assertEqual(self._my_television.get_tv_volume(),3)

        self._my_television.turn_off_tv()
        self.assertEqual(self._my_television.get_tv_volume(),0)

    def test_next_channel_changes_the_channel_forward(self):
        self._my_television.turn_on_tv()
        self.assertEqual(self._my_television.get_tv_channel(), 1)

        self._my_television.next_channel()
        self._my_television.next_channel()

        self.assertEqual(self._my_television.get_tv_channel(), 3)


    def test_next_channel_wraps_back_to_1_after_50(self):
        self._my_television.turn_on_tv()

        for count in range(49):
            self._my_television.next_channel()

        self.assertEqual(self._my_television.get_tv_channel(), 50)

        self._my_television.next_channel()
        self.assertEqual(self._my_television.get_tv_channel(), 1)


    def test_that_previous_chanel_changes_channel_from_1_to_50(self):
        self._my_television.turn_on_tv()
        self.assertEqual(self._my_television.get_tv_channel(), 1)

        self._my_television.previous_channel()
        self.assertEqual(self._my_television.get_tv_channel(), 50)

    def test_channel_resets_to_1_when_tv_is_turned_off(self):
        self._my_television.turn_on_tv()
        self._my_television.next_channel()
        self._my_television.next_channel()

        self.assertEqual(self._my_television.get_tv_channel(), 3)

        self._my_television.turn_off_tv()
        self.assertEqual(self._my_television.get_tv_channel(), 1)


if __name__ == '__main__':
    unittest.main()
