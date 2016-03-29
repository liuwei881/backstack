define(['angular'], function (angular) {
  'use strict';

  /**
   * @ngdoc service
   * @name zCloudApp.MysqlService
   * @description
   * # MysqlService
   * Service in the zCloudApp.
   */
  angular.module('zCloudApp.services.MysqlService', [])
	.service('MysqlService', function ($http) {
	    // AngularJS will instantiate a singleton by calling "new" on this function
	    function fetch(params) {
            return $http.get('/api/mysql', {params: params});
        }

        function save(params) {
            if (params.MysqlId != undefined) {
                return $http.put('/api/mysql/' + params.MysqlId, {params: params})
            } else {
                return $http.post('/api/mysql', {params: params})
            }
        }

        function Delete(params) {
            return $http.delete('/api/mysql/' + params.MysqlId);
        }

        return {
            fetch: fetch,
            save: save,
            Delete: Delete
        }
	});
});
