<link type="text/css" rel="stylesheet" href="http://yui.yahooapis.com/2.8.2r1/build/carousel/assets/skins/sam/carousel.css"> 
	<script src="http://yui.yahooapis.com/2.8.2r1/build/yahoo/yahoo-dom-event.js"></script> 
	<script src="http://yui.yahooapis.com/2.8.2r1/build/element/element-min.js"></script> 
	<script src="http://yui.yahooapis.com/2.8.2r1/build/carousel/carousel-min.js"></script> 
	
	var my_url="viewimage.php?q="
	<div id="container"> 
	    <ol id="carousel"> 
	        <li> 
	            <img src="my_url" 
	                width="75" height="75"> 
	        </li> 
	
	
	/* Always be sure to give your carousel items a width and a height */  
	.yui-carousel-element li { 
	    width: 75px; 
	    height: 75px; 
	} 
	
	.yui-carousel-element .yui-carousel-item-selected { 
	    border:0; /* Override selected item's dashed border so it feels more like a photo album */ 
	} 
	
	#container { 
	    position: relative; 
	} 
	
	.yui-carousel-pagination { 
	    position:absolute; 
	    left:0.7ex; /* relative to div#container */  
	    top:2.364ex; 
	    width:88px; 
	    height:12px; 
	    text-align:left; 
	    font-size:76%; 
	} 
	
	.yui-skin-sam .yui-carousel .yui-carousel-nav ul { 
	    /* Since we're taking up space with the paging text, adjust the position of the page nav for IE6/7 */ 
	    *margin-left:-140px; 
	} 
	
	
	YAHOO.util.Event.onDOMReady(function (ev) { 
	    carousel    = new YAHOO.widget.Carousel("container", { 
	        // turn on multi-row to use in this example by passing an array of rows and cols 
	        numVisible: [3, 2] 
	    }); 
	     
	    // register our text and/or HTML pagination template with embedded Carousel {tokens} 
	    carousel.registerPagination("<strong>Image</strong> {firstVisible} - {lastVisible} <strong>of</strong> {numItems}"); 
	 
	    carousel.render(); // get ready for rendering the widget 
	    carousel.show();   // display the widget 
	}); 