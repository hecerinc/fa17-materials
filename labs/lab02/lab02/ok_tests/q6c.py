test = {
  'name': 'Question 6c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> popular_songs_small.shape[0] == 4
          True
          >>> set(popular_songs_small.index) == {'One Dance', 'Sorry', 'Closer', 'Decpasito'}
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
