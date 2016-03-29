/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: VolumeSnap', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.VolumeSnap'));

    // instantiate service
    var VolumeSnap;
    beforeEach(inject(function (_VolumeSnap_) {
      VolumeSnap = _VolumeSnap_;
    }));

    it('should do something', function () {
      expect(!!VolumeSnap).toBe(true);
    });

  });
});
