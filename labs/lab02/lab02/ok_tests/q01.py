test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(fruit_info["rank"]) == {1, 2, 4, 3}
          True
          >>> set(fruit_info.columns.values) == set(np.array(["color", "fruit", "rank"]))
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
