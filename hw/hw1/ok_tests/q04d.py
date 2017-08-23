test = {
  'name': 'Question 3b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.linalg.inv(A @ B) @ np.array([80, 80, 100])
          array([ 5.5       ,  2.20833333,  1.        ])
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
