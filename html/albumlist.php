<?php
	session_start();

	include "include.php";
	dbconnect();

	if(isset($_COOKIE['ID_my_site']))
	{
		$currentUserName=$_COOKIE['ID_my_site'];
		$currentUserIDQuery=mysql_query("SELECT userID FROM user WHERE userName='".$currentUserName."'"); // getting current userID
		$currentUserIDRow=mysql_fetch_array($currentUserIDQuery);
		$currentUserID=$currentUserIDRow['userID'];
		if(isset($_POST['createAlbum']) )
			{ 
				if(!$_POST['createAlbumName'] )
				{
					echo '<i>Album name cannot be blank!</i>';
					albumOptions();
				}
				else
				{
				try 
				{
					$stmt =mysql_query("INSERT INTO album (name, userID) VALUES ('".$_POST['createAlbumName']."',".$currentUserID.")");	 // insert  current userID and albumname   
	        		upload($_POST['createAlbumName']);        
        		}
    			catch(PDOException $e)
        		{
    				echo '<h4>'.$e->getMessage().'</h4>';
        		}
    			catch(Exception $e)
        		{
        			echo '<h4>'.$e->getMessage().'</h4>';
        		}	
			}
		}

		else
		{
       		albumOptions($currentUserID);
		}	
	 //
	}

	function albumOptions($currentUserID)
	{
		$stmt2=mysql_query("SELECT name,albumID FROM album WHERE userID=".$currentUserID); //getting name, albumID of current users
		echo "<form action=".$_SERVER['PHP_SELF']." method=post>";
		if($stmt2)
		{       
        	echo "Albums Available";
        	
        	$nt=mysql_fetch_array($stmt2);//Array or records stored in $nt
			
        	while($nt=mysql_fetch_array($stmt2))
        	{//Array or records stored in $nt
				echo "<br /><a href=viewalbum.php?".$nt[albumID].">".$nt[name]."</a>";
        	}
        	
		}
		echo "<br />Enter new album name:";
		echo "<input type=text name=\"createAlbumName\" />";
		echo "<input type=submit name=createAlbum value=\"Create Album\" />";

	}

	function upload($albumname)
	{

		//$stmt1=mysql_query("SELECT albumID FROM album where name = '".$albumname."' ");

		
		$queryStatement="SELECT albumID FROM album WHERE name = '$albumname'"; //getting albumID
		echo $queryStatement;
		$albumIDlist=mysql_query($queryStatement) or die(mysql_error());
    	session_register($albumID);
        while($albumIDEntry=mysql_fetch_array($albumIDlist))
        {
        	$albumID=$albumIDEntry['albumID'];
        }
        

        $_SESSION['albumID']=$albumID;
      	header("Location: viewalbum.php");	
	}
?> 	