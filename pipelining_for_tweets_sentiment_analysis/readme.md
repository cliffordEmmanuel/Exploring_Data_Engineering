## Premise
Can we have a script that downloads tweets stores them into a database(Sql-lite) and perform some sentiment analysis and save the predictions back to the database?

## Planning

### Task 1
- Write script that downloads tweets and stores to a database.
    - twitter credentials
    - tweets should be downloaded periodically (time period should be passed as an argument)
    - ...

### Task 2
- Perform the sentiment analysis on the stored tweets

    *method 1*
    - make an api call to a pre-trained-sentiment analyzer model
    - save predictions back to the database.

    *method 2*
    - build a sentiment model
    - deploy and expose as an API
    - save predictions back to the database.
    - train periodically with new data.


the rest would follow suit soon.