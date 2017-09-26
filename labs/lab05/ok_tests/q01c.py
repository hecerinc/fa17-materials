
test = {
  'name': 'q01c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> ("|" not in regx3)
True
>>> (re.match(regx3, 'can') is not None) 
True
>>> (re.match(regx3, 'fan') is not None) 
True
>>> (re.match(regx3, 'man') is not None) 
True
>>> (re.match(regx3, 'dan') is None) 
True
>>> (re.match(regx3, 'ran') is None) 
True
>>> (re.match(regx3, 'pan') is None)
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
