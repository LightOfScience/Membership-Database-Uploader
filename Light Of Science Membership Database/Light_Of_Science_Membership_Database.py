import time
from random_membershipID_generator import RandomID
from upload_database import uploadData
from member_details import member_details

MemberID = RandomID()

member = member_details()

uploadData(MemberID, member[0], member[1])