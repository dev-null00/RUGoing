function createUpcomingEvents() {
                var Dom = YAHOO.util.Dom,
                Event = YAHOO.util.Event,
                myDataSource = null,
                myDataTable = null;
                
                Event.onDOMReady(function() {
                        //defined columns for datatable
                        var myColumnDefs = [
                                {key:"name", sortable:true},
                                {key:"location", sortable:true},
                                {key:"time", sortable:true}
                        ];
                        //end defined columns for datatable
                        myDataSource = new YAHOO.util.DataSource("cgi-bin/dashboard.py?operation=upcoming");
                        myDataSource.responseType = YAHOO.util.DataSource.TYPE_XML;
                        myDataSource.connXhrMode = "queueRequests";
                        myDataSource.connMethodPost = true;
                        myDataSource.responseSchema = {
                                resultNode: "DataTable",
                                fields: ["name","location","time","eventid"]
                        };
                        // DataTable configuration
                        var myConfigs = {
                                initialRequest: ""
                        };

                        myDataTable = new YAHOO.widget.DataTable("upcomingEvents", myColumnDefs,myDataSource,myConfigs);
			myDataTable.subscribe("rowMouseoverEvent", myDataTable.onEventHighlightRow);
			myDataTable.subscribe("rowMouseoutEvent", myDataTable.onEventUnhighlightRow);
			myDataTable.subscribe("rowClickEvent", function(ev) 
			{
				var target = YAHOO.util.Event.getTarget(ev);
				var record = this.getRecord(target);
				window.location = record.getData('eventid');
			}
			);
			myDataTable.selectRow(myDataTable.getTrEl(0));
			myDataTable.focus();			
                });
}

