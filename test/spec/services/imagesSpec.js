/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: Images', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.Images'));

    // instantiate service
    var Images;
    beforeEach(inject(function (_Images_) {
      Images = _Images_;
    }));

    it('should do something', function () {
      expect(!!Images).toBe(true);
    });

  });
});
