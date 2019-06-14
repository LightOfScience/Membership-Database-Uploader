import time
from online_database import uploadData
from member_details import member_details
from memberID_validate import memberID

print("\t\t----------------------------------------------------")
print("\n\t\tLight Of Science New Membership Application Database\n\n")
print("\t\t----------------------------------------------------\n\n")

MemberID = memberID()
print("\n\n")


MemberDetails =     member_details()

BSSID =             MemberDetails[0]
FirstName =         MemberDetails[1]
LastName =          MemberDetails[2]
Sex =               MemberDetails[3]
DOB =               MemberDetails[4]
Address =           MemberDetails[5]
District =          MemberDetails[6]
PostalCode =        MemberDetails[7]
ContactNumber =     MemberDetails[8]
Email =             MemberDetails[9]
Profession =        MemberDetails[10]
Designation =       MemberDetails[11]
InstituteOffice =   MemberDetails[12]
DateOfSubmission =  MemberDetails[13]
Reciever =          MemberDetails[14]

uploadData(MemberID, BSSID, FirstName, LastName, Sex, DOB, Address, District, PostalCode, ContactNumber[0], ContactNumber[1], Email, Profession, Designation, InstituteOffice, DateOfSubmission, Reciever)

#Sleep to exit
print("\n")
sleepTime=3
while (sleepTime>0):
    print("This program will be closed automatically in %d sec" %sleepTime)
    sleepTime-=1
    time.sleep(1)