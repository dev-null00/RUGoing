<?php session_register('albumID');

	if(isset($_COOKIE['ID_my_site']))
	{
		include "include.php";
		dbconnect();
		
		$otherUser=0;
		$uploadTried=0;
		$currentUserName=$_COOKIE['ID_my_site'];
		$currentUserIDQuery=mysql_query("SELECT userID FROM user WHERE userName='".$currentUserName."'");
		$currentUserIDRow=mysql_fetch_array($currentUserIDQuery);
		$currentUserID=$currentUserIDRow['userID'];
		if($_GET['userID'])
		{
			$userID=$_GET['userID'];
			if($userID!=$currentUserID) $otherUser=1;
		}
		else
		{
			$userID=$currentUserID;
		}
		
		if($_GET['albumID'])
		{
			$albumID=$_GET['albumID'];
		}
		else
		{
			$albumID=$_SESSION['albumID'];
		}
		/*** Check the $_GET variable ***/

		if($_POST['UploadImage'])
		{
			
			$uploadTried=1;
			if(!isset($_FILES['userfile']))
			{
				$uploadErrorMessage="Please Select an Image.";
			}
			else
			{
				
				/*** check if a file is uploaded ***/
				if(is_uploaded_file($_FILES['userfile']['tmp_name']) && getimagesize($_FILES['userfile']['tmp_name']) != false)
				{
    				/***  get image info. ***/
					$size = getimagesize($_FILES['userfile']['tmp_name']);
    				/*** assign variables ***/
					$type = $size['mime'];
					$imageSizeData=$size[3];
					$fp=fopen($_FILES['userfile']['tmp_name'],'r');
	
					$imgfp=fread($fp, filesize($_FILES['userfile']['tmp_name']));
					$imageData=addslashes($imgfp);

					$size = filesize($_FILES['userfile']['tmp_name']);
					$name = $_FILES['userfile']['name'];
					$maxsize = 600000;
		
					if(get_magic_quotes_gpc())
						$imageData=$imgfp;
					else
						$imageData=mysql_real_escape_string($imgfp);
   					/*** check if file is less than the max file size ***/
  		  			if($_FILES['userfile']['size'] < $maxsize )
        			{
						$albumID = $_SESSION['albumID'];
						// inserting image and image information in the table
						$insertQuery="INSERT INTO photo (image_type , image_size, image_name, albumID, userID, image) VALUES ('".$type."', '".$imageSizeData."', '".$name."', '".$albumID."', ".$userID.", '".$imageData."')";
						
						$stmt1=mysql_query($insertQuery) or die(mysql_error());
						$uploadErrorMessage="Sucessfully uploaded.";
        			}
        			else
        			{
        				$uploadErrorMessage="Maximum image size is 550KB.";
        			}	
				}
			}
		}
		
		$albumNameQuery= "SELECT name FROM album WHERE albumID=".$albumID;
		$albumNameQueryResult=mysql_query($albumNameQuery);
		$albumNameRow=mysql_fetch_array($albumNameQueryResult);
		$albumName=$albumNameRow['name'];

    		// getting imageid, imagetype, image based on particular albumID
    	$imageListQuery = "SELECT image_id, image_type, image_name FROM photo WHERE albumID=".$albumID;

        /*** prepare the sql ***/
		$imageListQueryResult=mysql_query($imageListQuery);
		echo "<a href=albumlist.php>Back to Albums</a>";
		echo "<center><h2>Now viewing :".$albumName."</h2><table>";
		echo "<tr><td>No. of Images: ".mysql_num_rows($imageListQueryResult)."</td></tr>";
   		while($imageDetail=mysql_fetch_array($imageListQueryResult))
		{
			$image="viewimage.php?image_id=".$imageDetail['image_id'];
			echo "<tr><td>";
           	echo '<img src="viewimage.php?image_id='.$imageDetail['image_id'].'" height=200 width=200></img>';
           	
           	echo "</td></tr><tr><td>".$imageDetail['image_name'].'</tr></td>';
           
		}
		echo "</table></center>";
		
		
		if($otherUser!=1)
		{
?>		
	<center>
	<form method="post" action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" enctype="multipart/form-data">
		Select Image File:
		<input type="file" name="userfile"  size="40">
		<input type="hidden" name="MAX_FILE_SIZE" value="6000000">
		<br />
		<input type="submit" value="Upload" name="UploadImage">
	</form>		
	
<?php 	
			if($uploadTried==1)
			{
				echo "<br />".$uploadErrorMessage;	
			}
	echo "</center>";	
		}
	
	}
?>