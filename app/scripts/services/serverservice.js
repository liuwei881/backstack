define(['angular'], function (angular) {
  'use strict';

  /**
   * @ngdoc service
   * @name zCloudApp.ServerService
   * @description
   * # ServerService
   * Service in the zCloudApp.
   */
  angular.module('zCloudApp.services.ServerService', [])
	.service('ServerService', function ($http) {
	    // AngularJS will instantiate a singleton by calling "new" on this function
	    function fetch(params) {
            return $http.get('/api/server', {params: params});
        }

        function save(params) {
            if (params.ServerId != undefined) {
                return $http.put('/api/server/' + params.ServerId, {params: params})
            } else {
                return $http.post('/api/server', {params: params})
            }
        }

        function saveNginx(params) {
            if (params.NginxId != undefined) {
                return $http.put('/api/nginx/' + params.NginxId, {params: params})
            } else {
                return $http.post('/api/nginx', {params: params})
            }
        }

        function saveMysql(params) {
            if (params.MysqlId != undefined) {
                return $http.put('/api/mysql/' + params.MysqlId, {params: params})
            } else {
                return $http.post('/api/mysql', {params: params})
            }
        }

        function Delete(params) {
            return $http.delete('/api/server/' + params.ServerId);
        }


        return {
            fetch: fetch,
            save: save,
            saveNginx: saveNginx,
            saveMysql: saveMysql,
            Delete: Delete
        }
	});
});
