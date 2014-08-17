var EVENT_IMPORTED = "EVENT_IMPORTED";
var entry = SpreadsheetApp.getActiveSpreadsheet(); //This is the place from where data will be imported so need to change this part

function onOpen() {
   var Entries = [{name: "Import Events to Calendar", functionName: "importEventtoCalendar"}];
   entry.addMenu("Scripts", Entries); // the 2second and this line deals with addind events from database, solomon you need to see these 2 lines //and make changes
}

var handleError = function(error) {
  PRINT(error);
}
function importEventtoCalendar() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var startRow = 2;  // First row of data to process
  var numRows = 100;   // Number of rows to process
  var dataRange = sheet.getRange(startRow, 1, numRows, 6)
  // Fetch values for each row in the Range.
  var data = dataRange.getValues();
  for (var i = 0; i < data.length; ++i) {
    var row = data[i];
    var title = row[0];  // First column //title
    var startDate = row[1];       // Second column  //Stime
    var endDate = row[2];     // Third column       //Etime
    var description = row[3];    // Fourth column   //Description
    var location = row[4]; // Fifth column          //Location
    var eventImported = row[5];// Sixth column      
    if (eventImported  != EVENT_IMPORTED && title != "") {  // Prevents importing duplicates
  var cal = CalendarApp.getDefaultCalendar();
      cal.createEvent(title, new Date(startDate), new Date(endDate), {description: description, location: location});
      sheet.getRange(startRow + i, 6).setValue(EVENT_IMPORTED);
        Browser.msgBox("Events imported");
      // Make sure the cell is updated right away in case the script is interrupted
      SpreadsheetApp.flush();  
    }
  }
}