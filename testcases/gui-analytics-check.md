# DOP Metrics/Volume Analytics Check
<b>tcid:</b> <br>
<b>name:</b> "DOP Metrics/Volume Analytics Check"<br>

### Prerequisites

* DOP should be installed in the cluster.
* Selenium grid should be installed and running.

### Test Case 1: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify volumes details are shown.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on clusters
* Click on Monitor

#### &nbsp;&nbsp;&nbsp;Expected Output
     volume details are shown such as volume name,status,capacity,Application,namespace,replicas and cas type.

### Test Case 2: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify the report generation functionality.
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on clusters
* Click on Monitor
* Click on volume analytics for any volume(jiva/cstor)
* Click on report 

#### &nbsp;&nbsp;&nbsp;Expected Output
     Volume analytics report should get generated.

### Test Case 3: 
#### &nbsp;&nbsp;&nbsp;Details
     Test case to verify different component status of volume
#### &nbsp;&nbsp;&nbsp;Steps Performed in the test

* Access the DOP url.
* Login using credentials
* Click on clusters
* Click on Monitor
* Click on volume analytics for any volume(jiva/cstor)

#### &nbsp;&nbsp;&nbsp;Expected Output
     Deatiled volumes info are shown in graphical way such as IOPS,throughput, latency etc