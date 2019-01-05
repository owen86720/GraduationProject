var url_trafficlight = 'https://raw.githubusercontent.com/goish135/GPro/master/traffic_light.json';
var c=0;
var t;
var now_url = location.href;
var image1={url:'red.ico',};


var map = new google.maps.Map(document.getElementById("map"),{
      center: {lat: 24.1436581, lng: 120.6696387},
      zoom: 17,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

function initialize() {
	var directionsService = new google.maps.DirectionsService();
    var directionsDisplay = new google.maps.DirectionsRenderer();
    
    /*
    var map = new google.maps.Map(document.getElementById("map"),{
      center: {lat: 24.1436581, lng: 120.6696387},
      zoom: 17,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });*/
    
        
 
/*        
    var image1={
    url:'red.ico',
    };
    var trafficlight = [
     {
          position : { lat: 24.145406,  lng: 120.671333 },
          map:map,
          icon:image1,
          title:'Traffic light'
     },
     {
          position : { lat: 24.143958,  lng: 120.669818 },
          map:map,
          icon:image1,
          title:'Traffic light'
     },
     {
          position : { lat: 24.141948,  lng: 120.672098},
          map:map,
          icon:image1,
          title:'Traffic light'
     },
     {
          position : { lat: 24.143362,  lng: 120.673606 },
          map:map,
          icon:image1,
          title:'Traffic light'
     },
     {
          position : { lat: 24.142822,  lng: 120.674278 },
          map:map,
          icon:image1,
          title:'Traffic light'
     },
     {
          position : { lat: 24.141699,  lng: 120.675505 },
          map:map,
          icon:image1,
          title:'Traffic light'
     },
     {
          position : { lat: 24.145030,  lng: 120.671832 },
          map:map,
          icon:image1,
          title:'Traffic light'
     },
     {
          position : { lat: 24.144576,  lng: 120.672365 },
          map:map,
          icon:image1,
          title:'Traffic light'
     },
     {
          position : { lat: 24.143149,  lng: 120.673881 },
          map:map,
          icon:image1,
          title:'Traffic light'
     }
    ];
     
    for (var i= 0; trafficlight.length >i ; i++) {
        var marker = new google.maps.Marker(trafficlight[i]);
    }*/
    
     
    getDirections(map);

}

//marker移動

/*function moveMarker(map, marker, latlng) {
    marker.setPosition(latlng);
    map.panTo(latlng);
}

function autoRefresh(map, pathCoords) {
    var i, route, marker;
    
    route = new google.maps.Polyline({
        path: [],
        geodesic : true,
        strokeColor: '#A500CC',
        strokeOpacity: 1.0,
        strokeWeight: 2,
        editable: false,
        map:map
    });
    
    var image2={
    url:'carbig.ico',
    };
    marker=new google.maps.Marker({map:map, icon:image2});

    for (i = 0; i < pathCoords.length; i++) {                
        setTimeout(function(coords) {
            route.getPath().push(coords);
            moveMarker(map, marker, coords);
        }, 3000 * i, pathCoords[i]);
    }
}*/

function getDirections(map) {
    var directionsService = new google.maps.DirectionsService();

    var request = {
        origin: new google.maps.LatLng(24.145395, 120.671326),
        destination: new google.maps.LatLng(24.139352, 120.676666),
        travelMode: google.maps.TravelMode.DRIVING
    };
    directionsService.route(request, function(result, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            autoRefresh(map, result.routes[0].overview_path);
        }
    });

 
new AutocompleteDirectionsHandler(map);


}

//以上為 initialize function************************


//輸入地址導航

function AutocompleteDirectionsHandler(map) {
  this.map = map;
  this.originPlaceId = null;
  this.destinationPlaceId = null;
  this.travelMode = 'DRIVING';
  var originInput = document.getElementById('origin-input');
  var destinationInput = document.getElementById('destination-input');
  var modeSelector = document.getElementById('mode-selector');
  this.directionsService = new google.maps.DirectionsService;
  this.directionsDisplay = new google.maps.DirectionsRenderer;
  this.directionsDisplay.setMap(map);

  var originAutocomplete = new google.maps.places.Autocomplete(
      originInput, {placeIdOnly: true});
  var destinationAutocomplete = new google.maps.places.Autocomplete(
      destinationInput, {placeIdOnly: true});
      
  this.setupClickListener('changemode-driving', 'DRIVING');
  this.setupClickListener('changemode-transit', 'TRANSIT');
  this.setupClickListener('changemode-walking', 'WALKING');

  this.setupPlaceChangedListener(originAutocomplete, 'ORIG');
  this.setupPlaceChangedListener(destinationAutocomplete, 'DEST');

  this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(originInput);
  this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(destinationInput);
  this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(modeSelector);
}


// 變更選擇位置
// 自動填寫
AutocompleteDirectionsHandler.prototype.setupClickListener = function(id, mode) {
  var radioButton = document.getElementById(id);
  var me = this;
  radioButton.addEventListener('click', function() {
    me.travelMode = mode;
    me.route();
  });
};

AutocompleteDirectionsHandler.prototype.setupPlaceChangedListener = function(autocomplete, mode) {
  var me = this;
  autocomplete.bindTo('bounds', this.map);
  autocomplete.addListener('place_changed', function() {
    var place = autocomplete.getPlace();
    if (!place.place_id) {
      window.alert("Please select an option from the dropdown list.");
      return;
    }
    if (mode === 'ORIG') {
      me.originPlaceId = place.place_id;
    } else {
      me.destinationPlaceId = place.place_id;
    }
    me.route();
  });

};

AutocompleteDirectionsHandler.prototype.route = function() {
  if (!this.originPlaceId || !this.destinationPlaceId) {
    return;
  }
  var me = this;

  this.directionsService.route({
    origin: {'placeId': this.originPlaceId},
    destination: {'placeId': this.destinationPlaceId},
    travelMode: this.travelMode
  }, function(response, status) {
    if (status === 'OK') {
      me.directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
};


//取得座標

function codeAddress(){
	var add = document.getElementById("ConstructionADD");
	var Latitude = document.getElementById("Latitude");
	var Longitude = document.getElementById("Longitude");
	var geocoder = new google.maps.Geocoder();
 
	geocoder.geocode( { address: add.value}, function(results, status) {
		if (status == google.maps.GeocoderStatus.OK) {
			Latitude.value = results[0].geometry.location.lat();
			Longitude.value = results[0].geometry.location.lng();	
		}
		else {
			alert("Start geocode was not successful for the following reason: " + status);
		}
	});
}

function codeAddress2(){
	var add = document.getElementById("ConstructionADD2");
	var Latitude2 = document.getElementById("Latitude2");
	var Longitude2 = document.getElementById("Longitude2");
	var geocoder = new google.maps.Geocoder();

	geocoder.geocode( { address: add.value}, function(results, status) {
		if (status == google.maps.GeocoderStatus.OK) {
			Latitude2.value = results[0].geometry.location.lat();
			Longitude2.value = results[0].geometry.location.lng();	
		}
		else {
			alert("End geocode was not successful for the following reason: " + status);
		}
	});
}

 
//設定polylinec和infowindow


function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
};

function getRandomNumber() {
	
    var random = 0.3;
	random += (Math.floor(Math.random()*5)/100);
    
    return random;
};


function drawpoly(){
	var Ntokm_element = document.getElementById('Ntokm');
	var Ntokm = Ntokm_element.value.split(" ");
	var Nfromkm_element = document.getElementById('Nfromkm');
	var Nfromkm = Nfromkm_element.value.split(" ");
	var Etokm_element = document.getElementById('Etokm');
	var Etokm = Etokm_element.value.split(" ");
	var Efromkm_element = document.getElementById('Efromkm');
	var Efromkm = Efromkm_element.value.split(" ");
    var speed_element = document.getElementById('value');
	var speed = speed_element.value.split(" ");
	var Ndrawpath=[];
	var Edrawpath=[];
    var marker=[];
    var lineSymbol = {
        path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW
	};
	
	for(var i=0;i<(Ntokm.length);i++){
		Ndrawpath[i]=new google.maps.LatLng(Ntokm[i],Etokm[i]);
		Edrawpath[i]=new google.maps.LatLng(Nfromkm[i],Efromkm[i]);
	}
	for (var i=0;i<(Ntokm.length);i++) {
		var PathStyle = new google.maps.Polyline({
    		path:  [Ndrawpath[i],Edrawpath[i]],
    		strokeColor: getRandomColor(),
    		strokeOpacity: 1.0,
    		strokeWeight: 3,
    		icons: [{
				icon:lineSymbol,
				strokeColor:'#000000',
		        strokeOpacity: 1.0,
				offset: '100%'
			}],
    		map: map
  		});
  		PathStyle.setMap(map);
	}
	//
	for(var i=0;i<(Ntokm.length);i++){
		marker[i] = new google.maps.Marker({
			position: Ndrawpath[i],
			map: map,
			icon: image1,
			title: 'Traffic light'
		});
	}
	
	
	//marker.setMap(map);
  for (var i=0;i<(Ntokm.length);i++) {
	  var temp =getRandomNumber();
	  var remain = 1-temp;
	  //alert(temp);
	  //alert(remain);
      if(speed[i]!="NULL"){
          var num = new Number(speed[i]);
          speed[i] = num.toFixed(2);
      }
	  	var infowindow = new google.maps.InfoWindow({
	    	content: speed[i],
	        position: new google.maps.LatLng((parseFloat(Ntokm[i])*temp+parseFloat(Nfromkm[i])*remain),(parseFloat(Etokm[i])*temp+parseFloat(Efromkm[i])*remain)),	    
			maxWidth:70
	  	});
		infowindow.open(map);
	  }
	

}



google.maps.event.addDomListener(window, 'load', initialize);





//key=https://maps.googleapis.com/maps/api/js?key=AIzaSyAoAHgmSDPtCoOHfigh_mhfminLJEO_Ihw&libraries=places&callback=initMap
 
/*function draw() {
	var oform = document.forms['form'];
	var firstpoint= new google.maps.LatLng(oform.elements['Latitude'].value,oform.elements['Longitude'].value);
	var secondpoint= new google.maps.LatLng(oform.elements['Latitude2'].value,oform.elements['Longitude2'].value);	
	alert('First point: '+firstpoint + '\nSecond point: '+secondpoint);
 	var PathStyle = new google.maps.Polyline({
    	path: [firstpoint,secondpoint],
    	strokeColor: red,
    	strokeOpacity: 1.0,
    	strokeWeight: 2,
    	map: map
  	});
	PathStyle.setMap(map);
}*/


/*function parameters(){
	if(now_url.indexOf("?")!=-1){
       	var url_array = now_url.split("?");
		var url_array = now_url.split("?");
    	var parameter_array = url_array[1].split("&");
    	var result_array = parameter_array[0].split("=");
    	var id = result_array[1];
        alert(id);
     }
     else{
     	alert('No parameters');
     }
}*/

/*function forparameters(){
	if(now_url.indexOf('?')!=-1){
	    var id = "";
	    var name = "";
	    var value_array = now_url.split('?')[1].split('&');
	    for(i=0;i<=(value_array.length)-1;i++)
	    { 
	        if(value_array[i].split('=')[0] == 'id'){
	            id = value_array[i].split('=')[1];
	    	}
	    	if(value_array[i].split('=')[0] == 'name'){
	            name = value_array[i].split('=')[1];
	    	}
	    }
	    alert(id+"  "+name);	
	}
	else{
		alert('No parameters');
	}
}*/

