/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: Volumes', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.Volumes'));

    // instantiate service
    var Volumes;
    beforeEach(inject(function (_Volumes_) {
      Volumes = _Volumes_;
    }));

    it('should do something', function () {
      expect(!!Volumes).toBe(true);
    });

  });
});
