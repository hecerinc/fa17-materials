test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(bus, pd.DataFrame)
          True
          >>> bus.shape == (6315, 9)
          True
          >>> isinstance(ins, pd.DataFrame)
          True
          >>> ins.shape == (15430, 4)
          True
          >>> isinstance(vio, pd.DataFrame)
          True
          >>> vio.shape == (40936, 3)
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
