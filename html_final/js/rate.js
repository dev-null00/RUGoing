$(function() {
	$('#click').raty({
		onClick: function(score) {
			//send the rating to the server to save
			var szName = getCookie("RUGoing");
	                var eventID = $("input#eventID").val();
	                var dataString ='operation=rate&rating='+score+'&eventID='+eventID+'&username='+szName;


			$.ajax({
                        type: "POST",
                        url: "cgi-bin/dashboard.py",
                        data: dataString,
                        success: function(msg) {
				//check the result for true
				var result=msg.getElementsByTagName('rateEventResult')[0].firstChild.nodeValue.replace(/^\s*|\s*$/g,'');
				if(result == 'true') // Modify OK?
				{
                                	alert("Thank You for Rating this Event");
				}
				else {
                                	alert("Rating Failed");
				}
                                return true;
                        }
                });
		}
	});
})();
