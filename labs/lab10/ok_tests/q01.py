
test = {
  'name': 'q01',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> len(least_squares_est(X, Y)) == 2
True
>>> np.isclose(np.linalg.norm(least_squares_est(X, Y) - np.array([-2.5883789105125632,  0.6953174687410612])), 0.0)
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
