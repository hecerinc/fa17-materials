test = {
  'name': 'Question 5a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> list(calls["road"][:5]) == ['LE CONTE AVE', 'SHATTUCK AVE', 'UNIVERSITY AVE', 'SEVENTH ST', 'PARKSIDE DR']
          True
          >>> ascii_sum(calls['road'].dropna())
          4458018
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r'''
      >>> def ascii_sum(ans):
      ...     return sum([sum(map(ord, s.strip())) for s in ans])
      ''',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
