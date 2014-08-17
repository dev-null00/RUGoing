/*
* Create a single event
*/ 

// Create the calendar service object
var calendarService = new google.gdata.calendar.CalendarService('RUGoing'); //Needs to be Application name

// The default "private/full" feed is used to insert event to the 
// primary calendar of the authenticated user
var feedUri = 'http://www.google.com/calendar/feeds/default/private/full';

// Create an instance of CalendarEventEntry representing the new event
var entry = new google.gdata.calendar.CalendarEventEntry();

// Set the title of the event
entry.setTitle(google.gdata.Text.create('Football Match'));

// Create a When object that will be attached to the event
var when = new google.gdata.When();

// Set the start and end time of the When object
var startTime = google.gdata.DateTime.fromIso8601("2010-12-10T09:00:00.000-08:00");
var endTime = google.gdata.DateTime.fromIso8601("2010-12-10T10:00:00.000-08:00");
when.setStartTime(startTime);
when.setEndTime(endTime);

// Add the When object to the event 
entry.addTime(when);

// The callback method that will be called after a successful insertion from insertEntry()
var callback = function(result) {
  PRINT('event created!');
}

// Error handler will be invoked if there is an error from insertEntry()
var handleError = function(error) {
  PRINT(error);
}

// Submit the request using the calendar service object
calendarService.insertEntry(feedUri, entry, callback, 
    handleError, google.gdata.calendar.CalendarEventEntry);