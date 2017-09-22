test = {
  'name': 'Question 3c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ascii_sum(answer3c) == 2492
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
