test = {
  'name': 'Question 6a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(song_and_streams.columns.values) == set(np.array(["song name", "number of streams"]))
          True
          >>> song_and_streams.shape[0] == 6
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
