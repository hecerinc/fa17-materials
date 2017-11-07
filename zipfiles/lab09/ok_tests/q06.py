
test = {
  'name': 'q06',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> d = pd.read_csv('q06.csv')
>>> len(d) == 213
True
>>> list(d["word"][:10]) == ['spark', 'the', 'to', 'for', 'run', 'and', 'apache', 'a', 'org', 'building']
True
>>> list(d["count"][:10]) == [29, 23, 16, 13, 13, 11, 10, 9, 8, 8]
True
>>> d["count"].sum() == 513
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
