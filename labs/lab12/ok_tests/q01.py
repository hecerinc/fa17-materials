
test = {
  'name': 'q01',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> np.allclose(examples.mean(), 0.13885355)
True
>>> np.allclose(examples.std(), 0.31703091)
True
>>> len(images) == 10 
True
>>> np.allclose(np.array([x.mean() for x in images]), np.array([ 0.15441678,  0.11100941,  0.1077331 ,  0.11536616,  0.1914316 , 0.16284515,  0.08603442,  0.07767608,  0.25953886,  0.12248399]))
True
>>> 

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
