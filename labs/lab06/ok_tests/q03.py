
test = {
  'name': 'q03',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> y = data['tip']
>>> x = data['total_bill']
>>> np.isclose(minimize_average_loss(squared_loss, model, x, y), 0.14373189229218733)
True
>>> np.isclose(minimize_average_loss(abs_loss, model, x, y), 0.14958862353611219)
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
