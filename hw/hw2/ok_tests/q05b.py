test = {
  'name': 'Question 5b',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pd.value_counts(ins['type'])['complaint'] == 1
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
