angular.module('app', [])
.controller('adminController',["$scope", "$http", function($scope,$http){
    $scope.package = {};
    $scope.days=[];
    $scope.package_days={};
    $scope.amenities=[];
    $scope.package_amenity={};
    $scope.collage={};
    $scope.student={};


 var sendPostCall = function(url, data) {
    console.log("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDJJJJJJJJJJJJJ3");
    console.log(data, "333333333333333333333333333333333333333333333333333333");
    console.log("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ3");
    
    $http({
      method: 'POST',
      url: url,
      data : data
    }).then(function (res) {
      console.log(res);
      
            createToast("'pakage successfully created!!!'","green");

      },
      // failed callback
      function (req) {
        createToast("'Something went wrong!!!'","red");
      })
    }   



      $scope.addPackage=function(){
        console.log("aaaaaaaaaat");
        console.log("package details",$scope.package);
        sendPostCall('/api/v1/package',$scope.package);
        createToast("'Pakage Added!!'","green");
      }



        $scope.addCollege=function(){
          console.log(" addcollege function working");
          console.log("college details",$scope.college);
          sendPostCall('/api/v1/college', $scope.college);
          createToast("'College Added!!'","green");
        }




          $scope.addStudent=function(){
            console.log(" addstudent function working");
            console.log("student details",$scope.student);
            sendPostCall('/api/v1/student', $scope.student);
            createToast("'Data recieved ..proceed to payment !!'","green");
          }




          /*var app = angular.module('myApp', []);
          app.controller('adminController'function($scope, $http){
            method : "POST",
            url : "/api/v1/package"
            data : $scope.package
          }).then(function (res) {
            console.log(res);
            
                  createToast("'pakage successfully created!!!'","green");
      
            },
            // failed callback
            function (req) {
              createToast("'Something went wrong!!!'","red");
            });*/
               
 
            




  $scope.addAnotherDay=function(){
    $scope.days.push($scope.package_days);
    $scope.package_days={};
    $scope.package.days=$scope.days;
    console.log("days",$scope.days);
    createToast("'Day Added!!'","green");

  }



  $scope.addAmenities=function(){
    $scope.amenities.push($scope.package_amenity);
    $scope.package_amenity={};
    $scope.package.amenities=$scope.amenities;
    console.log("package",$scope.package);
    createToast("'amenity Added!!'","green");

  }
}]);