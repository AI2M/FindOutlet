<?php
	/**
	*Database config variables
    */
    /*
    define("DB_HOST","605309c4-e07e-4c43-995a-a8140093a394.mysql.sequelizer.com");
	define("DB_USER","bucvgnslopvtkrfh");
	define("DB_PASSWORD","2mdxLMDW5ZdtdVbxJVvDjizAYkqMtiqtvPYm7Joxrr5xBwxWJBkJuRhSTKFzwYBV");
	define("DB_DATABASE","db605309c4e07e4c43995aa8140093a394");
	$connection = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);
	if(mysqli_connect_errno()){
		die("Database connnection failed " . "(" .
			mysqli_connect_error() . " - " . mysqli_connect_errno() . ")"
				);
    }*/
    $servername = "a2493b78-cdb2-4f15-8776-a812008fb298.mysql.sequelizer.com";
    $username = "orpjqgdwunagzyuf";
    $password = "YgY8KwG3DShvLK4wNC7GyCg5iGGtX7S5dGQyESuXzfKzy6eCjevB7sjua4YdXndF";
	$dbname = "dba2493b78cdb24f158776a812008fb298";
	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error){
		die("Connection failed: " . $conn->connect_error);
	}
?>