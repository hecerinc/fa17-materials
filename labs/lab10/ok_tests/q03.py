
test = {
  'name': 'q03',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> np.isclose(rmse(np.array([1.2, 2.3]), X, Y), 4.7053762514545463, rtol=1e-2, atol=1e-2)
True
>>> np.isclose(rmse(theta_true, X, Y), 4.0265834813515395, rtol=1e-2, atol=1e-2)
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
