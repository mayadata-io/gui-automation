**Running Selenium authentication test cases for DOP**

Prerequisites
    • DOP should be installed in the cluster.
    • Selenium grid should be installed and running.
    
Test Case 1: 
	Details
	 	In this test case we have to verify Administrator login should be successful.
	Steps Performed in the test
	    • Open DOP URL in browser.
	    • Once UI is accessible login using Administrator credentials.	
	Expected Output
		    Login to DOP should be successful.
	
Test Case 2: 
	Details
	 	In this test case we have to verify signup functionality in Local Auth.
	Steps Performed in the test
	    • Open DOP URL in browser.
	    • Click on signup option at bottom.
	    • Provide First name.
	    • Provide last name.
	    • Provide unique email id.
	    • Provide apha numeric password with at-least 8 and utmost 20 character
	Expected Output
		 Signup to DOP should be successful.
    
	
Test Case 3: 
	Details
	 	In this test case we have to verify the Change password functionality for local auth account.
	Steps Performed in the test
	    • Install DOP.
	    • Login using local auth credentials.
	    • Click on name on the left panel.
	    • Click on profile 
	    • Click on change password.
	    • Provide old password and new password.
	    • Logout of local auth account.
	    • Login using local auth account and new password
	Expected Output
		 Local Auth login should be successful using updated password.

Test Case 4: 
	Details
	 	In this test case we have to verify error message is shown if wrong password is provided.
	Steps Performed in the test
	    • Open DOP URL in browser.
	    • Provide correct email and wrong password.
	Expected Output
		Error message should be shown that either username or password is incorrect.
	
Test Case 5: 
	Details
	 	In this test case we have to verify error message is shown if wrong email ID provided.
	Steps Performed in the test
	    •  Open DOP URL in browser.
	    •  Provide wrong email and correct password.
	Expected Output
		Error message should be shown that either username or password is incorrect.
	
Test Case 6: 
	Details
	 	In this test case we have to verify password for local authentication should be alpha numeric supported.
	Steps Performed in the test
	    • Open DOP URL  in browser
	    • Click on signup option.
	    • Provide First name.
	    • Provide the Email ID.
	    • Provide the normal password(test)
	Expected Output
	    • Error message should be shown that password must be alpha numeric with atleast 8 chars and utmost 20 chars.
	    • Once the correct format of password is provided signup/login should be successful.
	
Test Case 7: 
	Details
	 	In this test case we have to verify unique Email ID for each user.
	Steps Performed in the test
	    • Open DOP URL 
	    • Click on signup option.
	    • Provide First name.
	    • Provide the Email ID of an existing user.
	    • Provide the password
	Expected Output
	    • Error message should be shown that this email id is already been taken.
	    • Once unique email Id is provided signup should be successful