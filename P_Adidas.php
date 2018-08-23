<?php
require_once 'functions.php';
header('Access-Control-Allow-Origin: *');
$_GET['dbname']="AdidasOld";
$_GET['name']="1";
$_GET['sale']="2"; 
$_GET['base_price']="3";
$_GET['sale_price']="4"; 
$_GET['img_url']="5";
 
// json response array
$response = array("error" => FALSE);
if (isset($_GET['dbname']) && isset($_GET['name']) && isset($_GET['sale']) && isset($_GET['base_price'])
&& isset($_GET['sale_price']) && isset($_GET['img_url'])){
    $dbname = $_GET['dbname'];
    $name = $_GET['name'];
    $sale = $_GET['sale']; 
    $base_price = $_GET['base_price'];
    $sale_price = $_GET['sale_price']; 
    $img_url = $_GET['img_url'];

    $Adidas =  post_Adidas($dbname,$name, $sale, $base_price, $sale_price, $img_url);    
    if ($Adidas != false) {

        $response = array();
        $response["error"] = FALSE;
        $response["Adidas"] = $Adidas;
        
        header('Content-Type: application/json');
        
        echo json_encode($response);
    } else {
      
        $response["error"] = TRUE;
        $response["error_msg"] = "Unknown error occurred!";
        echo json_encode($response);
    }
}
else{
    $response["error"] = TRUE;
    $response["error_msg"] = "Required parameters missing!";
    echo json_encode($response);
}
    
 
    
  
 
   
?>