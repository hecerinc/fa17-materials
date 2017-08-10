test = {
  'name': 'Question 9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> simple_mag_angle = mag_angle(gradient(simple_image_grayscale))
          >>> isinstance(simple_mag_angle, list)
          True
          >>> simple_mag_angle[0].shape == simple_mag_angle[1].shape == (1, 1)
          True
          >>> np.allclose(simple_mag_angle[0], np.array([[ 0.19213371]]))
          True
          >>> np.allclose(simple_mag_angle[1], np.array([[ 1.19676548]]))
          True

          >>> mag_chunk = np.array([[ 0.00326797,  0.00065359,  0.00130719,  0.        ,  0.00261438],
          ...    [ 0.00326797,  0.00065359,  0.00130719,  0.        ,  0.00261438],
          ...    [ 0.00326797,  0.00065359,  0.00130719,  0.        ,  0.00261438],
          ...    [ 0.00333269,  0.00078552,  0.0013779 ,  0.00087146,  0.00262344],
          ...    [ 0.00227458,  0.00048716,  0.00089828,  0.0011109 ,  0.00132522]])
          >>> angle_chunk = np.array([[ 3.14159265,  3.14159265,  0.        ,  0.        ,  3.14159265],
          ...    [ 3.14159265,  3.14159265,  0.        ,  0.        ,  3.14159265],
          ...    [ 3.14159265,  3.14159265,  0.        ,  0.        ,  3.14159265],
          ...    [-2.94419709, -2.55359005, -0.32175055, -1.57079633, -3.05845142],
          ...    [-2.85013586, -2.67794504, -0.24497866, -1.37340077,  2.97644398]])
          >>> im5_mag_angle[0].shape == (298, 398)
          True
          >>> np.allclose(im5_mag_angle[0][50:55, 50:55], mag_chunk)
          True
          >>> np.allclose(im5_mag_angle[1][50:55, 50:55], angle_chunk)
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
