define(['angular'], function (angular) {
  'use strict';

  /**
   * @ngdoc function
   * @name zCloudApp.controller:TaskCtrl
   * @description
   * # TaskCtrl
   * Controller of the zCloudApp
   */
  angular.module('zCloudApp.controllers.TaskCtrl', ['highcharts-ng'])
    .controller('TaskCtrl', function (TaskService, $scope, $state, $modal, Syncservice, $element) {
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
            TaskService.fetch({page: $scope.page, pageSize: $scope.pageSize, searchKey:searchKey}).
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
                TaskService.save(item).
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
                TaskService.save(item).
                    success(function (data) {
                    console.log(item);
                        modalInstance.close();
                        $scope.initPage();
                    });
            };
        };

        $scope.changeStatus = function (TaskId) {
            TaskService.changeStatus(TaskId).
                success(function (data) {
                    $scope.initPage();
                });
        };

        $scope.statics = function (i) {
            var data = Syncservice.fetch('/api/taskstatics/'+i);
            data = JSON.parse(data);
            if(data.rows){
                var chartConfig = {
                      options: {
                        chart: {
                            type: 'line'
                        },
                      },
                      xAxis: {
                            type: 'datetime',
                      },
                      yAxis: {
                            title: {
                                text: 'FileSize(MB) '
                            }
                      },
                      title: {
                          text: ''
                      },
                      credits:{
                        enabled: true,
                        text: 'IT Group',
                      },
                      plotOptions: {
                            line: {
                                dataLabels: {
                                    enabled: true
                                },
                                enableMouseTracking: false
                            }
                      },
                      series: [{
                        name: "备份文件大小",
                        data: eval('['+data.rows+']')
                      }]

                };
                $modal.open({
                    animation: true,
                    templateUrl: 'statics.html',
                    controller: 'ModalInstanceCtrl',
                    size: 'lg',
                    resolve: {
                        item: function () {
                            return chartConfig;
                        },
                        title: function () {
                            return '备份文件占用趋势';
                        }
                    }
                });
            }
        };

        $scope.Search = function (searchKey) {
            $scope.initPage(searchKey);
        };

        $scope.pageAction = function (page) {
            TaskService
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
