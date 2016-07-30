//Setting HTTP Headers

//The $http service will automatically add certain HTTP headers to all requests. These defaults can be
//fully configured by accessing the $httpProvider.defaults.headers configuration object, which currently
//contains this default configuration:
/*
    $httpProvider.defaults.headers.common (headers that are common for all requests):
        Accept: application/json, text/plain, * / *
    $httpProvider.defaults.headers.post: (header defaults for POST requests)
        Content-Type: application/json
    $httpProvider.defaults.headers.put (header defaults for PUT requests)
        Content-Type: application/json
*/
//To add or overwrite these defaults, simply add or remove a property from these configuration objects.
//To add headers for an HTTP method other than POST or PUT, simply add a new object with the lowercased
//HTTP method name as the key, e.g. $httpProvider.defaults.headers.get = { 'My-Header' : 'value' }.

//The defaults can also be set at runtime via the $http.defaults object in the same fashion. For example:

module.run(function($http) {
    $http.defaults.headers.common.Authorization = 'Basic YmVlcDpib29w';
});

//In addition, you can supply a headers property in the config object passed
//when calling $http(config), which overrides the defaults without changing them globally.

//To explicitly remove a header automatically added via $httpProvider.defaults.headers
//on a per request basis, Use the headers property, setting the desired header to undefined. For example:

var req = {
    method: 'POST',
    url: 'http://example.com',
    headers: {
        'Content-Type': undefined
    },
    data: {
        test: 'test'
    }
};

//$http(req).then(function(){...}, function(){...});