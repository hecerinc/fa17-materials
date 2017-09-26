
test = {
  'name': 'q01a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> ("|" not in regx1)
True
>>> (re.match(regx1, "abc") is not None) 
True
>>> (re.match(regx1, "abcde") is not None) 
True
>>> (re.match(regx1, "abcdefg") is not None)
True

""",
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
