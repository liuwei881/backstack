/*jshint unused: vars */
require.config({
    paths: {
        angular: '../../asserts/angular/angular',
        'angular-animate': '../../asserts/angular-animate/angular-animate',
        'angular-cookies': '../../asserts/angular-cookies/angular-cookies',
        'angular-mocks': '../../asserts/angular-mocks/angular-mocks',
        'angular-sanitize': '../../asserts/angular-sanitize/angular-sanitize',
        bootstrap: '../../asserts/bootstrap/dist/js/bootstrap',
        'angular-ui-router': '../../asserts/angular-ui-router/release/angular-ui-router',
        'angular-route': '../../asserts/angular-route/angular-route',
        jquery: '../../asserts/jquery/dist/jquery.min',
        'jquery-ui': '../../asserts/global/plugins/jquery-ui/jquery-ui.min',
        bootstraphoverdropdown: '../../asserts/global/plugins/bootstrap-hover-dropdown.min',
        slimscroll: '../../asserts/global/plugins/jquery-slimscroll/jquery.slimscroll.min',
        metronic: '../../asserts/global/scripts/metronic',
        layout: '../../asserts/admin/layout4/scripts/layout',
        'angular-resource': '../../asserts/angular-resource/angular-resource',
        'angular-bootstrap': '../../asserts/angular-bootstrap/ui-bootstrap-tpls',
        'bootstrap-tpls': '../../asserts/angular-bootstrap/ui-bootstrap-tpls.min',
        typeAttrEtc: '../../asserts/etc/attrsConf',
        'highcharts-ng': '../../asserts/highcharts-ng/dist/highcharts-ng',
        highcharts: '../../asserts/highcharts-ng/highcharts',
        d3:'../../asserts/d3/d3.min'
    },
    shim: {
        angular: {
            exports: 'angular'
        },
        'angular-cookies': [
            'angular',
            'typeAttrEtc'
        ],
        'angular-sanitize': [
            'angular'
        ],
        'angular-animate': [
            'angular'
        ],
        'angular-mocks': {
            deps: [
                'angular'
            ],
            exports: 'angular.mock'
        },
        'angular-ui-router': [
            'angular'
        ],
        'angular-bootstrap': [
            'angular',
            'bootstrap-tpls'
        ],
        'bootstrap-tpls': [
            'angular'
        ],
        'highcharts-ng': [
            'angular',
            'highcharts'
        ],
        metronic: {
            deps: [
                'bootstrap',
                'jquery',
                'jquery-ui',
                'bootstraphoverdropdown',
                'slimscroll'
            ],
            exports: 'Metronic'
        },
        bootstrap: {
            deps: [
                'jquery'
            ]
        },
        bootstraphoverdropdown: {
            deps: [
                'jquery'
            ]
        },
        slimscroll: {
            deps: [
                'jquery'
            ]
        },
        layout: {
            deps: [
                'metronic'
            ]
        },
        jquery: {
            exports: 'jQuery'
        }
    },
    priority: [
        'angular'
    ],
    packages: [

    ]
});

//http://code.angularjs.org/1.2.1/docs/guide/bootstrap#overview_deferred-bootstrap
window.name = 'NG_DEFER_BOOTSTRAP!';

require([
    'angular',
    'app',
    'angular-cookies',
    'angular-sanitize',
    'angular-animate',
    'angular-ui-router',
    'layout',
    'angular-bootstrap',
    'highcharts-ng',
    'd3'
], function (angular, app, ngCookies, ngSanitize, ngAnimate, uiRouter, layout, bootstrap) {
    'use strict';
    /* jshint ignore:start */
    var $html = angular.element(document.getElementsByTagName('html')[0]);
    /* jshint ignore:end */
    angular.element().ready(function () {
        angular.resumeBootstrap([app.name]);
    });
});
