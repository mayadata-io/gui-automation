# DOP Self Connected Cluster Check
<b>tcid:</b> gacc01 <br>
<b>name:</b> "DOP Self Connected Cluster Check"<br>

### Prerequisites

* DOP should be installed in the cluster.
* Selenium grid should be installed and running.

### Test Case 1: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify self connected cluster is shown for Admin user
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test
* Access the DOP URL in browser
* Login using Admin credentials
* Click on clusters button
       
##### &nbsp;&nbsp;&nbsp;Expected Output
      The self connected cluster status shown should be active

### Test Case 2: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify cluster name should not be less than 6 character and should not contain any special character
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP URL
* Login using credentials
* In Home dashboard click on connect cluster button
* Select respective platform
* Provide cluster name less than 6 characters

#### &nbsp;&nbsp;&nbsp;Expected Output
     Error message should be shown in UI
