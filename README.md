# Replication

All work is able to be replicated idempotently inside of a Docker container.

If you have Docker installed on your machine, you can run `docker compose build && docker compose up`.  This will build the container, install all necessary dependencies and then run `start.sh` to execute all of the python scripts.

Please note that you can replicate all of the work outside of a container, but you will need to make sure that:
- You are running the scripts from the root directory of this repo
- You have all necessary dependencies installed
- If you are running `python exercise/insert_data.py`, you will need to ensure that the database does not yet exist, or if it does exist it will need to be empty.

# Dealing with Inconsistent Data

To deal with the data constraints laid out in this exercise, I chose to encode all of the constraints into the schema definitions with the `sqlite` `CHECK` functionality. I found this approach to be be most readable and it required the least amount of code.  I also like this approach because it makes error handling very simple and explicit.  In addition, this approach would make testing relatively trivial compared to a scenario where all data munging/checking was done in python code.

The main assumption I had to make when dealing with the data inconsistencies was how to treat the empty strings in the csv files.  For simplicity's sake I chose to convert all empty strings to `NULL`.  I think this is the right approach for `TEXT` types, but it is unclear if this is the right approach for `NUMERIC` types -- perhaps they were meant to be zeros and it is a symptom of an upstream data issue.  This could potentially cause erroneous query results when using aggregate SQL functions on a `NUMERIC` column that uses `NULL` when zeros are expected.  In a real-world version of this scenario I would check with the stakeholder to see what they would expect to see in these columns.

One caveat that is worth mentioning is that that `sqlite` does not enforce data type constraints (e.g. you can write `TEXT` to a `NUMERIC` column), so in a real-world version of this scenario, I would recommend moving to a different type of database, or add more robust checks at the schema level using `typeof()`.

# Dependencies

Only two external dependencies were required, `pandas` and `matplotlib`, for the visualization question.
