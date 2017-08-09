test = {
  'name': 'Question 2b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(orgs, Table)
          True
          >>> orgs.num_rows == 7
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
