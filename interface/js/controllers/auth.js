var angular = require('angular');
module.exports = function ($scope, $location, $cookieStore, $localStorage, $sessionStorage/*, authorization, api*/) {
	$scope.title = 'Likeastore. Analytics';
	$scope.login = function () {
		var credentials = {
			username: this.username,
			token: this.token
		};
		var success = function (data) {
			var token = data.token;
			api.init(token);
			$cookieStore.put('token', token);
			$location.path('/');
		};
		var error = function () {
			// TODO: apply user notification here..
		};
		//authorization.login(credentials).success(success).error(error);
	};
}
/*

angular.module('foundationDemoApp').controller('ModalDemoCtrl', function ($scope, $modal, $log) {

  $scope.items = ['item1', 'item2', 'item3'];

  $scope.open = function () {

    var modalInstance = $modal.open({
      templateUrl: 'myModalContent.html',
      controller: 'ModalInstanceCtrl',
      resolve: {
        items: function () {
          return $scope.items;
        }
      }
    });

    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });
  };
});

// Please note that $modalInstance represents a modal window (instance) dependency.
// It is not the same as the $modal service used above.

angular.module('foundationDemoApp').controller('ModalInstanceCtrl', function ($scope, $modalInstance, items) {

  $scope.items = items;
  $scope.selected = {
    item: $scope.items[0]
  };

  $scope.reposition = function () {
    $modalInstance.reposition();
  };

  $scope.ok = function () {
    $modalInstance.close($scope.selected.item);
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
});



*/