**Running Selenium cluster test cases for DOP**
Prerequisites
    • DOP should be installed in the cluster.
    • Selenium grid should be installed and running.
Test Case 1: 
    Details
        In this test case we have to verify self connected cluster is shown for Admin user
    Steps Performed in the test
        • Access the DOP URL in browser.
        • Login using Admin credentials
        • Click on clusters button.
    Expected Output
         The self connected cluster status shown should be active .

Test Case 2: 
    Details
        In this test case we have to verify cluster name should not be less than 6 character and should not contain any special character.
    Steps Performed in the test
        • Access the DOP URL.
        • Login using credentials
        • In Home dashboard click on connect cluster button.
        • Select respective platform
        • Provide cluster name less than 6 characters
    Expected Output
           Error message should be shown in UI.
