
test = {
  'name': 'q01',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> np.isclose(df['lit'].mean(),78.435, rtol=0.01)
True
>>> np.isclose(df['inc'].mean(),7919.251, rtol=0.01)
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
