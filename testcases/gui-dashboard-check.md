# DOP Dashboard Check
<b>tcid:</b> gadash01 <br>
<b>name:</b> "DOP Dashboard Check"<br>

### Prerequisites

* DOP should be installed in the cluster.
* Selenium grid should be installed and running.

### Test Case 1: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case To verify graphs are shown in Home dashboards
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test
* Access the DOP url.
* Login using credentials
       
##### &nbsp;&nbsp;&nbsp;Expected Output
      Graphs are shown for the openEBS volumes except volumes which are using OpenEBS hospath as sc.
      
### Test Case 2: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify active clusters and other clusters lists are shown in home dashboard
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials

#### &nbsp;&nbsp;&nbsp;Expected Output
     a. Active clusters will show the list all the active clusters
     b. Other clusters will shows the list of inactive or offline clusters
     
### Test Case 3: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify in Home dashboards project team members are shown
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials

#### &nbsp;&nbsp;&nbsp;Expected Output
     Project team members are shown with respective roles
     
### Test Case 4: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify alerts are shown and clickable for Active clusters in Home dashboard
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on cluster button
* Type the name of cluster which you want to find

#### &nbsp;&nbsp;&nbsp;Expected Output
     The respective cluster should be shown in UI
     
### Test Case 5: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify the cluster search functionality
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on cluster button
* Type the name of cluster which you want to find

#### &nbsp;&nbsp;&nbsp;Expected Output
     The respective cluster should be shown in UI   
     
### Test Case 6: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify cluster dashboard should show the status of all the cluster connected to DOP
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on cluster button

#### &nbsp;&nbsp;&nbsp;Expected Output
     Active,inactive and offline clusters should be shown
     
### Test Case 7: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify that disconnect text should be present for delete icon and the pop up message should also have disconnect text
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on cluster button
* Hover the mouse to delete icon

#### &nbsp;&nbsp;&nbsp;Expected Output
     a. Disconnect should be shown.
     b. After clicking on disconnect icon disconnect pop message should be shown
     
### Test Case 8: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify User and Roles dashboard view
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on Users and Roles

#### &nbsp;&nbsp;&nbsp;Expected Output
     a. All users can be view.
     b. Pending invite for users can be viewed
     
### Test Case 9: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify Overview dashboard
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on cluster

#### &nbsp;&nbsp;&nbsp;Expected Output
     a. Volume analytics graphs should be shown.
     b. DOP component status cann be viewed.
     c. volume and pools which need attention can be viewed 
     
### Test Case 10: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify Application dashboard
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on cluster
* Click on Applications

#### &nbsp;&nbsp;&nbsp;Expected Output
     List of applications in the cluster will be seen