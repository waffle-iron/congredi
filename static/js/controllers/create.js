var angular = require('angular');
module.exports = function ($scope, $location) {
// 	$scope.note = new Note();
	$scope.isSubmitting = false;
	$scope.saveNote = function (note) {
		$scope.isSubmitting = true;
		note.$save().then(function () {
			$location.path('/notes');
		}).finally(function () {
			$scope.isSubmitting = false;
		});
	};
	Session.authenticate();
// 	$scope.note = new Note();
// 	Category.all().then(function (categoryData) {
// 		$scope.categories = categoryData;
// 		$scope.note.CategoryId = categoryData[0].id;
// 	});
	$scope.updateNote = function (note) {
		$scope.errors = null;
		$scope.updating = true;
// 		Note.create(note).catch(function (noteData) {
// 			$scope.errors = [noteData.data.error];
// 		}).finally(function () {
// 			$scope.updating = false;
// 		});
// 		note.$save().catch(function (noteData) {
// 			$scope.errors = [noteData.data.error];
// 		}).finally(function () {
// 			$scope.updating = false;
// 		});
	};
}