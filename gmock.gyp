# Copyright (c) 2009 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'includes': [
    './common.gyp',
  ],

  'targets': [
    {
      'target_name': 'gmock',
      'type': 'static_library',
      'dependencies': [
        'gtest.gyp:gtest',
      ],
      'sources': [
        # Sources based on files in r173 of gmock.
        'third_party/googletest/googlemock/include/gmock/gmock-actions.h',
        'third_party/googletest/googlemock/include/gmock/gmock-cardinalities.h',
        'third_party/googletest/googlemock/include/gmock/gmock-generated-actions.h',
        'third_party/googletest/googlemock/include/gmock/gmock-generated-function-mockers.h',
        'third_party/googletest/googlemock/include/gmock/gmock-generated-matchers.h',
        'third_party/googletest/googlemock/include/gmock/gmock-generated-nice-strict.h',
        'third_party/googletest/googlemock/include/gmock/gmock-matchers.h',
        'third_party/googletest/googlemock/include/gmock/gmock-spec-builders.h',
        'third_party/googletest/googlemock/include/gmock/gmock.h',
        'third_party/googletest/googlemock/include/gmock/internal/gmock-generated-internal-utils.h',
        'third_party/googletest/googlemock/include/gmock/internal/gmock-internal-utils.h',
        'third_party/googletest/googlemock/include/gmock/internal/gmock-port.h',
        'third_party/googletest/googlemock/src/gmock-all.cc',
        'third_party/googletest/googlemock/src/gmock-cardinalities.cc',
        'third_party/googletest/googlemock/src/gmock-internal-utils.cc',
        'third_party/googletest/googlemock/src/gmock-matchers.cc',
        'third_party/googletest/googlemock/src/gmock-spec-builders.cc',
        'third_party/googletest/googlemock/src/gmock.cc',
      ],
      'sources!': [
        'third_party/googletest/googlemock/src/gmock-all.cc',  # Not needed by our build.
      ],
      'include_dirs': [
        'third_party/googletest/googlemock/',
        'third_party/googletest/googlemock/include',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'third_party/googletest/googlemock/include',  # So that gmock headers can find themselves.
        ],
      },
      'export_dependent_settings': [
        'gtest.gyp:gtest',
      ],
    },
    {
      'target_name': 'gmock_main',
      'type': 'static_library',
      'dependencies': [
        'gmock',
      ],
      'sources': [
        'third_party/googletest/googlemock/src/gmock_main.cc',
      ],
    },
  ],
}