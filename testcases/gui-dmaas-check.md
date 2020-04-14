# DOP Dmaas Schedule and Restore Check
<b>tcid:</b> <br>
<b>name:</b> "DOP Dmaas Schedule and Restore Check (Minio Platform)"<br>

### Prerequisites

* DOP should be installed in the cluster.
* Selenium grid should be installed and running.

### Test Case 1: 
#### &nbsp;&nbsp;&nbsp;Details
     Create dmaas schedule and check the status for deployment app(cstor)
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url
* Login using credentials
* Click on clusters
* Click on Applications
* Check cas type. It should be cstor
* Click on Dmaas
* Click on New schedule
* Provide required info

#### &nbsp;&nbsp;&nbsp;Expected Output
     Schedule should get created successfully.

### Test Case 2: 
#### &nbsp;&nbsp;&nbsp;Details
     Create a dmaas schedule and check the status for statefulset app(cstor)
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url
* Login using credentials
* Click on clusters
* Click on Applications
* Check cas type. It should be cstor
* Click on Dmaas
* Click on New schedule
* Provide required info

#### &nbsp;&nbsp;&nbsp;Expected Output
     Schedule should get created successfully.


### Test Case 3: 
#### &nbsp;&nbsp;&nbsp;Details
     Check the status backups.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on clusters
* Click on Applications
* Check cas type. It should be cstor
* Click on Dmaas
* Click on New schedule
* Provide required info

#### &nbsp;&nbsp;&nbsp;Expected Output
* schedule should become active.
* Clicking on schedule should backup status as completed.

### Test Case 4: 
#### &nbsp;&nbsp;&nbsp;Details
     Check if the backups are taken incrementally
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on clusters
* Click on Applications
* Check cas type. It should be cstor
* Click on Dmaas
* Click on New schedule
* Provide required info

#### &nbsp;&nbsp;&nbsp;Expected Output
	Backups should be completed for specificed time period and data should be present.

### Test Case 5: 
#### &nbsp;&nbsp;&nbsp;Details
     Start a restore of chosen backup.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on dmaas.
* Click on the schedule.
*  Click on restore button of a successful backup
* Select the destination cluster

#### &nbsp;&nbsp;&nbsp;Expected Output
	Application should get restored to the destination cluster.

### Test Case 6: 
#### &nbsp;&nbsp;&nbsp;Details
     Try to delete schedule.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on dmaas.
* Click on delete icon of schedule

#### &nbsp;&nbsp;&nbsp;Expected Output
	The respective schedule should get deleted.