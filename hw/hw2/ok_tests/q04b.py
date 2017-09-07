test = {
  'name': 'Question 4b',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> bus_sf_latlong.shape == (24,3)
          True
          >>> bus_sf_latlong['null_lon'].values == [253, 251, 247, 196, 146, 135, 123, 115, 108, 100, 100,  88, 82,  76,  67,  65,  59,  59, 55,  53,  35,  29,  28, 14]
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
