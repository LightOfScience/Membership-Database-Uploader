def uploadData (MemberID, BSSID, FirstName, LastName, Sex, DOB, Address, District, PostalCode, ContactNumber1, ContactNumber2, Email, Profession, Designation, InstituteOffice, DateOfSubmission, Reciever):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('API_Credentials.json', scope)

    gc = gspread.authorize(credentials)

    MemberDatabase = gc.open('Light Of Science Member Database').sheet1

    # print (MemberDatabase.get_all_records()) # Show All Records
    print ("\n\nUploading Data to Google Sheets")
    MemberDatabase.append_row([MemberID, BSSID, FirstName, LastName, Sex, DOB, Address, District, PostalCode, ContactNumber1, ContactNumber2, Email, Profession, Designation, InstituteOffice, DateOfSubmission, Reciever])
    
    print ("Data Uploaded Successfully. Updated data can be viewed at 'https://docs.google.com/spreadsheets/d/1--pOfXF-glocbmoBgR6f6LcFFPtKlaN3qZWeFC05j6I/edit?usp=sharing'")
    return 1

def UsedMemberID():
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('API_Credentials.json', scope)

    gc = gspread.authorize(credentials)

    MemberDatabase = gc.open('Light Of Science Member Database').sheet1

    #Getting All Used Memeber ID
    UsedMemebrID = MemberDatabase.col_values(1)
    return MemberDatabase.col_values(1)