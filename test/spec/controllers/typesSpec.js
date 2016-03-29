/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Controller: TypesCtrl', function () {

    // load the controller's module
    beforeEach(module('zCloudApp.controllers.TypesCtrl'));

    var TypesCtrl;

    // Initialize the controller and a mock scope
    beforeEach(inject(function ($controller, $rootScope) {
      TypesCtrl = $controller('TypesCtrl', {
        // place here mocked dependencies
      });
    }));

    it('should attach a list of awesomeThings to the scope', function () {
      expect(TypesCtrl.awesomeThings.length).toBe(3);
    });
  });
});
