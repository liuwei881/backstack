/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: Types', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.Types'));

    // instantiate service
    var Types;
    beforeEach(inject(function (_Types_) {
      Types = _Types_;
    }));

    it('should do something', function () {
      expect(!!Types).toBe(true);
    });

  });
});
