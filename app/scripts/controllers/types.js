define(['angular'], function (angular) {
  'use strict';

  /**
   * @ngdoc function
   * @name zCloudApp.controller:TypesCtrl
   * @description
   * # TypesCtrl
   * Controller of the zCloudApp
   */
  angular.module('zCloudApp.controllers.TypesCtrl', [])
    .controller('TypesCtrl', function (Types, $scope, $modal, $state) {
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
            Types.fetch({page: $scope.page, pageSize: $scope.pageSize, searchKey:searchKey}).
                success(function (data) {
                    $scope.searchKey = searchKey;
                    $scope.total = data.total;
                    $scope.rows  = data.rows;
                });
        };

        if ($state.current.needRequest) {
            $scope.initPage();
        }

        $scope.Create = function () {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'add.html',
                controller: 'ModalInstanceCtrl',
                size: 'lg',
                resolve: {
                    item: function () {
                        return {};
                    },
                    title: function () {
                        return {'title':'新建'};
                    }
                }
            });
            modalInstance.save = function (item) {
                Types.save(item).
                    success(function (data) {
                        modalInstance.close();
                        $scope.initPage();
                    });
            };
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
                        return '查看';
                    }
                }
            });
        };

        $scope.edit = function (i) {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'edit.html',
                controller: 'ModalInstanceCtrl',
                size: 'lg',
                resolve: {
                    item: function () {
                        return $scope.rows[i];
                    },
                    title: function () {
                        return {'title':'编辑','etcTaskType':etcTaskType,'etcIsDisabled':etcIsDisabled};
                    }
                }
            });
            modalInstance.save = function (item) {
                Types.save(item).
                    success(function (data) {
                        modalInstance.close();
                        $scope.initPage();
                    });
            };
        };
        $scope.changeStatus = function (TypeId) {
            Types.changeStatus(TypeId).
                success(function (data) {
                    $scope.initPage();
                });
        };

        $scope.Search = function (searchKey) {
            $scope.initPage(searchKey);
        };

        $scope.pageAction = function (page) {
            Types
                .fetch({page: page})
                .success(function (data) {
                    $scope.total = data.total;
                    $scope.rows = data.rows;
                });
        };


    });
});
