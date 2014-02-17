{
    "includes": [ "deps/common.gypi" ],
    "targets": [
        {
          "target_name": "node_libtorrent",
          "sources": [
              # Node.js libtorrent bindings sources
            	"src/module.cpp",

              "src/add_torrent_params.cpp",
              "src/alert.cpp",
              "src/bencode.cpp",
              "src/create_torrent.cpp",
              "src/entry.cpp",
              "src/file_storage.cpp",
              "src/fingerprint.cpp",
              "src/ip_filter.cpp",
              "src/peer_info.cpp",
              "src/rss.cpp",
              "src/session.cpp",
              "src/session_settings.cpp",
              "src/session_status.cpp",
              "src/storage.cpp",
              "src/torrent_handle.cpp",
              "src/torrent_info.cpp",
              "src/torrent_status.cpp",
          ],
          'xcode_settings': {
              "OTHER_CFLAGS": [
                  '<@(default_cflags)'
              ],
              'OTHER_CPLUSPLUSFLAGS':[
                  '<@(default_cflags)'
              ],
              'GCC_ENABLE_CPP_RTTI': 'YES',
              'GCC_ENABLE_CPP_EXCEPTIONS': 'NO'
          },
          'defines': [
              '_LIB',
              '<@(default_defines)'
          ], 
          'dependencies': [
              'deps/libtorrent/libtorrent.gyp:libtorrent'
          ],
          'include_dirs': [
              'deps/libtorrent',
              'deps/libtorrent/include',
              'deps/libtorrent/include/libtorrent',
              'deps/boost',
              'deps/boost/boost'
          ]
        },

        # CLIENT_TEST
        {
            "target_name": "libtorrent_client_test",
            'type': 'executable',
            "sources": [
                'deps/libtorrent/examples/client_test.cpp'
            ],
            'include_dirs': [
                'deps/boost/inc-examples',
                'deps/boost/inc-examples/boost',
            ],
            'xcode_settings': {
                "OTHER_CFLAGS": [
                    '<@(default_cflags)'
                ],
                'OTHER_CPLUSPLUSFLAGS':[
                    '<@(default_cflags)'
                ],
                'GCC_ENABLE_CPP_RTTI': 'YES',
                'GCC_ENABLE_CPP_EXCEPTIONS': 'NO'
            },
            'dependencies': [
                'deps/libtorrent/libtorrent.gyp:libtorrent',
                'deps/boost/boost.gyp:boost_atomic',
                'deps/boost/boost.gyp:boost_date_time',
                'deps/boost/boost.gyp:boost_exception',
                'deps/boost/boost.gyp:boost_smart_ptr',
                'deps/boost/boost.gyp:boost_system',
                'deps/boost/boost.gyp:boost_thread'
            ]
        },

        # CONNECTION_TESTER
        {
            "target_name": "libtorrent_connection_tester",
            'type': 'executable',
            "sources": [
                'deps/libtorrent/examples/connection_tester.cpp'
            ],
            'include_dirs': [
                'deps/boost/inc-examples',
                'deps/boost/inc-examples/boost',
            ],
            'xcode_settings': {
                "OTHER_CFLAGS": [
                    '<@(default_cflags)'
                ],
                'OTHER_CPLUSPLUSFLAGS':[
                    '<@(default_cflags)'
                ],
                'GCC_ENABLE_CPP_RTTI': 'YES',
                'GCC_ENABLE_CPP_EXCEPTIONS': 'NO'
            },
            'dependencies': [
                'deps/libtorrent/libtorrent.gyp:libtorrent',
                'deps/boost/boost.gyp:boost_atomic',
                'deps/boost/boost.gyp:boost_date_time',
                'deps/boost/boost.gyp:boost_exception',
                'deps/boost/boost.gyp:boost_smart_ptr',
                'deps/boost/boost.gyp:boost_system',
                'deps/boost/boost.gyp:boost_thread'
            ]
        },

        # SIMPLE_CLIENT
        {
            "target_name": "libtorrent_simple_client",
            'type': 'executable',
            "sources": [
                'deps/libtorrent/examples/simple_client.cpp'
            ],
            'include_dirs': [
                'deps/boost/inc-examples',
                'deps/boost/inc-examples/boost',
            ],
            'xcode_settings': {
                "OTHER_CFLAGS": [
                    '<@(default_cflags)'
                ],
                'OTHER_CPLUSPLUSFLAGS':[
                    '<@(default_cflags)'
                ],
                'GCC_ENABLE_CPP_RTTI': 'YES',
                'GCC_ENABLE_CPP_EXCEPTIONS': 'NO'
            },
            'dependencies': [
                'deps/libtorrent/libtorrent.gyp:libtorrent',
                'deps/boost/boost.gyp:boost_atomic',
                'deps/boost/boost.gyp:boost_date_time',
                'deps/boost/boost.gyp:boost_exception',
                'deps/boost/boost.gyp:boost_smart_ptr',
                'deps/boost/boost.gyp:boost_system',
                'deps/boost/boost.gyp:boost_thread'
            ]
        }
    ]
}
