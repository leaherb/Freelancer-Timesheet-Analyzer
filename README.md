
Freelancer Timesheet Analyzer
==============================

This project is a work in progress, not yet 'production' level.

Problem
-------
I track my freelance work time in a spreadsheet, a row for each chunk of time I work on a customer's project. The spreadsheet contains all the time chunks for all my customers in a single sheet. 

When it comes time to invoice a customer, manually filtering through the spreadsheet becomes tedious. Especially since some time is billable and some is not. I dislike manipulating "raw data", even to simply re-order records in the spreadsheet by customer name and time category, so I have to copy the spreadsheet and work on the copy. I need a better process.

I could write functions in Excel to achieve my reporting needs, but I prefer to use Python so I can use the same functionality for multiple sheets.

Solution
--------
A Python3 program that reads timesheet data, prompts for filters (e.g. Customer name), and reports billable hours.

Freelancer-Timesheet-Analyzer creates this report, plus it interactively allows you to adjust total billable hours to make invoicing easier (e.g. if you want to give a discount or add an additional hours based on whatever logic you desire). 

### This project is in its infancy. Right now, it works like this:

  1. You record your work time in an Excel spreadsheet.
  2. Run Freelancer-Timesheet-Analyzer. 
  3. Respond to prompts for filters.
  
* Note: reporting functions are not yet working in version 2.

Timesheet Requirements
---------------------------
Your timesheet can contain any number of columns in any order, but needs to include these minimum columns with these column headings: 
  * 'Customer' (string)
  * 'Date' (date string format: %mm/%dd/%yy)
  * 'Hours' (float)
Optional:
  * 'Billable' (any value, it's simply tested for null-ness)
  * 'Details' (any string, it's simply included in the final report to help you decide if you want to make billable adjustments)
  
See /data for example.xls timesheet.

Caveats
------------------
  * 

Future Improvements
------------------
  * Fix reporting 
  * Include generic filtering prompts instead of hard-coding.
