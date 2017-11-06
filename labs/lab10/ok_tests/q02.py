
test = {
  'name': 'q02',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> np.isclose(correlation(X[:,0], Y), -0.90739849873602996, rtol=1e-2, atol=1e-2)
True
>>> np.isclose(correlation(X[:,1], Y), 0.43225082378347551, rtol=1e-2, atol=1e-2)
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
