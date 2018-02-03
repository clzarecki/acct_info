# acct_info

1. It currently throws an exception in the JSON parsing.
2. My solution is optimized for query latency. All the decision making is done
at event insertion.
3. I would create a score system that analyzes the similarity of the new event
to any other record. Names and birthdates would have the highest weight and
emails would have low weight. The system would update the customer with the
highest score to the new event.
4. If all the customer information doesn't exist in memory, the best solution I
can think of is to put the information in a database, updating and querying the
database at runtime.
