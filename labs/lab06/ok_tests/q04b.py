
test = {
  'name': 'q04b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> np.abs(np.std(squared_loss_samples) - 0.004) < 1e-2
True
>>> np.abs(np.mean(squared_loss_samples) - 0.143) < 1e-2
True
>>> np.abs(np.std(abs_loss_samples) - 0.003) < 1e-2
True
>>> np.abs(np.mean(abs_loss_samples) - 0.149) < 1e-2
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
