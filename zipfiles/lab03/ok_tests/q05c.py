test = {
  'name': 'Question 5c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> list(calls['road_ave'][:5])
          ['LE CONTE AVE', 'SHATTUCK AVE', 'UNIVERSITY AVE', 'SEVENTH ST', 'PARKSIDE DR']
          >>> ascii_sum(calls['road_ave'].dropna())
          4384938
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
