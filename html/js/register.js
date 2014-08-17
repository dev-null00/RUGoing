// Preload Images
img1 = new Image(16, 16);  
img1.src="images/spinner.gif";
img2 = new Image(220, 19);  
img2.src="images/ajax-loader.gif";

// When DOM is ready
$(document).ready(function(){
	// Launch MODAL BOX if the Login Link is clicked
	$("#register_link").click(function(){
		$('#register_form').modal("daf");
	});
	// When the form is submitted
	$("#status2 > form").submit(function(){  
		// Hide 'Submit' Button
		$('#submit2').hide();
		// Show Gif Spinning Rotator
		$('#ajax_loading').show();
		// 'this' refers to the current submitted form  
		var str = $(this).serialize();  
		str = str + "&operation=register";
		var username = document.getElementById('username2').value;
		//alert(username);
		// -- Start AJAX Call --
		$.ajax({  
    			type: "POST",
    			url: "cgi-bin/homepage.py",  // Send the login info to this page
    			data: str,  
    			success: function(msg){  
				$("#status2").ajaxComplete(function(event, request, settings){  
					// Show 'Submit' Button
					$('#submit2').show();
					// Hide Gif Spinning Rotator
					$('#ajax_loading').hide();  
					//alert(msg);
					//var result=msg;
					var result=msg.getElementsByTagName('registerUser2Result')[0].firstChild.nodeValue.replace(/^\s*|\s*$/g,'');
					//alert(result);
 					if(result == 'true') // LOGIN OK?
 					{  
						var today = new Date();
                                        	var nextMonth = new Date(today.getYear(), today.getMonth()+1, today.getDate());
						//testAlert();
                                        	setCookie("RUGoing", username, nextMonth);
 						var register_response = '<div id="logged_in">' +
	 					'<div style="width: 350px; float: left; margin-left: 70px;">' + 
	 					'<div style="width: 40px; float: left;">' +
	 					'<img style="margin: 10px 0px 10px 0px;" align="absmiddle" src="images/ajax-loader.gif">' +
	 					'</div>' +
	 					'<div style="margin: 10px 0px 0px 10px; float: right; width: 300px;">'+ 
	 					"You are successfully registered! <br /> Please wait while you're redirected...</div></div>";  
						$('a.modalCloseImg').hide();  
						$('#simplemodal-container').css("width","500px");
						$('#simplemodal-container').css("height","120px");
 						$(this).html(register_response); // Refers to 'status'
						// After 3 seconds redirect the 
						setTimeout('go_to_private_page()', 3000); 
 					}  
 					else // ERROR?
 					{  
 						var register_response = "Username has been taken";
 						$('#register_response').html(register_response);
 					}  
 				});  
 			}  
			//error: function(){
			//	alert("hello");
			//	var login_response = "Service is currently down please try again later";
			//	$('#login_response').html(login_response);
			//}
			//error: function(xhr,err){
    			//	alert("readyState: "+xhr.readyState+"\nstatus: "+xhr.status);
    			//	alert("responseText: "+xhr.responseText);
			//}
  		});  
		// -- End AJAX Call --
		return false;
	}); // end submit event
});

function go_to_private_page()
{
	window.location = 'dashboard.html'; // Members Area
}
