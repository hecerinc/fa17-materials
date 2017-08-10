test = {
  'name': 'Question 11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test = np.array([[ 0.83333333,  0.83333333,  0.        ],
          ...    [ 0.83333333,  0.83333333,  0.        ],
          ...    [ 0.83333333,  0.83333333,  0.        ]])
          >>> np.allclose(edges(test, 0.1), np.round(test))
          True
          >>> np.allclose(edges(test, 0.5), np.round(test))
          True
          >>> np.allclose(edges(test, 1), np.zeros((3, 3)))
          True

          >>> isinstance(im5_edges, np.ndarray)
          True
          >>> im5_edges.shape == (298, 398)
          True

          >>> edges_chunk = np.array([[ 1.,  0.,  0.,  0.,  1.],
          ...    [ 1.,  0.,  0.,  0.,  1.],
          ...    [ 1.,  0.,  0.,  0.,  1.],
          ...    [ 1.,  0.,  0.,  0.,  1.],
          ...    [ 1.,  0.,  0.,  0.,  0.]])
          >>> np.allclose(im5_edges[20:25, 20:25], edges_chunk)
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
