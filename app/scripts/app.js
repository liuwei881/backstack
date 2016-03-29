/*jshint unused: vars */
define(['angular', 'controllers/main', 'controllers/about', 'directives/paging', 'controllers/login', 'controllers/header', 'controllers/sidebar', 'controllers/pagehead', 'controllers/footer', 'controllers/dashboard', 'services/httpinterceptor', 'controllers/users', 'services/users', 'controllers/modalinstance', 'controllers/task', 'services/taskservice', 'controllers/tasklog', 'services/tasklogservice', 'directives/tasktype', 'controllers/types', 'services/types', 'services/syncservice','controllers/server','services/serverservice','controllers/nginxserver','services/nginxservice','controllers/mysqlserver','services/mysqlservice']/*deps*/, function (angular, MainCtrl, AboutCtrl, PagingDirective, LoginCtrl, HeaderCtrl, SidebarCtrl, PageHeadCtrl, FooterCtrl, DashboardCtrl, PhysicalCtrl, HttpInterceptorFactory, PhysicalService, UsersCtrl,UsersServices, ModalinstanceCtrl, TaskCtrl, TaskServiceService, TasklogCtrl, TasklogServiceService, TaskTypeDirective, TypesCtrl, TypesService, Syncservice,ServerCtrl,ServerService,NginxServerCtrl,NginxService,MsqlServerCtrl,MysqlService)/*invoke*/ {
    'use strict';

    /**
     * @ngdoc overview
     * @name zCloudApp
     * @description
     * # zCloudApp
     *
     * Main module of the application.
     */
    return angular
        .module('zCloudApp', ['zCloudApp.controllers.MainCtrl',
            'zCloudApp.controllers.AboutCtrl',
            'zCloudApp.directives.Paging',
            'zCloudApp.controllers.LoginCtrl',
            'zCloudApp.controllers.HeaderCtrl',
            'zCloudApp.controllers.SidebarCtrl',
            'zCloudApp.controllers.PageHeadCtrl',
            'zCloudApp.controllers.FooterCtrl',
            'zCloudApp.controllers.DashboardCtrl',
            'zCloudApp.services.HttpInterceptor',
            'zCloudApp.controllers.UsersCtrl',
            'zCloudApp.services.Users',
            'zCloudApp.controllers.ModalInstanceCtrl',
            'zCloudApp.controllers.TaskCtrl',
'zCloudApp.services.TaskService',
'zCloudApp.controllers.TasklogCtrl',
'zCloudApp.services.TasklogService',
'zCloudApp.directives.TaskType',
'zCloudApp.controllers.TypesCtrl',
'zCloudApp.services.Types',
'zCloudApp.services.Syncservice',
'zCloudApp.controllers.ServerCtrl',
'zCloudApp.services.ServerService',
'zCloudApp.controllers.NginxServerCtrl',
'zCloudApp.services.NginxService',
'zCloudApp.controllers.MysqlServerCtrl',
'zCloudApp.services.MysqlService',
/*angJSDeps*/
            'ngCookies',
            'ngSanitize',
            'ngAnimate',
            'ui.router'
        ])
        .config(function ($stateProvider, $urlRouterProvider, $httpProvider) {
            $httpProvider.interceptors.push('httpInterceptor');
            $stateProvider
                .state('dashboard', {
                    url: '/',
                    templateUrl: 'views/main.html',
                    nav: 'DashHome'
                })
                .state('dashboard.home', {
                    url: '/dashboard',
                    templateUrl: 'views/dashboard.html',
                    controller: 'DashboardCtrl',
                    nav: 'DashBoard'
                })
                .state('dashboard.task', {
                    url: 'task',
                    templateUrl: 'views/task.html',
                    controller: 'TaskCtrl',
                    nav: '任务管理',
                    needRequest: true
                })
                .state('dashboard.tasklog', {
                    url: 'tasklog',
                    templateUrl: 'views/tasklog.html',
                    controller: 'TasklogCtrl',
                    nav: '任务日志',
                    needRequest: true
                })
                .state('dashboard.types', {
                    url: 'types',
                    templateUrl: 'views/types.html',
                    controller: 'TypesCtrl',
                    nav: '类型管理',
                    needRequest: true
                })
                .state('dashboard.server', {
                    url: 'server',
                    templateUrl: 'views/server.html',
                    controller: 'ServerCtrl',
                    nav: '服务器管理',
                    needRequest: true
                })
                .state('dashboard.nginx', {
                    url: 'nginx',
                    templateUrl: 'views/nginxserver.html',
                    controller: 'NginxServerCtrl',
                    nav: 'Nginx管理',
                    needRequest: true
                })
                .state('dashboard.mysql', {
                    url: 'mysql',
                    templateUrl: 'views/mysqlserver.html',
                    controller: 'MysqlServerCtrl',
                    nav: 'Mysql管理',
                    needRequest: true
                })
                .state('login',{
                    url: '/login',
                    templateUrl: 'views/login.html',
                    controller: 'LoginCtrl'
                })
                .state('logout',{
                    url: '/logout',
                    controller: function($cookies,$state){
                        $cookies.remove('user');
                        $state.go('login');
                    }
                })
            $urlRouterProvider.otherwise('/');
        })
        .run(function ($rootScope, $state, $stateParams, $cookies) {
            $rootScope.$state = $state;
            $rootScope.$stateParams = $stateParams;
            $rootScope.$on('$stateChangeStart', function (event, toState, fromState) {
                if (toState.url === '/login') {
                    $('body').addClass('login');
                } else {
                    $('body').removeClass('login');
                    if ($cookies.get('user') === undefined) {
                        event.preventDefault();
                        $state.go('login');
                    }
                }
            });
        });
    ;
});
