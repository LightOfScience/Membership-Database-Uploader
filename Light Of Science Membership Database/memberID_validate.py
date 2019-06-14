from random_membershipID_generator import RandomID
from online_database import UsedMemberID

def memberID():
    CurrentMemberID = RandomID()
    UsedID =  UsedMemberID()

    n=1 # 1 is used because the first element is the column title
    while (n<len(UsedID)):
        if CurrentMemberID == UsedID[n]:
            n=1
            CurrentMemberID = RandomID()
        else:
            n+=1
    print ("Assigned Membership ID :: %s" %CurrentMemberID)
    return CurrentMemberID