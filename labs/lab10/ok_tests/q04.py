
test = {
  'name': 'q04',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> add_const(X).shape == (100, 3)
True
>>> add_const(X)[:,2].sum() == 100.0
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
