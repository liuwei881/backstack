/*jshint unused: vars */
define(['angular', 'angular-mocks', 'app'], function(angular, mocks, app) {
  'use strict';

  describe('Directive: paging', function () {

    // load the directive's module
    beforeEach(module('zCloudApp.directives.Paging'));

    var element,
      scope;

    beforeEach(inject(function ($rootScope) {
      scope = $rootScope.$new();
    }));

    it('should make hidden element visible', inject(function ($compile) {
      element = angular.element('<paging></paging>');
      element = $compile(element)(scope);
      expect(element.text()).toBe('this is the paging directive');
    }));
  });
});
