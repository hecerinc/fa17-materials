test = {
  'name': 'Question 3a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(calls["Day"]) == {'Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tueday', 'Wedesday'}
          True
          >>> list(calls["Day"][:5]) == ['Sunday', 'Thursday', 'Thursday', 'Thursday', 'Tueday']
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
