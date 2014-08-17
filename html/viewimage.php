<?php
	include "include.php";
	dbconnect();
	if(isset($_COOKIE['ID_my_site']))
	{
		while (@ob_end_clean());
		/*** some basic sanity checks ***/
		if(filter_has_var(INPUT_GET, "image_id") !== false && filter_input(INPUT_GET, 'image_id', FILTER_VALIDATE_INT) !== false)
    	{
    	/*** assign the image id ***/
			$image_id = filter_input(INPUT_GET, "image_id", FILTER_SANITIZE_NUMBER_INT);
			
			$sql = "SELECT image, image_type, image_size FROM photo WHERE image_id=$image_id";//getting image based on imageid
			$stmt1=mysql_query($sql) or die(mysql_error());
			
			if(mysql_num_rows($stmt1) == 1)
	        {
	        	
				$image = mysql_fetch_array($stmt1);
				$imageData=$image['image'];
				
				/*** set the headers and display the image ***/
				header("Content-type: image/jpeg");
         		/*** output the image ***/
				echo $imageData;
            }
			else
			{
				
			}
			
        }
		else
        {

        }
	}
	else
	{
		header("Location:homepage.php");
	}
	
?>