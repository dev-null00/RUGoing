(function () {
        // Get the image link from within its (parent) container.
        function getImage(parent) {
            var el = parent.firstChild;
                    
            while (el) { // walk through till as long as there's an element
                if (el.nodeName.toUpperCase() == "IMG") { // found an image
                    // flickr uses "_s" suffix for small, and "_m" for big
                    // images respectively
                    return el.src.replace(/_s\.jpg$/, "_m.jpg");
                }
                el = el.nextSibling;
            }
            
            return "";
        }
                
        YAHOO.util.Event.onDOMReady(function (ev) {
            var spotlight   = YAHOO.util.Dom.get("spotlight"),
                carousel    = new YAHOO.widget.Carousel("photocontainer");
                       
            carousel.on("itemSelected", function (index) {
                // item has the reference to the Carousel's item
                var item = carousel.getElementForItem(index);
 
                if (item) {
                    spotlight.innerHTML = "<img src=\""+getImage(item)+"\" style=\"width:75%;height:75%;\">";
                }
            });
                
            carousel.render(); // get ready for rendering the widget
            carousel.show();   // display the widget
        });
    })(); 
