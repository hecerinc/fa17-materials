test = {
  'name': 'Question 9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> top_2017_songs.shape[0] == 2
          True
          >>> set(top_2017_songs.index) == {'Thinking Out Loud', 'One Dance'}
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
