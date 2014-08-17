using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

/// <summary>
/// Use to provide and API for event data in database
/// </summary>
public class eventData 
{
    /// <summary>
    /// Used to hold results from database, or to hold data to be inserted database, or to hold records to be deleted into the database.
    /// </summary>
    private eventDataDB data;

    /// <summary>
    /// eventData constructor
    /// </summary>
    /// <param name="none"> 
    /// </param>
    /// <returns>
    /// Does not return anything.
    /// </returns>
	public eventData()
	{
        data = new eventDataDB();
	}

    /// <summary>
    /// used to search the database for events > systemdate.
    /// </summary>
    /// <param name="none"> 
    /// </param>
    /// <returns>
    /// eventDataDB object holding the all events > systemdate. 
    /// </returns>
    public eventDataDB getUpcomingEvents()
    {
        eventDataDBTableAdapters.DataTableTableAdapter adapt = new eventDataDBTableAdapters.DataTableTableAdapter();
        adapt.FillUpcomingEvents(data.DataTable);
        return data;
    }

    /// <summary>
    /// Function used to search events based on user's search term
    /// </summary>
    /// <param name="query"> 
    /// Holds the users search term
    /// </param>
    /// <returns>
    /// eventDataDB object holding the search results.
    /// </returns>
    public eventDataDB searchEvents(string query){
        eventDataDBTableAdapters.DataTableTableAdapter adapt = new eventDataDBTableAdapters.DataTableTableAdapter();
        query = query + "%";
        adapt.FillSearchEvents(data.DataTable,query);
        return data;
    }

    /// <summary>
    /// Function used to insert events into the database
    /// </summary>
    /// <param name="name"> 
    /// Name of the event
    /// </param>
    /// <param name="location"> 
    /// Location of the event
    /// </param>
    /// <param name="timeOfEvent"> 
    /// Time in which the event will take place
    /// </param>
    /// <returns>
    /// Boolean value of success or failure of inserting event into the database.
    /// </returns>
    public Boolean insertEvent(string name, string location, DateTime timeOfEvent, string url, string synopsis, string category, string target_audience) {
        eventDataDBTableAdapters.eventsTableAdapter adapt = new eventDataDBTableAdapters.eventsTableAdapter();
        try
        {
            DateTime saveNow = DateTime.Now;
            if (timeOfEvent < saveNow||name.Length<6||name.Length>200)
            {
                return false;
            }
            adapt.Insert(name, location, timeOfEvent, url, synopsis, category, target_audience,"hash");
            return true;
        }
        catch
        {
            return false;
        }
    }


    public eventDataDB getRecommendedEvents(string username)
    {
        eventDataDBTableAdapters.DataTableTableAdapter adapt = new eventDataDBTableAdapters.DataTableTableAdapter();
        adapt.FillRecommendedEvents(data.DataTable, username);
        return data;
    }

    public eventDataDB getEventInformation(int eventID)
    {
        eventDataDBTableAdapters.eventsTableAdapter adapt = new eventDataDBTableAdapters.eventsTableAdapter();
        adapt.FillEventInformation(data.events, eventID);
        return data;
    }
}