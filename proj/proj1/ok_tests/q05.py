test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(to_grayscale(simple_image), np.ndarray)
          True
          >>> to_grayscale(simple_image).shape == (simple_image.shape[0], simple_image.shape[1])
          True
          >>> np.allclose(to_grayscale(simple_image), simple_image_grayscale)
          True

          >>> im5_gray.shape == (300, 400)
          True
          >>> im5_gray_chunk = np.array([[ 0.61132784,  0.62309255,  0.63093569,  0.63485725,  0.63485725],
          ...    [ 0.61189333,  0.62365804,  0.63150118,  0.63542275,  0.63934431],
          ...    [ 0.60797176,  0.61973647,  0.62757961,  0.63542275,  0.63542275],
          ...    [ 0.6040502 ,  0.6158149 ,  0.62365804,  0.62757961,  0.63150118],
          ...    [ 0.60012863,  0.60797176,  0.61973647,  0.62365804,  0.62365804]])
          >>> np.allclose(im5_gray[10:15, 10:15], im5_gray_chunk)
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
