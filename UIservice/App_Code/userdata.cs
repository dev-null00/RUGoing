using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

/// <summary>
/// Use to provide and API for user's data in database
/// </summary>
public class userdata
{
    /// <summary>
    /// Used to hold results from database, or to hold data to be inserted database, or to hold records to be deleted into the database.
    /// </summary>
    private userdataDB data;

    /// <summary>
    /// userdata constructor
    /// </summary>
    /// <param name="none"> 
    /// </param>
    /// <returns>
    /// Void
    /// </returns>
	public userdata()
	{
	    data = new userdataDB();
	}

    /// <summary>
    /// Function used check the user provided credentials in the database
    /// </summary>
    /// <param name="username"> 
    /// User provided username
    /// </param>
    /// <param name="password"> 
    /// User provided password
    /// </param>
    /// <returns>
    /// Boolean value for the provided credentials.
    /// </returns>
    public Boolean checklogin(string username, string password)
    {
        userdataDBTableAdapters.DataTableTableAdapter adapt = new userdataDBTableAdapters.DataTableTableAdapter();
        adapt.FillLogin(data.DataTable, password, username);
        if (data.DataTable.Count() == 1)
            return true;
        return false;
    }

    /// <summary>
    /// Function used check the retrive all of the speficied user's information
    /// </summary>
    /// <param name="username"> 
    /// Username to be searched in database
    /// </param>
    /// <returns>
    /// All information for specified user.
    /// </returns>
    public userdataDB getUserData(string username) 
    {
        //TODO: get user's data
        userdataDBTableAdapters.DataTableTableAdapter adapt = new userdataDBTableAdapters.DataTableTableAdapter();
        adapt.Fill(data.DataTable);
        return data;
    }

    /// <summary>
    /// Function used register user into the database.
    /// </summary>
    /// <param name="username"> 
    /// User provided username
    /// </param>
    /// <param name="password"> 
    /// User provided password
    /// </param>
    /// <param name="firstName"> 
    /// User provided first name
    /// </param>
    /// <param name="lastName"> 
    /// User provided last name
    /// </param>
    /// <param name="interests"> 
    /// User provide list of topics
    /// </param>
    /// <returns>
    /// Boolean value to determine if registration was sucessful.
    /// </returns>
    public Boolean registerUser(string username, string firstName, string lastName, string password, string[] interests)
    {
        try
        {
            if (username.Length < 6)
            {
                return false;
            }
            userdataDBTableAdapters.DataTableTableAdapter adapt = new userdataDBTableAdapters.DataTableTableAdapter();
            userdataDBTableAdapters.DataTable2TableAdapter adapt2 = new userdataDBTableAdapters.DataTable2TableAdapter();
            adapt.RegisterUser(username, password, firstName, lastName);
            foreach (string s in interests)
            {
                adapt2.insertUserInterest(username, s);
            }

            return true;
        }
        catch
        {
            return false;
        }
    }

    /// <summary>
    /// Function used modify registered user into the database.
    /// </summary>
    /// <param name="username"> 
    /// Used to identified which user to updated. 
    /// </param>
    /// <param name="password"> 
    /// User provided updated password
    /// </param>
    /// <param name="firstName"> 
    /// User provided updated first name
    /// </param>
    /// <param name="lastName"> 
    /// User provided updated last name
    /// </param>
    /// <param name="interests"> 
    /// User provide updated list of topics
    /// </param>
    /// <returns>
    /// Boolean value to determine if modification was sucessful.
    /// </returns>
    public Boolean modifyUser(string username, string firstName, string lastName, string oldpassword, string password, string[] interests)
    {
        try
        {
            userdataDBTableAdapters.DataTableTableAdapter adapt = new userdataDBTableAdapters.DataTableTableAdapter();
            userdataDBTableAdapters.DataTable2TableAdapter adapt2 = new userdataDBTableAdapters.DataTable2TableAdapter();
            adapt.FillLogin(data.DataTable, oldpassword, username);
            if (data.DataTable.Count() == 1)
            {
                //run update for first name, last name, password
                adapt2.modifyUser(username, firstName, lastName, password);
                //delte all interests
                adapt2.deleteUserInterest(username);
                //insert interests
                foreach (string s in interests)
                {
                    adapt2.insertUserInterest(username, s);
                }
                return true;
            }

            return false;
        }
        catch
        {
            return false;
        }
    }

    /// <summary>
    /// Function used to rate event
    /// </summary>
    /// <param name="username"> 
    /// User that is rating the event
    /// </param>
    /// <param name="rating"> 
    /// Rating of the event
    /// </param>
    /// <param name="eventID">
    /// ID of the event being rated
    /// </param>
    /// <returns>
    /// Boolean value of sucess or failure.
    /// </returns>
    public Boolean rateEvent(string username, int rating, int eventID)
    {
        try
        {

            userdataDBTableAdapters.DataTable2TableAdapter adapt = new userdataDBTableAdapters.DataTable2TableAdapter();
            eventDataDBTableAdapters.DataTableTableAdapter adapt2 = new eventDataDBTableAdapters.DataTableTableAdapter();
            eventDataDB checkValidEventID = new eventDataDB();
            adapt2.FillCheckEventID(checkValidEventID.DataTable, eventID);     

            if(checkValidEventID.DataTable.Count() != 1 ) {
                return false;
            }
            if (rating < 0 || rating > 5)
            {
                return false;
            }
            adapt.rateEvent(username, rating, eventID);
            return true;
        }
        catch
        {
            return false;
        }
    }
}