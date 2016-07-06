{
  'includes': [
    '../common.gyp',
  ],

  'targets': [
    {
      'target_name': 'openasr_unittests',
      'type': 'executable',
      'dependencies':[
        '../gtest.gyp:gtest',
        '../gtest.gyp:gtest_main',
        '../gmock.gyp:gmock',
        '../gmock.gyp:gmock_main',
        '../src/src.gyp:src'
      ],
      'include_dirs': [
        '.',
      ],
      'sources': [
        'Helpers.cpp',
        'test_logger.cpp',
        'test_main.cpp'
      ],
    },
  ],
}