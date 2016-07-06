{
  'includes': [
    '../common.gyp'
  ],

  'targets': [
    {
      'target_name': 'src',
      'type': 'none',
      'dependencies': [
        'utils/utils.gyp:utils'
      ],
      'export_dependent_settings':[
        'utils/utils.gyp:utils'
      ]
    }
  ],
}