var angular = require('angular');
module.exports = function ($scope, $routeParams, $location, Note, Category, Session) {
	$scope.note = Note.get({
		id: $routeParams.id
	});
	$scope.isSubmitting = false;
	$scope.categories = Category.query();
	$scope.users = User.query();
	$scope.saveNote = function (note) {
		$scope.isSubmitting = true;
		note.$update().finally(function () {
			$scope.isSubmitting = false;
			$location.path('/notes/' + note.id);
		});
	};
	// Without NgResource
	// Note.find($routeParams.id).success(function (noteData) {
	//   $scope.note = noteData;
	// });
	Session.authenticate();
	// With NgResource
	$scope.note = Note.get({
		id: $routeParams.id
	});
	// Fetch the node types to use within the sorting menu
	Category.all().then(function (categoryData) {
		$scope.categories = categoryData;
	});
	$scope.updateNote = function (note) {
		$scope.errors = null;
		$scope.updating = true;
		// Without NgResource
		// Note.update(note).catch(function (noteData) {
		//   $scope.errors = [noteData.data.error];
		// }).finally(function () {
		//   $scope.updating = false;
		// });
		// With NgResource
		note.$update().catch(function (noteData) {
			$scope.errors = [noteData.data.error];
		}).finally(function () {
			$scope.updating = false;
		});
	};
};
