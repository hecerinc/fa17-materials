
test = {
  'name': 'q06a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> isinstance(hash_re, str)
True
>>> not re.search(rt_re, 'this')
True
>>> not re.search(rt_re, 'this is the start.')
True
>>> re.search(rt_re, 'rt hi')
True
>>> re.search(rt_re, 'hi rt')
True
>>> re.search(rt_re, 'rt: hello')
True
>>> re.search(rt_re, 'hello rt: @Sam')
True
>>> not re.search(hash_re, '# heya')
True
>>> not re.search(hash_re, '#')
True
>>> re.search(hash_re, '#heya')
True
>>> re.search(hash_re, '#h')
True
>>> re.search(hash_re, 'ds100 is #goals')
True
>>> not re.search(hash_re, 'ds100 is # goals')
True
>>> re.search(hash_re, 'http://google.com')
True
>>> re.search(hash_re, 'https://google.com')
True
>>> re.search(hash_re, 'hihttphello')
True
>>> 
>>> isinstance(hash_or_link, pd.DataFrame)
True
>>> # If you fail this test, you might not be looking everywhere in the string
>>> len(hash_or_link) > 1100
True
>>> '907303264458362880' in hash_or_link.index
True
>>> '907311779331690496' in hash_or_link.index
True
>>> '907588803161939968' in hash_or_link.index
True
>>> '907675638055743489' in hash_or_link.index
True
>>> '907698529606541312' in hash_or_link.index
True
>>> '906828550065582080' not in hash_or_link.index
True
>>> '906828871106002944' not in hash_or_link.index
True
>>> '906829008955957248' not in hash_or_link.index
True
>>> '907579024960098304' not in hash_or_link.index
True
>>> '907592460070768641' not in hash_or_link.index
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
