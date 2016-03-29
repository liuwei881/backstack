/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Directive: taskType', function () {

    // load the directive's module
    beforeEach(module('zCloudApp.directives.TaskType'));

    var element,
      scope;

    beforeEach(inject(function ($rootScope) {
      scope = $rootScope.$new();
    }));

    it('should make hidden element visible', inject(function ($compile) {
      element = angular.element('<task-type></task-type>');
      element = $compile(element)(scope);
      expect(element.text()).toBe('this is the taskType directive');
    }));
  });
});
