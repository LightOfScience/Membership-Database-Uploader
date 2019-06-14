def member_details():
    BSSID=input("BSS Membership ID :: ")

    print ("\n")
    FirstName = input("First Name :: ")
    LastName =  input("Last Name  :: ")

    print ("\n")
    Sex = input("Sex :: ")
    DOB = input("Data of Birth (DD/MM/YYYY) :: ") 

    print ("\n")
    Address =   input("Address     :: ")
    District =  input("District    :: ")
    PostalCode =input("Postal Code :: ")

    print ("\n")
    ContactNumber=[input("Primary Contact Number :: "), input("Optional Contact Number :: ")]
    Email = input("Email :: ")

    print ("\n")
    Profession = input("Profession :: ")
    Designation = input ("Designation :: ")
    InstituteOffice = input("Institute/Office name :: ")

    print ("\n")
    DateOfSubmission = input("Date of Submission (DD/MM/YYYY) :: ")
    Reciever = input("Recieved by, ")

    MemberDetails = (BSSID, FirstName, LastName, Sex, DOB, Address, District, PostalCode, ContactNumber, Email, Profession, Designation, InstituteOffice, DateOfSubmission, Reciever)
    return MemberDetails