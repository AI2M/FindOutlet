<?php require_once("connect.php");?>
<?php
function getDateAndBuilding($date,$building){
    global $conn;
    $query = "SELECT * from visit WHERE visit_date=$date AND visit_building=$building ";
    $dateAndBuilding = mysqli_query($conn, $query);
    $data = array();
    if($dateAndBuilding){
        while ($res = mysqli_fetch_assoc($dateAndBuilding)){
            array_push($data,$res);
        }
        return $data;
    }
    else{
        return false;
    }
}

function post_Adidas($dbname,$name, $sale, $base_price, $sale_price, $img_url){
    global $connection;
    $query = "INSERT INTO AdidasOld";
    $query .= "(name, sale, base_price, sale_price, img_url) ";
    $query .= "VALUES('{$name}', '{$sale}','{$base_price}','{$sale_price}','{$img_url}')";
    $result = mysqli_query($connection, $query);
    $data = array();
    
    if($result){
        $query2 = "SELECT * FROM {$dbname} WHERE name = '{$name}'";
        $getdata = mysqli_query($connection, $query2);
        if($getdata){
            while ($res = mysqli_fetch_assoc($getdata)){
                array_push($data,$res);
            }
            return $data;
        }else{
                return false;
            }
        }
        else{
            return false;
        }
}

   
?>