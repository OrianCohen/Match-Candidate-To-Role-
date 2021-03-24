**OVERVIEW**
basic “matcher” service. 

The services include these basic 3 main models
*Skill  
*Candidate  
*Job  


service’s core function is “ CandidateFinder ” which given a job, returns the best
candidates for this job.


**DETAILS**
1. A skill is an entity that has a name.

2. A candidate is an entity that has:
    Id
    Name
    Phone
    City 
    Title
    Skills 
    
    
3. A job is an entity that has 
    Id
    Company Name
    Title
    Skills
    
**DATABASE**
Using in-memory data base (h2)
-In memory databases are not persistent.
-All data stored in memory