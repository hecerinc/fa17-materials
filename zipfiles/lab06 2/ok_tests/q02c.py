
test = {
  'name': 'q02c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> abs_loss(2, 1) == 1
True
>>> abs_loss(-2, 1) == 3
True
>>> abs_loss(1, -3) == 4 
True
>>> np.linalg.norm(abs_loss(np.array([1,2]), np.array([-3,3])) - np.array([4, 1]), ord=1) == 0.0
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
