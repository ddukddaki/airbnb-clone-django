from rest_framework.test import APITestCase


class TestAmenities(APITestCase):
    def test_two_plus_two(self):
        self.assertEqual(2 + 2, 5, msg="The math is wrong.")
