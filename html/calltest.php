<?php
    //if($_POST)
    $y1 = $_POST['Latitude'];
    $y2 = $_POST['Latitude2'];
    $x1 = $_POST['Longitude'];
    $x2 = $_POST['Longitude2'];
    $time = $_POST['time'] * 60;
    //echo($time."<BR>");
    set_include_path(get_include_path() . PATH_SEPARATOR . 'phpseclib');
    include('Net/SSH2.php');
    $ssh = new Net_SSH2('120.108.204.6','3389');
    if (!$ssh->login('user', 'ntcuk201')) {
        exit('Login Failed');
    }
    $ssh->setTimeOut(3000);
    $temp = $ssh->exec('python3 GraduationProject/run.py '.$x1.' '.$x2.' '.$y1.' '.$y2.' '.$time);
    //echo 'python3 GraduationProject/test.py '.$x1.' '.$x2.' '.$y1.' '.$y2.' '.$time;
    //echo $temp;
    $route = substr($temp,strrpos($temp,"{")+1,strrpos($temp,"}")-strrpos($temp,"{")-1);
    $route = str_replace("'","",$route);
    $route = str_replace(" ","",$route);
    $route = explode(",",$route);
    //echo "<BR>";
    $speed = substr($temp,strrpos($temp,"[[")+2,strrpos($temp,"]]")-strrpos($temp,"[[")-2);
    //echo $speed."<BR>";
    $speed = explode(" ",$speed);
    print_r($route);
    print_r($speed);
    $link = mysqli_connect("", "", "", "") or die("無法開啟MySQL資料庫連接!<br/>"); // 與GPU server連線
    mysqli_query($link, 'SET NAMES utf8');
    
    $Ntokm = array();
    $Nfromkm = array();
    $Etokm = array();
    $Efromkm = array();
    $value = array();
    $count = 0;
    foreach($route as $tem){
        //echo $tem."<BR>";
        $sql = "SELECT * FROM RoadInfo where ID = '".$tem."'";
        $result = mysqli_query($link, $sql);
        if(!$result){
            echo ("Error: ".mysqli_error($link));
            exit();
        }
        $row = mysqli_fetch_array($result);
        array_push($Ntokm,$row["Ntokm"]);
        array_push($Nfromkm,$row["Nfromkm"]);
        array_push($Etokm,$row["Etokm"]);
        array_push($Efromkm,$row["Efromkm"]);
        echo $speed[$count+1]."<BR>";
        array_push($value,$speed[$count+1]);
        $count+=2;
    }
    $Ntokm = implode(" ",$Ntokm);
    $Nfromkm = implode(" ",$Nfromkm);
    $Etokm = implode(" ",$Etokm);
    $Efromkm = implode(" ",$Efromkm);
    $value = implode(" ",$value);
    
?>
<body onload="go()">
    <form action="default.php" method="post" id='myform'>
        <input type="hidden" name="Ntokm" value="<?=$Ntokm?>">
        <input type="hidden" name="Nfromkm" value="<?=$Nfromkm?>">
        <input type="hidden" name="Etokm" value="<?=$Etokm?>">
        <input type="hidden" name="Efromkm" value="<?=$Efromkm?>">
        <input type="hidden" name="value" value="<?=$value?>">
    </form>
</body>
<script language="javascript">
    function go(){
        document.getElementById("myform").submit();
    }
</script>