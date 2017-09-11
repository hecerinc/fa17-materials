test = {
  'name': 'Question 5c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> (calls["road"].value_counts()["SHATTUCK AVE"] > 400) and (calls["road"].value_counts()["SHATTUCK AVE"] < 420 )
          True
          >>> list(filter(lambda x:x.find("AVENUE")>=0,calls["road"])) == []
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
