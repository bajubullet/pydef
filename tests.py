import unittest
import pydef


_TEST_CODE = '''import os

def apple():
  print 'apple'

ball = 'ball'

class Cat:
  def dog():
    print 'dog'

print dir(apple)
'''
_EXPECTED_RESULT = [
    ('apple', 'function', None),
    ('Cat', 'class', None),
    ('dog', 'method', 'Cat')]


class TestParseCode(unittest.TestCase):

  def test_parse_code(self):
    self.assertEquals(_EXPECTED_RESULT, pydef.parse_code(_TEST_CODE))

if __name__ == '__main__':
  unittest.main()
