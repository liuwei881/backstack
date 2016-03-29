/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Controller: TasklogCtrl', function () {

    // load the controller's module
    beforeEach(module('zCloudApp.controllers.TasklogCtrl'));

    var TasklogCtrl;

    // Initialize the controller and a mock scope
    beforeEach(inject(function ($controller, $rootScope) {
      TasklogCtrl = $controller('TasklogCtrl', {
        // place here mocked dependencies
      });
    }));

    it('should attach a list of awesomeThings to the scope', function () {
      expect(TasklogCtrl.awesomeThings.length).toBe(3);
    });
  });
});
