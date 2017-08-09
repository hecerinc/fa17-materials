test = {
  'name': 'Question 2a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(richest, Table)
          True
          >>> richest.num_rows == 10
          True
          >>> np.round(richest.column(2).mean()) == 447808
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
