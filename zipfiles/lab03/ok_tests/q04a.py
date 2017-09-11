test = {
  'name': 'Question 4a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(calls["hour"]) == set(range(24))
          True
          >>> list(calls["hour"][:5]) == [6, 8, 18, 17, 18]
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
