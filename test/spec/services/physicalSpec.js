/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: Physical', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.Physical'));

    // instantiate service
    var Physical;
    beforeEach(inject(function (_Physical_) {
      Physical = _Physical_;
    }));

    it('should do something', function () {
      expect(!!Physical).toBe(true);
    });

  });
});
