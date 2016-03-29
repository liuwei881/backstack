define(['angular'], function (angular) {
  'use strict';

  /**
   * @ngdoc function
   * @name zCloudApp.controller:ServerCtrl
   * @description
   * # ServerCtrl
   * Controller of the zCloudApp
   */
  angular.module('zCloudApp.controllers.ServerCtrl', ['highcharts-ng'])
    .controller('ServerCtrl', function (ServerService, $scope, $state, $modal) {
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
            ServerService.fetch({page: $scope.page, pageSize: $scope.pageSize, searchKey:searchKey}).
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
                        return {'title':'新建','etcTaskType':etcTaskType,'etcIsDisabled':etcIsDisabled};
                    }
                }
            });
            modalInstance.save = function (item) {
                ServerService.save(item).
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
                ServerService.save(item).
                    success(function (data) {
                    console.log(item);
                        modalInstance.close();
                        $scope.initPage();
                    });
            };
        };

            $scope.Delete = function (i) {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'delete.html',
                controller: 'ModalInstanceCtrl',
                size: 'lg',
                resolve: {
                    item: function () {
                        return $scope.rows[i];
                    },
                    title: function () {
                        return {'title':'删除','etcTaskType':etcTaskType,'etcIsDisabled':etcIsDisabled};
                    }
                }
            });
           modalInstance.Delete = function (item) {
                ServerService.Delete(item).
                    success(function (data) {
                    console.log(item);
                        modalInstance.close();
                        $scope.initPage();
                    });
            };
        };

            $scope.addNginx = function (ServerId) {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'views/server/nginxAdd.html',
                controller: 'ModalInstanceCtrl',
                size: 'lg',
                resolve: {
                    item: function () {
                        return {'ServerId':ServerId};
                    },
                    title: function () {
                        return {'title':'新增nginx配置','etcTaskType':etcTaskType,'etcIsDisabled':etcIsDisabled};
                    }
                }
            });
            modalInstance.save = function (item) {
                ServerService.saveNginx(item).
                    success(function (data) {
                        modalInstance.close();
                        $scope.initPage();
                    });
            };
        };

            $scope.addMysql = function (ServerId) {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'views/server/mysqlAdd.html',
                controller: 'ModalInstanceCtrl',
                size: 'lg',
                resolve: {
                    item: function () {
                        return {'ServerId':ServerId};
                    },
                    title: function () {
                        return {'title':'新增mysql配置','etcTaskType':etcTaskType,'etcIsDisabled':etcIsDisabled};
                    }
                }
            });
            modalInstance.save = function (item) {
                ServerService.saveMysql(item).
                    success(function (data) {
                        modalInstance.close();
                        $scope.initPage();
                    });
            };
        };

        $scope.Search = function (searchKey) {
            $scope.initPage(searchKey);
        };

        $scope.pageAction = function (page) {
            ServerService
                .fetch({page: page})
                .success(function (data) {
                    $scope.total = data.total;
                    $scope.rows = data.rows;
                });
        };


    }).filter('cut', function () {
        return function (value, wordwise, max, tail) {
            if (!value) return '';

            max = parseInt(max, 10);
            if (!max) return value;
            if (value.length <= max) return value;

            value = value.substr(0, max);
            if (wordwise) {
                var lastspace = value.lastIndexOf(' ');
                if (lastspace != -1) {
                    value = value.substr(0, lastspace);
                }
            }
            return value + (tail || '...');
        };
    });;
});
