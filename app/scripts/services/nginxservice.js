define(['angular'], function (angular) {
  'use strict';

  /**
   * @ngdoc service
   * @name zCloudApp.ServerService
   * @description
   * # ServerService
   * Service in the zCloudApp.
   */
  angular.module('zCloudApp.services.NginxService', [])
	.service('NginxService', function ($http) {
	    // AngularJS will instantiate a singleton by calling "new" on this function
	    function fetch(params) {
            return $http.get('/api/nginx', {params: params});
        }

        function save(params) {
            if (params.NginxId != undefined) {
                return $http.put('/api/nginx/' + params.NginxId, {params: params})
            } else {
                return $http.post('/api/nginx', {params: params})
            }
        }

        function Delete(params) {
            return $http.delete('/api/nginx/' + params.NginxId);
        }

        return {
            fetch: fetch,
            save: save,
            Delete: Delete
        }
	});
});
