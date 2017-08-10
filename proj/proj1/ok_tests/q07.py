test = {
  'name': 'Question 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> simple_grad = gradient(simple_image_grayscale)
          >>> isinstance(simple_grad, list)
          True
          >>> simple_grad[0].shape == simple_grad[1].shape
          True
          >>> simple_grad[0].shape == (1, 1)
          True
          >>> np.allclose(simple_grad[0], np.array([[ 0.0702]]))
          True
          >>> np.allclose(simple_grad[1], np.array([[ 0.17885]]))
          True

          >>> isinstance(im5_grad, list)
          True
          >>> im5_grad[0].shape == im5_grad[1].shape
          True
          >>> im5_grad[0].shape == (298, 398)
          True

          >>> im5_xgrad_chunk = np.array([[-0.00326797, -0.00065359,  0.00130719,  0.        , -0.00261438],
          ...    [-0.00326797, -0.00065359,  0.00130719,  0.        , -0.00261438],
          ...    [-0.00326797, -0.00065359,  0.00130719,  0.        , -0.00261438],
          ...    [-0.00326797, -0.00065359,  0.00130719,  0.        , -0.00261438],
          ...    [-0.00217865, -0.00043573,  0.00087146,  0.00021786, -0.00130719]])
          >>> im5_ygrad_chunk = np.array([[ 0.00326797,  0.00326797,  0.00348584,  0.00413943,  0.00522876],
          ...    [-0.021598  , -0.02268732, -0.02203373, -0.02072654, -0.01854789],
          ...    [-0.02816331, -0.02881691, -0.02903477, -0.02881691, -0.02838118],
          ...    [-0.01792366, -0.01727007, -0.0177058 , -0.01879512, -0.02053804],
          ...    [-0.00569386, -0.00700105, -0.00700105, -0.00721891, -0.00830824]])
          >>> np.allclose(im5_grad[0][50:55, 50:55], im5_xgrad_chunk)
          True
          >>> np.allclose(im5_grad[1][60:65, 60:65], im5_ygrad_chunk)
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
