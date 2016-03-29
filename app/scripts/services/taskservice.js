define(['angular'], function (angular) {
  'use strict';

  /**
   * @ngdoc service
   * @name zCloudApp.TaskService
   * @description
   * # TaskService
   * Service in the zCloudApp.
   */
  angular.module('zCloudApp.services.TaskService', [])
	.service('TaskService', function ($http) {
	    // AngularJS will instantiate a singleton by calling "new" on this function
	    function fetch(params) {
            return $http.get('/api/task', {params: params});
        }

        function save(params) {
            if (params.TaskId != undefined) {
                return $http.put('/api/task/' + params.TaskId, {params: params})
            } else {
                return $http.post('/api/task', {params: params})
            }
        }

        function Delete(id) {
            return $http.delete('/api/task/' + id);
        }

        function changeStatus(id) {
            return $http.get('/api/taskchange/status.' + id);
        }

        function statics(id) {
            return $http.get('/api/taskstatics/' + id);
        }

        return {
            fetch: fetch,
            save: save,
            Delete: Delete,
            changeStatus:changeStatus,
            statics : statics
        }
	});
});
