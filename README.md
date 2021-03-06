# node-libtorrent-rb

node-libtorrent-rb is a fork of [node-libtorrent](https://github.com/fanatid/node-libtorrent) and provides native bindings to [libtorrent rastebar](http://www.rasterbar.com/products/libtorrent/) as a [Node.js addon](http://nodejs.org/docs/latest/api/addons.html).

There is a lot of forks out there. My goal here was to be able to easily use this module everywhere (Mac, Linux **and** Windows).

Libtorrent and it's dependencies (Boost) are bundled and compiled with node-gyp. We then use node-pre-gyp to easily install the module from precompiled .node packages.

If a precompiled package is not available for the user's config, we try to compile the bindings, libtorrent and Boost with node-gyp.

# Getting started
Execute in command line:
```
$ npm install libtorrent-rb
```
or copy repository and build bindings manually
```
$ git clone git://github.com/leeroybrun/node-libtorrent-rb.git
$ cd node-libtorrent-rb
$ npm install -g node-gyp
$ node-gyp configure
$ node-gyp build
```

# TODO
- http://cylonjs.com/blog/2014/11/19/creating-multiplatform-precompiled-binaries-for-node-modules/
- Use Travis-CI
	- Debug travis build
	- Add tests to validate builds
- Package deps in a compressed folder (example: https://github.com/mapbox/node-sqlite3/tree/master/deps)
- Configure node-pre-gyp & add to package.json
- Add OpenSSL optional support
- Add options to node-gyp building
- Test building on linux/windows with node-gyp
