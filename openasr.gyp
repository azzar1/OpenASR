{
  'includes': [
    './common.gyp',
  ],

  'targets': [
    {
      'target_name': 'ALL',
      'type': 'none',
      'dependencies': [
        './src/src.gyp:src',
        './tests/tests.gyp:openasr_unittests'
      ]
    }
  ]
}