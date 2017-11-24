
test = {
  'name': 'q01',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> d = pd.read_csv('q01.csv')
>>> len(d) == 505
True
>>> d["value"].sum() == 509040
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
