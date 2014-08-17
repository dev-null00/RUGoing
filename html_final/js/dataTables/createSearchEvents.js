function createSearchEvents() {
	var Dom = YAHOO.util.Dom,
	Event = YAHOO.util.Event,
	myDataSource = null,
	myDataTable = null;
	var getTerms = function(query) {
		myDataSource.sendRequest('query=' + query, myDataTable.onDataReturnInitializeTable, myDataTable);
	};
                
	Event.onDOMReady(function() {
		var oACDS = new YAHOO.util.FunctionDataSource(getTerms);
		oACDS.queryMatchContains = true;
		var oAutoComp = new YAHOO.widget.AutoComplete("dt_input","dt_ac_container", oACDS);
		oAutoComp.minQueryLength = 1;
		//defined columns for datatable
		var myColumnDefs = [
			{key:"name", sortable:true},
			{key:"location", sortable:true},
			{key:"time", sortable:true}
		];
		//end defined columns for datatable
		myDataSource = new YAHOO.util.DataSource("cgi-bin/dashboard.py?operation=search&");
		myDataSource.responseType = YAHOO.util.DataSource.TYPE_XML;
		myDataSource.connXhrMode = "queueRequests";
		myDataSource.connMethodPost = true;
		myDataSource.responseSchema = {
			resultNode: "DataTable",
			fields: ["name","location","time","eventid"]
		};
		// DataTable configuration
		var myConfigs = {
//			initialRequest: 'query=' + Dom.get('dt_input').value 
		};
		myDataTable = new YAHOO.widget.DataTable("searchedEvents", myColumnDefs,myDataSource,myConfigs);
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

