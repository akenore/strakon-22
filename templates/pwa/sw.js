var CACHE_NAME = 'cache-v2';
var urlsToCache = [
    
    '/',
    '/static/pwa/manifest.json',
    '/static/frontend/js/jquery.min.js',
    '/static/frontend/js/popper.min.js',
    '/static/frontend/js/bootstrap.min.js',
    '/static/frontend/js/mdb.lite.min.js',
    '/static/frontend/img/logo.png',
    '/static/frontend/img/ifc.png',
    '/static/frontend/img/students-2.png',
    '/static/frontend/img/onlinepraesentation.png',
    '/static/frontend/img/c2it-strakon20.jpg',
    '/static/frontend/img/acs-strakon20.jpg',
    '/static/frontend/img/home-st.jpg'

];

self.addEventListener('install', function (event) {
    // Perform install steps
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function (cache) {
                console.log('Service Worker: Caching Files');
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', function (event) {
    event.respondWith(
        caches.match(event.request)
            .then(function (response) {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            }
            )
    );
});

self.addEventListener('activate', function (event) {
    console.log('Service Worker: Activated');
    
    var cacheAllowlist = ['cache-v1', 'cache-v2', 'cache-v3'];

    event.waitUntil(
        caches.keys().then(function (cacheNames) {
            return Promise.all(
                cacheNames.map(function (cacheName) {
                    if (cacheAllowlist.indexOf(cacheName) === -1) {
                        console.log('Service Worker: Delete old Cache');
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});