using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

[WebService(Namespace = "http://tempuri.org/")]
[WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]


public class Service : System.Web.Services.WebService
{
    /// <summary>
    /// Webservice providing database access to all RUGoing modules (dataminer, UI, and recommendation engine)
    /// </summary>
    public Service () {
    }

    /// <summary>
    /// Web service function to check login credentials
    /// </summary>
    /// <param name="username"> 
    /// Username to check
    /// </param>
    /// <param name="password"> 
    /// Password to check againist provide username
    /// </param>
    /// <returns>
    /// XML document with a boolean value inside result tag
    /// </returns>
    [WebMethod]
    public Boolean login(string username, string password) {
        userdata check = new userdata();
        return check.checklogin(username, password);
    }

    /// <summary>
    /// Web service function to get all of a user's information
    /// </summary>
    /// <param name="username"> 
    /// The user we will be fetching data of
    /// </param>
    /// <returns>
    /// XML document the following data: interest, friends, and event ratings
    /// </returns>
    [WebMethod]
    public userdataDB getAllUserData(string username)
    {
        userdata allusers = new userdata();
        return allusers.getUserData(username);
    }

    /// <summary>
    /// Web service function to get rate events
    /// </summary>
    /// <param name="username"> 
    /// The user we will be rating
    /// </param>
    /// <param name="eventID"> 
    /// Event to be rated
    /// </param>
    /// <param name="rating"> 
    /// Rating of the event
    /// </param>
    /// <returns>
    /// XML document the following data: interest, friends, and event ratings
    /// </returns>
    [WebMethod]
    public Boolean rateEvent(string username, int eventID, int rating)
    {
        try
        {
            userdata eventToRate = new userdata();
            return eventToRate.rateEvent(username, rating, eventID);
        }
        catch
        {
            return false;
        }
    }

    /// <summary>
    /// Web service function to get all events > systemdate
    /// </summary>
    /// <param name="none"> 
    /// </param>
    /// <returns>
    /// XML document with list of events with their: name, eventID, location, and time
    /// </returns>
    [WebMethod]
    public eventDataDB getAllUpcomingEvents()
    {
        eventData allUpcomingEvents = new eventData();
        return allUpcomingEvents.getUpcomingEvents();
    }



    /// <summary>
    /// Web service function to get all events related to search terms
    /// </summary>
    /// <param name="query"> 
    /// List of search terms to find related events in the database
    /// </param>
    /// <returns>
    /// XML document with list of events with their: name, eventID, location, and time
    /// </returns>
    [WebMethod]
    public eventDataDB searchEvents(string query)
    {
        eventData queriedEvents = new eventData();
        return queriedEvents.searchEvents(query);
    }

    /// <summary>
    /// Web service function used modify user's data.
    /// </summary>
    /// <param name="username"> 
    /// User to be updated 
    /// </param>
    /// <param name="password"> 
    /// Updated password
    /// </param>
    /// <param name="firstName"> 
    /// Upated first name
    /// </param>
    /// <param name="lastName"> 
    /// Updated last name
    /// </param>
    /// <param name="interests"> 
    /// Updated list of topics
    /// </param>
    /// <returns>
    /// XML document with a boolean value inside result tag
    /// </returns>
    [WebMethod]
    public Boolean modifyUser(string username, string firstName, string lastName, string oldpassword, string password, string[] interests)
    {
        userdata user = new userdata();
        return user.modifyUser(username, firstName, lastName, oldpassword, password, interests);
    }

    /// <summary>
    /// Web service function used register a user.
    /// </summary>
    /// <param name="username"> 
    /// Username chosen 
    /// </param>
    /// <param name="password"> 
    /// Password chosen
    /// </param>
    /// <param name="firstName"> 
    /// First name chosen
    /// </param>
    /// <param name="lastName"> 
    /// Last name chosen
    /// </param>
    /// <param name="interests"> 
    /// Interest chosen
    /// </param>
    /// <returns>
    /// XML document with a boolean value inside result tag
    /// </returns>
    [WebMethod]
    public Boolean registerUser2(string username, string password, string firstName, string lastName, string[] interests)
    {
        userdata user = new userdata();
        return user.registerUser(username, firstName, lastName, password,interests);
    }


    //TODO: add the xml for getRecommendedEvents
    [WebMethod]
    public eventDataDB getRecommendedEvents(string username)
    {
        eventData recommendedevents = new eventData();
        if(username.Length > 20)
        {
            return recommendedevents.getRecommendedEvents("");
        }
        return recommendedevents.getRecommendedEvents(username);
    }
/*
    //TODO add  friend
    [WebMethod]
    public Boolean addFriend(string username, string usernameOfFriend)
    {
        return false;
    }

    //TODO remove friend
    [WebMethod]
    public Boolean removeFriend(string username, string usernameOfFriend)
    {
        return false;
    }

    //TODO get friends
    [WebMethod]
    public Boolean getFriends(string username)
    {
        return false;
    }

    //TODO get calendar
    [WebMethod]
    public Boolean getCalendar(string username)
    {
        return false;
    }

    //TODO remove from calendar
    [WebMethod]
    public Boolean removeFromCalendar(string username, int eventID)
    {
        return false;
    }

    //TODO add to calendar friend
    [WebMethod]
    public Boolean addToCalendar(string username, int eventID)
    {
        return false;
    }
*/
    /// <summary>
    /// Web service function to insert events into the database
    /// </summary>
    /// <param name="name"> 
    /// Name of the event
    /// </param>
    /// <param name="location"> 
    /// Location where the event will take place
    /// </param>
    /// <param name="url"> 
    /// Link to event
    /// </param>
    /// </param>
    /// <param name="synopsis"> 
    /// Summary of event
    /// </param>
    /// <param name="category"> 
    /// Type of event
    /// </param>
    /// <param name="target_audience"> 
    /// main group of people which will attend
    /// </param>
    /// <param name="timeOfEvent"> 
    /// Time when the event will take place
    /// </param>
    /// <returns>
    /// XML document with a boolean value inside result tag
    /// </returns>
    [WebMethod]
    public bool insertEvent(string name, string location, string url, string synopsis, string category, string target_audience, string eventtime)
    {
        try
        {
            //will need work with timestamps
            //Wednesday, November 3, 2010  10:33 AM
            DateTime eventtimecov;
            eventtimecov = new DateTime();
            //eventtimecov = DateTime.ParseExact(eventtime, "dddd, MMMM d, yyyy hh:mm tt", null);
            //eventtime = "Wednesday, November 3, 2010 21:34 PM";
            eventtimecov = DateTime.ParseExact(eventtime, "dddd, MMMM d, yyyy  h:mm tt", null);
            eventData eventToInsert = new eventData();
            return eventToInsert.insertEvent(name, location, eventtimecov, url, synopsis, category, target_audience);
        }
        catch
        {
            return false;
        }
    }

    [WebMethod]
    public eventDataDB getEventData(int eventID)
    {

            eventData eventInformation= new eventData();
            return eventInformation.getEventInformation(eventID);

        
    }
}