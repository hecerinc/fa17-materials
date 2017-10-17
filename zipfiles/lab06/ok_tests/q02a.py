
test = {
  'name': 'q02a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> squared_loss(2, 1) == 1
True
>>> squared_loss(2, 0) == 4 
True
>>> squared_loss(5, 1) == 16
True
>>> np.sum((squared_loss(np.array([5, 6]), np.array([1, 1])) - np.array([16, 25]))**2) == 0.0
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
