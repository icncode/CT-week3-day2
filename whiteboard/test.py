from whiteboard import solution
from unittest import TestCase


class TestWhiteboard(TestCase):

    def test_1(self):
        a_string = 'hello_world'
        result = solution(a_string)
        self.assertEqual(result, 3)

    def test_2(self):
        a_string = 'This is Coding Temple'
        result = solution(a_string)
        self.assertEqual(result, 6)

    def test_3(self):
        a_string = 'Orange you glad I did not say banana'
        result = solution(a_string)
        self.assertEqual(result, 13)

    def test_4(self):
        a_string = 'Can you talk to devops next for me'
        result = solution(a_string)
        self.assertEqual(result, 10)
