/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: Instancesnap', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.Instancesnap'));

    // instantiate service
    var Instancesnap;
    beforeEach(inject(function (_Instancesnap_) {
      Instancesnap = _Instancesnap_;
    }));

    it('should do something', function () {
      expect(!!Instancesnap).toBe(true);
    });

  });
});
