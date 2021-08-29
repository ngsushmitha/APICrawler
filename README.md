# APICrawler


a) Steps to run code using docker

 -> Open Command Prompt
 
 -> Clone this repository and move to the respective directory using git clone and cd command
 
 -> Run the command "docker-compose up"
 
APIs will be stored in database and retrieved from the database.

b) Details of all the tables and their schema

 -> Database used: PostgreSQL. One table named test_table is used. 
 
 Schema:
| Column      | Description |
| ---         | ---         |
| API         | TEXT        |
| Description | TEXT        |
| Auth        | TEXT        |
| HTTPS       | BOOLEAN     |
| Cors        | TEXT        |
| Link        | TEXT        |
| Category    | TEXT        |

Table creation command:
CREATE TABLE test_table ( "API" TEXT, "Description" TEXT, "Auth" TEXT, "HTTPS" BOOLEAN, "Cors" TEXT, "Link" TEXT, "Category" TEXT)

c) What is done from “Points to achieve” and number of entries in your table

 -> Your code should follow concept of OOPS
 
 -> Support for handling authentication requirements & token expiration of server
 
 -> Support for pagination to get all data
 
 -> Develop work around for rate limited server
 
 -> Crawled all API entries for all categories and stored it in a database
 
 Number of entried retrieved : 640

d) What is not done from “Points to achieve”. If not achieved, write the possible reasons and current workarounds.

 -> All points are achieved.
 
e) What would you improve if given more days

 -> I would improve the efficiency of the code and explore with different databases.
