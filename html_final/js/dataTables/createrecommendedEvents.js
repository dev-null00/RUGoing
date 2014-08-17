function createrecommendedEvents() {
                var Dom = YAHOO.util.Dom,
                Event = YAHOO.util.Event,
                myDataSource = null,
                myDataTable = null;
		var szName = getCookie("RUGoing");                
                Event.onDOMReady(function() {
                        //defined columns for datatable
                        var myColumnDefs = [
                                {key:"name", sortable:true},
                                {key:"location", sortable:true},
                                {key:"time", sortable:true}
                        ];
                        //end defined columns for datatable
                        myDataSource = new YAHOO.util.DataSource("cgi-bin/dashboard.py?operation=recommend&username="+szName);
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

                        myDataTable = new YAHOO.widget.RowExpansionDataTable("recommendedEvents", myColumnDefs,myDataSource,myConfigs);
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

			//menu option setup
/*			var onContextMenuClick = function(p_sType, p_aArgs, p_myDataTable) {
				var task = p_aArgs[1];
				if(task) {
					// Extract which TR element triggered the context menu
					var elRow = this.contextEventTarget;
					elRow = p_myDataTable.getTrEl(elRow);
					if(elRow) {
						switch(task.index) {
							case 0:     // Delete row upon confirmation
								var oRecord = p_myDataTable.getRecord(elRow);
								if(confirm("Are you sure you want to delete SKU " +
								oRecord.getData("SKU") + " (" +
								oRecord.getData("Description") + ")?")) {
									p_myDataTable.deleteRow(elRow);
								}
						}
					}
				}
			};
			var myContextMenu = new YAHOO.widget.ContextMenu("mycontextmenu", {trigger:myDataTable.getTbodyEl()});
			myContextMenu.addItem("Delete Event");
			myContextMenu.addItem("Rate and Comment Event");
			myContextMenu.addItem("Add to Calendar");
			// Render the ContextMenu instance to the parent container of the DataTable
			myContextMenu.render("recommendedEvents");
			myContextMenu.clickEvent.subscribe(onContextMenuClick, myDataTable);
*/
                });
}

