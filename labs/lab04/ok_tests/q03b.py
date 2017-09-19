
test = {
  'name': 'q03b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> np.corrcoef(df['trans_lit'], df['trans_inc'])[0,1] > 0.7
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
