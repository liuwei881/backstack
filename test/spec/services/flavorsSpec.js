/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: Flavors', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.Flavors'));

    // instantiate service
    var Flavors;
    beforeEach(inject(function (_Flavors_) {
      Flavors = _Flavors_;
    }));

    it('should do something', function () {
      expect(!!Flavors).toBe(true);
    });

  });
});
