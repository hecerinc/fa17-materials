test = {
  'name': 'Question 4b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(answer4b) == 3
          True
          >>> np.mean(answer4b) == 15
          True
          >>> np.allclose(np.std(answer4b), 10.614455)
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
