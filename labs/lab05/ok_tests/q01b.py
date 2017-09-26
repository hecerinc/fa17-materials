
test = {
  'name': 'q01b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> ("|" not in regx2)
True
>>> (re.match(regx2, "abc123xyz")is not None) 
True
>>> (re.match(regx2, 'define "123"') is not None) 
True
>>> (re.match(regx2, "var g = 123;") is not None)
True
>>> (re.match(regx2, "var g = 124;") is None)
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
