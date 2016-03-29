/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: Instances', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.Instances'));

    // instantiate service
    var Instances;
    beforeEach(inject(function (_Instances_) {
      Instances = _Instances_;
    }));

    it('should do something', function () {
      expect(!!Instances).toBe(true);
    });

  });
});
