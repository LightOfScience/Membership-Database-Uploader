def uploadData(MemberID, FirstName, LastName):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('LOS Member Database-dd00eddde642.json', scope)

    gc = gspread.authorize(credentials)

    MemberDatabase = gc.open('Light Of Science Member Database').sheet1

# print (MemberDatabase.get_all_records()) # Show All Records

    MemberDatabase.append_row([MemberID, FirstName, LastName])
    return 1