# DOP Teaming Check
<b>tcid:</b> TCID-DIR-TEAMING-SEL-ALL <br>
<b>name:</b> "DOP Teaming Check"<br>

### Prerequisites

* DOP should be installed in the cluster.
* Selenium grid should be installed and running.

### Test Case 1: 
#### &nbsp;&nbsp;&nbsp;Details
     ProjectOwner can invite others in his/her Project.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on users and Roles.
* Click on invite  user
* Provide the email ID of already signup user
* Select one of the available role(projectAdmin,projectMember and ProjectReadAdmin)

#### &nbsp;&nbsp;&nbsp;Expected Output
     Invitation should be send to the invite.

### Test Case 2: 
#### &nbsp;&nbsp;&nbsp;Details
     To view pending invites
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using  inviter credentials
* Click on users and Roles.
* Click on pending invites

#### &nbsp;&nbsp;&nbsp;Expected Output
     Users who have not accepted the invite can be viewed

### Test Case 3: 
#### &nbsp;&nbsp;&nbsp;Details
     Only invitee can accept or reject invitation. 
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using invite credentials
* Click on name on the left panel
* Click on invites.

#### &nbsp;&nbsp;&nbsp;Expected Output
     Accept or Decline request can be seen in invitation page

### Test Case 4: 
#### &nbsp;&nbsp;&nbsp;Details
     Validate invitation reject process. 
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using invite credentials
* Click on name on the left panel
* Click on invites.
* Click on Decline

#### &nbsp;&nbsp;&nbsp;Expected Output
     The status to the inviter will be shown as rejected

### Test Case 5: 
#### &nbsp;&nbsp;&nbsp;Details
     Validate invitation accept process.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using invite credentials
* Click on name on the left panel
* Click on invites.
* Click on Accept

#### &nbsp;&nbsp;&nbsp;Expected Output
     a. From manage project dashboard he/she can see the project the user is part of.(invited user dashboard)
	 b. Inviter can view that user in All user tab

### Test Case 6: 
#### &nbsp;&nbsp;&nbsp;Details
     Project owner can only change the member role
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using  inviter credentials(project owner)
* Click on users and Roles.
* Click on All users.
* Click on eye icon on the right hand side.
* Change the role of the invited user

#### &nbsp;&nbsp;&nbsp;Expected Output
	 Role of invited user can be changed successfully.

### Test Case 7: 
#### &nbsp;&nbsp;&nbsp;Details
     To verify Project Owner access.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Open DOP URL in browser.
* Click on signup option at bottom.
* Provide First name.
* Provide last name.
* Provide unique email id.
* Provide apha numebric password with atleast 
* and utmost 20 character

#### &nbsp;&nbsp;&nbsp;Expected Output
	 a. Can invite others to his project.
	 b. Can change the role of the member in his project.
	 c. Can delete a member from a project.

### Test Case 8: 
#### &nbsp;&nbsp;&nbsp;Details
     To verify Project Admin access
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using  inviter credentials
* Click on users and Roles.
* Click on invite  user
* Provide the email ID of already signup user
* select Role as Project Admin

#### &nbsp;&nbsp;&nbsp;Expected Output
	 a. Can connect or disconnect clusters.
	 b. Can manage alerts.(Acknowledge alerts check)
	 c. in manage project(project dashboard), edit icon should be visible

### Test Case 9: 
#### &nbsp;&nbsp;&nbsp;Details
     To verify Project Read Admin access
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using  inviter credentials
* Click on users and Roles.
* Click on invite  user
* Provide the email ID of already signup user
* select Role as Project Read Admin

#### &nbsp;&nbsp;&nbsp;Expected Output
	 a. In manage project(project page), Edit icon should be invisible
	 b. Connect cluster button on cluster page should be invisible

### Test Case 10: 
#### &nbsp;&nbsp;&nbsp;Details
     To verify Project  Member access
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using  inviter credentials
* Click on users and Roles.
* Click on invite  user
* Provide the email ID of already signup user
* select Role as Project Member

#### &nbsp;&nbsp;&nbsp;Expected Output
	 a. In manage project(project page), project should not be clickable.
	 b. In manage project(project page)Edit button in project invisible.

### Test Case 11: 
#### &nbsp;&nbsp;&nbsp;Details
     Non Project owner can not change the member role
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using  inviter credentials(non project owner)
* Click on users and Roles.
* Click on All users.
* Click on eye icon on the right hand side.
* Change the role of the invited user

#### &nbsp;&nbsp;&nbsp;Expected Output
	 Role of invited user can not be changed (Check for error message when other then project owner try to changes role)
