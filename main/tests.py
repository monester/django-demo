from django.test import TestCase

# Create your tests here.
class TestMain(TestCase):
    def test_fail_math(self):
        assert 1 + 2 == 3

    def test_math(self):
        assert 1 + 1 == 2

    def test_false(self):
        assert False
