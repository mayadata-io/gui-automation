# Local Authentication Testcases Using Browser
<b>tcid:</b> gaau01 <br>
<b>name:</b> "Local Authentication Testcases Using Browser"<br>

### Prerequisites
    • DOP should be installed in the cluster.
    • Selenium grid should be installed and running.
    
### Test Case 1: 
#### &nbsp;&nbsp;&nbsp;Details
	 Test case to verify Administrator login should be successful
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test
* Open DOP URL in browser
* Once UI is accessible login using Administrator credentials

#### &nbsp;&nbsp;&nbsp;Expected Output
	 Login to DOP should be successful
	
### Test Case 2: 
#### &nbsp;&nbsp;&nbsp;Details
	 Test case to verify signup functionality in Local Auth.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test
* Open DOP URL in browser
* Click on signup option at bottom
* Provide First name
* Provide last name
* Provide unique email id
* Provide apha numeric password with at-least 8 and utmost 20 character

#### &nbsp;&nbsp;&nbsp;Expected Output
	 Signup to DOP should be successful
    
	
### Test Case 3: 
#### &nbsp;&nbsp;&nbsp;Details
	 Test case to verify the change password functionality for local auth account.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test
* Open DOP URL in browser
* Login using local auth credentials
* Click on name on the left panel
* Click on profile 
* Click on change password
* Provide old password and new password
* Logout of local auth account
* Login using local auth account and new password

#### &nbsp;&nbsp;&nbsp;Expected Output
	 Local Auth login should be successful using updated password

### Test Case 4: 
#### &nbsp;&nbsp;&nbsp;Details
	 Test case to verify error message is shown if wrong password is provided
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test
* Open DOP URL in browser
* Provide correct email and wrong password

#### &nbsp;&nbsp;&nbsp;Expected Output
	 Error message should be shown that either username or password is incorrect
	
### Test Case 5: 
#### &nbsp;&nbsp;&nbsp;Details
	 Test case to verify error message is shown if wrong email ID provided
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test
*  Open DOP URL in browser
*  Provide wrong email and correct password

#### &nbsp;&nbsp;&nbsp;Expected Output
	 Error message should be shown that either username or password is incorrect
	
### Test Case 6: 
#### &nbsp;&nbsp;&nbsp;Details
	 Test case to verify password for local authentication should be alpha numeric supported
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test
* Open DOP URL  in browser
* Click on signup option
* Provide First name
* Provide the Email ID
* Provide the normal password(test)

#### &nbsp;&nbsp;&nbsp;Expected Output
* Error message should be shown that password must be alpha numeric with atleast 8 chars and utmost 20 char
* Once the correct format of password is provided signup/login should be successful
	
### Test Case 7: 
#### &nbsp;&nbsp;&nbsp;Details
	 Test case to verify unique Email ID for each user.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test
* Open DOP URL in browser
* Click on signup option
* Provide First name
* Provide the Email ID of an existing user
* Provide the password

#### &nbsp;&nbsp;&nbsp;Expected Output
* Error message should be shown that this email id is already been taken
* Once unique email Id is provided signup should be successful