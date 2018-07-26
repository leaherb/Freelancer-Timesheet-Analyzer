
Freelancer Timesheet Analyzer
==============================

Problem
-------
I track my freelance work time in a spreadsheet, a row for each chunk of time I work on a customer's project. The spreadsheet contains all the time chunks for all my customers in a single sheet. 

When it comes time to invoice a customer, manually filtering through the spreadsheet becomes tedious. Especially since some time is billable and some is not. I dislike manipulating "raw data", even to simply re-order records in the spreadsheet by customer name and time category, so I have to copy the spreadsheet and work on the copy. I need a better process.

Solution
--------
A Python3 program that reads timesheet data, prompts for filters (e.g. Customer name), and reports billable hours.

Freelancer-Timesheet-Analyzer creates this report, plus it interactively allows you to adjust total billable hours to make invoicing easier (e.g. if you want to give a discount or add an additional hours based on whatever logic you desire). 

### This project is in its infancy. Right now, it works like this:

  1. You record your work time in a spreadsheet (see **CSV Timesheet Requirements** below).
  2. Convert the spreadsheet to a CSV file.
  3. Run Freelancer-Timesheet-Analyzer. It will prompt for values.
  
  Runtime Notes:
  * Only the Customer name is required when prompted, other inputs have defaults.
  * Some calculations are made with hard-coded values, like your hourly rate! **You'll want to update the code!**


CSV Timesheet Requirements
---------------------------
Your timesheet can contain any number of columns in any order, but needs to include these minimum columns with these column headings: 
  * 'Customer' (string)
  * 'Date' (date string format: %mm/%dd/%yy)
  * 'Hours' (float)
  * 'Billable' (any value, it's simply tested for null-ness)
  * 'Details' (any string, it's simply included in the final report to help you decide if you want to make billable adjustments)
  
### Example CSV File
```
Date,Customer,Category,Billable,Included,Non-Billable,Details,Start,Stop,Time,Hours
1/5/18,Customer 1,Proj Mgmt,,,X,Prepare for meeting,,,0:30,0.5
1/8/18,Customer 1,Document,X,,,Infrastructure doc and deliver,,,2:00,2.0
1/9/18,Customer 2,Develop,X,,,portfolio,1:15,3:30,2:15,2.3
1/9/18,Customer 2,Develop,X,,,portfolio,6:20,6:50,0:30,0.5
1/10/18,Customer 1,Develop,X,,,Reset Staging to latest Prod updates,11:30,12:00,0:30,0.5
1/11/18,Customer 1,Develop,X,,,"Look into ""for sale""",5:15,5:45,0:30,0.5
1/11/18,Customer 1,Develop,X,,,Introductory Offer!,6:00,6:30,0:30,0.5
1/11/18,Customer 3,Proj Mgmt,,,X,Email re: hosting,7:55,8:35,0:40,0.7
1/11/18,Customer 3,Develop,X,,,Toggle display qty on Shop page,8:00,8:30,0:30,0.5
1/11/18,Customer 3,Proj Mgmt,,,X,Marketing strategy meeting,,,2:00,2.0
1/12/18,Customer 1,Proj Mgmt,,,X,Brand planning,11:45,12:00,0:15,0.3
1/15/18,Customer 4,Develop,X,,,Stylize,2:45,4:20,1:35,1.6
```

Future Improvements
-----------------
  * Read data directly from the Excel (or other) spreadsheet, as opposed to manually converting it to CSV first.
  * Use pandas.dataframe.
  * Include generic filtering prompts instead of hard-coding.
