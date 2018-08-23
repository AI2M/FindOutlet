<?php
 
require_once 'functions.php';
header('Access-Control-Allow-Origin: *');
 
// json response array
$response = array("error" => FALSE);
// $postdata = file_get_contents("php://input");
// $postdata = json_decode($postdata);

$postdata->dbname = "AdidasOld";
$postdata->name = "name1";
$postdata->sale = "50";
$postdata->base_price = "100";
$postdata->sale_price = "50";
$postdata->img_url = "www.ppp.com";
 
if (isset($postdata->dbname) && isset($postdata->name)  && isset($postdata->sale)  
&& isset($postdata->base_price)&& isset($postdata->sale_price) && isset($postdata->img_url)) {
 
    // receiving the post params

    $dbname  = $postdata->dbname;
    $name = $postdata->name;
    $sale = $postdata->sale; 
    $base_price = $postdata->base_price; 
    $sale_price = $postdata->sale_price; 
    $img_url = $postdata->img_url;
        // create a new user
        $Adidas =  get_Adidas($dbname,$name, $sale, $base_price, $sale_price, $img_url);    
        if ($Adidas) {
            $response = array();
            $response["error"] = FALSE;
            $response["Adidas"] = $Adidas;
            
            header('Content-Type: application/json');
            //$ar =array("gg"=>"bb");
            echo json_encode($response);
        } else {
            // user failed to store
            $response["error"] = TRUE;
            $response["error_msg"] = "Unknown error occurred!";
            echo json_encode($response);
        }
    
} else {
    $response["error"] = TRUE;
    $response["error_msg"] = "Required parameters missing!";
    echo json_encode($response);
}
?>