define(['angular'], function (angular) {
  'use strict';

  /**
   * @ngdoc service
   * @name zCloudApp.Types
   * @description
   * # Types
   * Service in the zCloudApp.
   */
  angular.module('zCloudApp.services.Types', [])
	.service('Types', function ($http) {
	// AngularJS will instantiate a singleton by calling "new" on this function
	    function fetch(params) {
            return $http.get('/api/types', {params: params});
        }

        function fetchOne(TypeId) {
            return $http.get('/api/types/'+ TypeId);
        }

        function save(params) {
            if (params.TypeId != undefined) {
                return $http.put('/api/types/' + params.TypeId, {params: params})
            } else {
                return $http.post('/api/types', {params: params})
            }
        }

        function Delete(id) {
            return $http.delete('/api/types/' + id);
        }

        function changeStatus(id) {
            return $http.get('/api/taskchange/type.' + id);
        }

        return {
            fetch: fetch,
            save: save,
            fetchOne:fetchOne,
            Delete: Delete,
            changeStatus:changeStatus
        }
	});
});
