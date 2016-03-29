/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Controller: TaskCtrl', function () {

    // load the controller's module
    beforeEach(module('zCloudApp.controllers.TaskCtrl'));

    var TaskCtrl;

    // Initialize the controller and a mock scope
    beforeEach(inject(function ($controller, $rootScope) {
      TaskCtrl = $controller('TaskCtrl', {
        // place here mocked dependencies
      });
    }));

    it('should attach a list of awesomeThings to the scope', function () {
      expect(TaskCtrl.awesomeThings.length).toBe(3);
    });
  });
});
