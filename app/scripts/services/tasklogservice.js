define(['angular'], function (angular) {
  'use strict';

  /**
   * @ngdoc service
   * @name zCloudApp.TasklogService
   * @description
   * # TasklogService
   * Service in the zCloudApp.
   */
  angular.module('zCloudApp.services.TasklogService', [])
	.service('TasklogService', function ($http) {
	// AngularJS will instantiate a singleton by calling "new" on this function
	    function fetch(params) {
            return $http.get('/api/tasklog', {params: params});
        }

        return {
            fetch: fetch
        }
	});
});
