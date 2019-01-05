<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Smart Traffic Lights</title>
	<style type="text/css">
	.auto-style3 {
		color: #EE571C;
	}
	.auto-style5 {
		color: #EA6B82;
		font-size: xx-large;
	}
	</style>
</head>

<link rel="stylesheet" type="text/css" href="default.css">

<div id="header">
  <h1><br> <span class="auto-style5">Traffic States</span></h1>
</div>


<body bgcolor="#FFE8E8"> 
<input id="origin-input" class="controls" type="text" placeholder="Enter an origin location">
<input id="destination-input" class="controls" type="text" placeholder="Enter a destination location">
        
<div id="modeselector" class="controls">
  <input type="radio" name="type" id="changemode-driving" checked="checked">
  <label for="changemode-driving">Driving</label>

  <input type="radio" name="type" id="changemode-transit">
  <label for="changemode-transit">Bus</label>

  <input type="radio" name="type" id="changemode-walking">
  <label for="changemode-walking">Walking</label>
</div>


<div id="map"></div>
 
<div id="side">
	<form action="calltest.php" name="form" id="form" method="post">
		<b>First point:</b>
		<input name="ConstructionADD" type="text" id="ConstructionADD" size="33" maxlength="50" onchange="codeAddress()"/>
		<b>Second point:</b>
		<input name="ConstructionADD2" type="text" id="ConstructionADD2" size="33" maxlength="50" onchange="codeAddress2()"/>
		<b>Time:</b>
		<select name="time">
			<option value="0">0</option>
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
			<option value="11">11</option>
			<option value="12">12</option>
			<option value="13">13</option>
			<option value="14">14</option>
			<option value="15">15</option>
			<option value="16">16</option>
			<option value="17">17</option>
			<option value="18">18</option>
			<option value="19">19</option>
			<option value="20">20</option>
			<option value="21">21</option>
			<option value="22">22</option>
			<option value="23">23</option>
			<option value="24">24</option>
		</select>
		<p align="left">
		<b>Firstpoint Lat:</b>
		<input name="Latitude" type="text" id="Latitude" size="25" maxlength="15" readonly="readonly"/><br>
		<b>Firstpoint Lng:</b>
		<input name="Longitude" type="text" id="Longitude" size="25" maxlength="15" readonly="readonly"/></p><br>
		<b>Secondpoint Lat:</b>
		<input name="Latitude2" type="text" id="Latitude2" size="25" maxlength="15" readonly="readonly"/><br>
		<b>Secondpoint Lng:</b>
		<input name="Longitude2" type="text" id="Longitude2" size="25" maxlength="15" readonly="readonly"/><br><br>
		
		<input type="submit" name="submit" value="submit" style="background-color:#4d90fe;">
		<input type="reset"  name="empty" value="empty" style="background-color:#4d90fe;"><br><br>
	</form> 
</div>

<div id="footer">
	<h2>SMART TRAFFIC LIGHTS 2018 @NTCU</h2>
</div>


 
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAoAHgmSDPtCoOHfigh_mhfminLJEO_Ihw&libraries=places&alternatives=true&callback=initMap"></script>
<script src="default.js"></script>
<?php
    if(isset($_POST['Ntokm']))
        echo "<input id='Ntokm' type='hidden' value='".$_POST['Ntokm']."'>";
    if(isset($_POST['Nfromkm']))
        echo "<input id='Nfromkm' type='hidden' value='".$_POST['Nfromkm']."'>";
    if(isset($_POST['Etokm']))
        echo "<input id='Etokm' type='hidden' value='".$_POST['Etokm']."'>";
    if(isset($_POST['Efromkm']))
        echo "<input id='Efromkm' type='hidden' value='".$_POST['Efromkm']."'>";
    if(isset($_POST['value']))
        echo "<input id='value' type='hidden' value='".$_POST['value']."'>";
    echo "<script>drawpoly();</script> "; 
?>
</body>
</html>

