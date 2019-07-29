angular.module('app', ['angular.filter'])
.controller('adminController',["$scope", "$http", function($scope,$http){
    $scope.package = {};
    $scope.days=[];
    $scope.package_days={};
    $scope.amenities=[];
    $scope.package_amenity={};
    $scope.college={};
    $scope.student={};
    $scope.courses=[];
    $scope.college_courses={};
    $scope.images=[];
    $scope.package_images={};
    $scope.availabilities=[];
    $scope.availability_date={};
    $scope.login={};
    //availability
   
    //end code


    // $scope.counter;

    
    

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
      
            //createToast("'pakage successfully created!!!'","green");

      },
      // failed callback
      function (req) {
        //createToast("'Something went wrong!!!'","red");
      })
    }   



      $scope.addPackage=function(){
        console.log("aaaaaaaaaat");
        console.log("package details",$scope.package);
        sendPostCall('/api/v1/package',$scope.package);
        //createToast("'Pakage Added!!'","green");
      }
      

      $scope.loginCollege=function(){
        console.log("login");
        console.log("login details",$scope.login);
        sendPostCall('/college/login',$scope.login);
        //createToast("'Pakage Added!!'","green");
      }


        $scope.addCollege=function(){
          console.log(" addcollege function working");
          console.log("college details",$scope.college);
          sendPostCall('/api/v1/college', $scope.college);
          //createToast("'College Added!!'","green");
        }




          $scope.addStudent=function(){
            console.log(" addstudent function working");
            console.log("student details",$scope.student);
            sendPostCall('/api/v1/student', $scope.student);
            //createToast("'Data recieved ..proceed to payment !!'","green");
          }




/************************ slider jquery section  ************************************** */

          var i=1;
          // var j=1;
          if(window.screen.availWidth >=440){
            console.log(window.screen.availWidth);
            $( ".flex-next" ).click(function() {
              if($scope.package[0].images.length>10){
               var totalSlides=($scope.package[0].images.length)/10;
              }
              else{
               var totalSlides=1;
              }
              var onSlideImage = (slideIndex+1)%10
              // var lastSlides=totalSlides.toString().split(".")[1]+1;
              // if(onSlideImage==1){
              //   if ((totalSlides-1)>i){
              //     var transform=-800*i;
              //     document.body.style.setProperty('--txx',transform+'px');
              //     $(".demo").css("transform","translate3d(var(--txx), 0px, 0px)");
              //     $scope.currentDiv((i*10)+1);
          
              //     i++;
              //     return i;
              //   } 
              //   else if(((lastSlides)>j)&&((totalSlides-1)<i)){
              //     console.log("2nd if");i-1)));
              //     console.log("transform",transform);
              //     document.body.style.setProperty('--txx',transform+'px');
              //     $(".demo").css("transform","translate3d(var(--txx), 0px, 0px)");
              //     $scope.currentDiv((i*10)+1);
            
              //     j++;
              //     return j;
            
              //   }
               
              // }
              // else if(lastSlides < j) {
              //   console.log("3 rd if");
              //   $(".demo").css("transform","translate3d(0px, 0px, 0px)" );
              //   $scope.currentDiv(1);
              //   j=1;
              //     var transform=-(80*j+(800*(
              //   i=1;
              //   return i;
              //   return j;
              // }
              // else{
              //   slideIndex++;
              //   $scope.currentDiv(slideIndex);
              //   return slideIndex;
              // }
              if(onSlideImage==1){
                if (totalSlides>i){
                  var transform=-800*i;
                  document.body.style.setProperty('--txx',transform+'px');
                  $(".demo").css("transform","translate3d(var(--txx), 0px, 0px)");
                  $scope.currentDiv((i*10)+1);
          
                  i++;
                  return i;
                } 
              }
              else if(totalSlides< i) {
                $(".demo").css("transform","translate3d(0px, 0px, 0px)" );
                $scope.currentDiv(1);
                i=1;
                return i;
              }
              else{
                slideIndex++;
                $scope.currentDiv(slideIndex);
                return slideIndex;
              }
              
            });
            
            $( ".flex-prev" ).click(function() {
              var backSlideImage = (slideIndex)%10
              if (backSlideImage==1){
                if(1<i){
                  i--;
                  var transform =-800*(i-1);
                  document.body.style.setProperty('--txx',transform+'px');
                  $(".demo").css("transform","translate3d(var(--txx), 0px, 0px)");
                  $scope.currentDiv(i*10);
                  return i;
                }
               
              }else{
                if(slideIndex>1){
                  slideIndex--;
                  $scope.currentDiv(slideIndex);
                  return slideIndex;
                }
              }
            });
          
          }
          
          if(window.screen.availWidth <=440){
          
            $( ".flex-next" ).click(function() {
              console.log(window.screen.availWidth);
              if($scope.package[0].images.length>3){
                var totalSlides=($scope.hotel[0].images.length)/3;
               }
               else{
                var totalSlides=1;
               }
              var onSlideImage = (slideIndex+1)%3
          
              if(onSlideImage==1){
                if (totalSlides>i){
                  var transform=-240*i;
                  document.body.style.setProperty('--stx',transform+'px');
                  $(".demo").css("transform","translate3d(var(--stx), 0px, 0px)");
                  $scope.currentDiv((i*3)+1);
          
                  i++;
                  return i;
                } 
              }
              else if(totalSlides< i) {
                $(".demo").css("transform","translate3d(0px, 0px, 0px)" );
                $scope.currentDiv(1);
                i=1;
                return i;
              }
              else{
                slideIndex++;
                $scope.currentDiv(slideIndex);
                return slideIndex;
              }
            });
            
            $( ".flex-prev" ).click(function() {
          
              var backSlideImage = (slideIndex)%3
              if (backSlideImage==1){
                if(1<i){
                  i--;
                  var transform =-240*(i-1);
                  document.body.style.setProperty('--stx',transform+'px');
                  $(".demo").css("transform","translate3d(var(--stx), 0px, 0px)");
                  $scope.currentDiv(i*3);
                  return i;
                }
               
              }else{
                if(slideIndex>1){
                  slideIndex--;
                  $scope.currentDiv(slideIndex);
                  return slideIndex;
                }
              }
            });
          
          }
          /************************************************************************************************/






         
 
            




  $scope.addAnotherDay=function(){
    $scope.days.push($scope.package_days);
    $scope.package_days={};
    $scope.package.days=$scope.days;
    // $scope.counter= 0;
    // $scope.counter += inc;
    // $scope.days.no_of_day=$scope.counter;
    console.log("days",$scope.days);
    //createToast("'Day Added!!'","green");

  }



  $scope.addAmenities=function(){
    $scope.amenities.push($scope.package_amenity);
    $scope.package_amenity={};
    $scope.package.amenities=$scope.amenities;
    console.log("package",$scope.package);
    //createToast("'amenity Added!!'","green")

  }
  $scope.addCourse=function(){
    $scope.courses.push($scope.college_courses);
    $scope.college_courses={};
    $scope.college.courses=$scope.courses;
    console.log("college",$scope.college);
    //createToast("'course Added!!'","green");

  }
  $scope.addImages=function(){
    $scope.images.push($scope.package_images);
    $scope.package_images={};
    $scope.package.images=$scope.images;
    console.log("package",$scope.package);
    //createToast("'course Added!!'","green");

  }
   
  $scope.tripAvailability=function(){
    console.log("function working");
    $scope.availabilities.push($scope.availability_date);
    $scope.availability_date={};
    $scope.package.availabilities=$scope.availabilities;
    console.log("package",$scope.availabilities);
    console.log("function ended");
  }
  
  

}])
.config(['$qProvider', function ($qProvider) {
  $qProvider.errorOnUnhandledRejections(false);
}])

.controller('packagelistController',["$scope", "$http", function($scope, $http, $log) {

  $scope.package = {
    rating : null ,
    star :  null,
    price_start : null,
    price_end : null,
    page: 1
  };
  $scope.min= 0;
  $scope.max= 200000;
  var api_url='http://127.0.0.1:5000';
  var str = document.location.search;
  // var key = str.split("?");
  // var key1 = key[1].split("=");
  // console.log("key1",key1[0]);
  $scope.packageData = [];

$scope.getPackageData = function(cb){
  console.log("filter finction ")
  if(!cb) $scope.package.page = 1;
  
  let searchURL = 'http://127.0.0.1:5000/api/v1/package'
  console.log("searchurl",searchURL);
 
  
  Object.keys($scope.package).forEach(function(param){
    console.log($scope.package[param]);
    if($scope.package[param])
    searchURL += `&${param}=${$scope.package[param]}`;
  });
console.log("automaticccccccccccccccccccccccccccccccccccccccc");
  $http({
    method: 'GET',
    url: 'https://127.0.0.1:5000/api/v1/package'
  }).then(function success(response) {

    // this function will be called when the request is success
    if(cb){
      cb(res);
    }else{
      $scope.packageData = res.data.result.package;
      console.log("$scope.hotelData",$scope.packageData);
    }



    
    }, function error(response) {
    
    // this function will be called when the request returned error status
    
    });

   
    
  }

$scope.getPackageData();
}]);