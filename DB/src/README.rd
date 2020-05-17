This doc contains some thoughts while I am designing stuff.
Date 27 April 2020.

Today I am trying to implement B+ tree to store table. Structuring each node of a tree to a page. 
Using first page of the file to store meta data related to Database. Currently storing root node number for the table. 
As, we are considering only one table for now, just storing the relative page number in the file for root node.
Later on plan os to store table name and some meta data like column names, root node number etc for each table.

Rest all file is used to store pages containing other data.

Now the flow:

1. First lets check if file is empty or not.
2. if its empty, lets initialise a table, with root page number 1.
3. If there is an insert statement, lets insert key, row starting at DATA_OFFSET of that page.
3. if not, lets load the root node into the table/pager.

Status as of 17 May 2020
Implemented a Two level B+ tree. Which supports splitting of the leaf node when the leaf node is full and pushes the key to the root node.
Things to be done:

1. Binary search on the non-leaf node to find which children the key should be inserted/search also.
2. Implement a search functionality
3. Multi level B+ tree
