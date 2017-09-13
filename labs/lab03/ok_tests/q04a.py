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
          >>> np.allclose(calls['hour'].mean(), 13.52451)
          True
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
