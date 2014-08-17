$(function() {
        $("#submitmod").click(function() {
		var szName = getCookie("RUGoing");
                var firstname = $("input#firstname").val();
                var lastname = $("input#lastname").val();
                var oldpassword = $("input#oldpassword").val();
                var newpassword = $("input#newpassword").val();
                var interest = $("input#interests").val();
                var dataString ='operation=modify&firstname='+firstname+'&lastname='+lastname+'&oldpassword='+oldpassword+'&newpassword='+newpassword+'&interest='+interest+'&username='+szName;
                $.ajax({
                        type: "POST",
                        url: "cgi-bin/dashboard.py",
                        data: dataString,
                        success: function(msg) {
				//check the result for true
				var result=msg.getElementsByTagName('modifyUserResult')[0].firstChild.nodeValue.replace(/^\s*|\s*$/g,'');
				if(result == 'true') // Modify OK?
				{
                                	alert("modify successful");
				}
				else {
                                	alert("modify failed");
				}
                                return true;
                        }
                });
                return false;
        });
});

