{
  'target_defaults': {

    'cflags': ['-std=c++11', '-fPIC'],
    'link_settings': {
      'ldflags': ['-pthread']
    },

    'default_configuration': 'Release',

    'configurations': {
      'Debug': {
        'defines': ['DEBUG'],
        'cflags': ['-g3', '-O0']
      },

      'Release': {
        'cflags': ['-O3']
      }
    }
  }
}