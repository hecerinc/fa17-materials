
test = {
  'name': 'q01d',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> ("|" not in regx4)
True
>>> (re.match(regx4, '1 file found.') is not None) 
True
>>> (re.match(regx4, '2 files found.') is not None) 
True
>>> (re.match(regx4, '5 files found.') is not None) 
True
>>> (re.match(regx4, "No files found.") is None)
True
>>> 

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
