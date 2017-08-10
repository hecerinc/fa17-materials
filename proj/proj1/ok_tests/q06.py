test = {
  'name': 'Question 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(blur(simple_image_grayscale), np.ndarray)
          True
          >>> blur(simple_image_grayscale).shape == simple_image_grayscale.shape
          True

          >>> blurred_simple = np.array([
          ...     [ 0.23782222,  0.44444444,  0.65106667],
          ...     [ 0.30117778,  0.38888889,  0.4766    ],
          ...     [ 0.36453333,  0.33333333,  0.30213333]])
          >>> np.allclose(blur(simple_image_grayscale), blurred_simple)
          True
          >>> im5_gray.shape == im5_blurred.shape
          True

          >>> im5_blurred_chunk = np.array([[ 0.56527024,  0.59620706,  0.61276479,  0.61755782,  0.61930074],
          ...    [ 0.56788462,  0.5996929 ,  0.61712209,  0.62147939,  0.62104366],
          ...    [ 0.57137046,  0.60448593,  0.62235085,  0.6288868 ,  0.62627242],
          ...    [ 0.57354911,  0.60579312,  0.62278658,  0.6288868 ,  0.62670815],
          ...    [ 0.57442057,  0.60579312,  0.62147939,  0.62540096,  0.62365804]])
          >>> np.allclose(im5_blurred[20:25, 20:25], im5_blurred_chunk)
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
