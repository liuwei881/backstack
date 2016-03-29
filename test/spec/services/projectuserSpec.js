/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: ProjectUser', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.ProjectUser'));

    // instantiate service
    var ProjectUser;
    beforeEach(inject(function (_ProjectUser_) {
      ProjectUser = _ProjectUser_;
    }));

    it('should do something', function () {
      expect(!!ProjectUser).toBe(true);
    });

  });
});
