test = {
  'name': 'Question 2a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ascii_sum(answer2a)
          4304
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
