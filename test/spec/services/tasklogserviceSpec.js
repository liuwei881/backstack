/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Service: TasklogService', function () {

    // load the service's module
    beforeEach(module('zCloudApp.services.TasklogService'));

    // instantiate service
    var TasklogService;
    beforeEach(inject(function (_TasklogService_) {
      TasklogService = _TasklogService_;
    }));

    it('should do something', function () {
      expect(!!TasklogService).toBe(true);
    });

  });
});
