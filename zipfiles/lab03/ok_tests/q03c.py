test = {
  'name': 'Question 3c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(set(answer3c).intersection({'LIQUOR LAW VIOLATION', 'DRUG VIOLATION'}))>0
          True
          >>> len(set(answer3c).union({'LIQUOR LAW VIOLATION', 'DRUG VIOLATION'})) == 2
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
