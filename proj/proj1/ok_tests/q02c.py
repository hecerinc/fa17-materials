test = {
  'name': 'Question 2c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(job_spread, Table)
          True
          >>> job_spread.num_columns == 2
          True
          >>> job_spread.num_rows == 1058
          True
          >>> np.allclose(job_spread.column(1).mean(), 88415.3155)
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
