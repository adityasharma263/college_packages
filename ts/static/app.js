controller('adminController',["$scope", "$http", function($scope){
    $scope.package={};
    $scope.tripdays=[];
    $scope.days={};
    $scope.package_amenities=[];
    $scope.amenities={};


var sendPostCall = function(url, data) {fg
    console.log(data);
    
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



      $scope.addpakage=function(){
        $scope.package_id=$scope.package;
        sendPostCall('/api/v1/package', $scope.package)
        createToast("'Pakage Added!!'","green");
      }



        $scope.addcollege=function(){
          $scope.college_id=$scope.college_id;
          sendPostCall('/', $scope.college)
          createToast("'College Added!!'","green");
        }




          $scope.addstudent=function(){
            $scope.student_id=$scope.student_id;
            sendPostCall('/', $scope.student)
            createToast("'Data recieved ..proceed to payment !!'","green");
          }




  $scope.addanotherday=function(){
    $scope.tripdays.push($scope.days);
    $scope.days={};
    createToast("'Day Added!!'","green");

  }



  $scope.addamenities=function(){
    $scope.package_amenities.push($scope.amenities);
    $scope.amenities={};
    createToast("'amenity Added!!'","green");

  }
}])