The test approach is to check responses firstly for each parameter and after that for their combinations.
As soon as there is no data what exact parameters are required per one query and what exactly should be given inside response payload - this should be discovered either with help of developers or experimentally.
Also a good approach is to verify response with help of Schema Validator firstly before parsing response.  
For the provided example in this repo with parametrized tests, was taken parameter "des". 
There are 3 positive parametrized tests with different "des" but stale params.
Negative tests can also be done but with different type of fixture "xfail". 

**Tests run.**

In order to run tests in docker it should be installed on your local env before you run tests. 

Here are the commands to build and run container: 

