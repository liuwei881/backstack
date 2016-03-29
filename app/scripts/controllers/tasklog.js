define(['angular'], function (angular) {
  'use strict';

  /**
   * @ngdoc function
   * @name zCloudApp.controller:TasklogCtrl
   * @description
   * # TasklogCtrl
   * Controller of the zCloudApp
   */
  angular.module('zCloudApp.controllers.TasklogCtrl', [])
    .controller('TasklogCtrl', function (TasklogService, $scope, $state, $modal) {
      this.awesomeThings = [
        'HTML5 Boilerplate',
        'AngularJS',
        'Karma'
      ];
        $scope.total = 0;
        $scope.pageSize = 15;
        $scope.page = 1;
        $scope.searchKey = '';
        $scope.initPage = function(searchKey){
            TasklogService.fetch({page: $scope.page, pageSize: $scope.pageSize, searchKey:searchKey}).
                success(function (data) {
                    $scope.searchKey = searchKey;
                    $scope.total = data.total;
                    $scope.rows  = data.rows;
                });
        };

        $scope.detail = function (i) {
            $modal.open({
                animation: true,
                templateUrl: 'detail.html',
                controller: 'ModalInstanceCtrl',
                size: 'lg',
                resolve: {
                    item: function () {
                        return $scope.rows[i];
                    },
                    title: function () {
                        return '查看更新命令';
                    }
                }
            });
        };

        if ($state.current.needRequest) {
            $scope.initPage();
        }
        $scope.pageAction = function (page) {
            TasklogService
                .fetch({page: page})
                .success(function (data) {
                    $scope.total = data.total;
                    $scope.rows = data.rows;
                });
        };
        $scope.Search = function (searchKey) {
            $scope.initPage(searchKey);
        };

    });
});
