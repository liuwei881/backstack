/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: Projects', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.Projects'));

    // instantiate service
    var Projects;
    beforeEach(inject(function (_Projects_) {
      Projects = _Projects_;
    }));

    it('should do something', function () {
      expect(!!Projects).toBe(true);
    });

  });
});
