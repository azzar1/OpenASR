{
  'includes': [
    '../../common.gyp'
  ],

  'targets': [
    {
      'target_name': 'utils',
      'type': '<(library)',
      'sources': [
        'logging/Logger.cpp',
        'logging/LoggingWriter.cpp'
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '.',
        ],
      },
    }
  ]
}