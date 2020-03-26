# DOP Profile Check
<b>tcid:</b> <br>
<b>name:</b> "DOP Profile Check"<br>

### Prerequisites

* DOP should be installed in the cluster.
* Selenium grid should be installed and running.

### Test Case 1: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify profile can be updated just after signup.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access DOP URL
* Click on signup
* Once signup is done it will redirect to update your  profile page
* Provide the asked Info

#### &nbsp;&nbsp;&nbsp;Expected Output
     User should able to feed Email,company,Role and Phone number

### Test Case 2: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify the profile info is same whatever provided during onboarding time.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access DOP URL.
* Provide the local auth credentails 
* Click on LogIn
* Click on name 
* Click on profile

#### &nbsp;&nbsp;&nbsp;Expected Output
     All the given info should be present in profile section.

### Test Case 3: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify First and last Name can be modified for local Auth user.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access DOP URL.
* Provide the local auth credentails 
* Click on Login
* Click on name 
* Click on profile
* Modify the First and Last name.
* Click on update profile

#### &nbsp;&nbsp;&nbsp;Expected Output
     New First and last name should be seen after updating the profile.

### Test Case 4: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify company,Role and phone can be modified for local Auth user.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access DOP URL.
* Provide the local auth credentails 
* Click on Login
* Click on name 
* Click on profile
* Modify the company,role and phone number
* Click on update profile

#### &nbsp;&nbsp;&nbsp;Expected Output
     New details should be visible in profile section.

### Test Case 5: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify First and last Name cannot be modified for local Auth Admin user
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access DOP URL.
* Provide the local auth credentails 
* Click on Login
* Click on name 
* Click on profile
* Try to modify First or last Name

#### &nbsp;&nbsp;&nbsp;Expected Output
     Error message should be shown in UI.

### Test Case 6: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify Email id  can be modified for any user (not valid for Admin user)
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access DOP URL
* Provide the local auth credentails 
* Click on Login
* Click on name 
* Click on profile
* modify  the Email ID

#### &nbsp;&nbsp;&nbsp;Expected Output
     User should now be able to login using modified email id.
     
