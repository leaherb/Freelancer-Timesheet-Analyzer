
# coding: utf-8

# # Freelancer Timesheet Analyzer
# Status: Version 2 not yet complete: reporting functions need to be re-written after moving from nested-lists to pandas dataframe.
# 
# ## Version 2
# 1. Only Excel spreadsheets (.xlsx) formats are accepted.
# 2. Data is loaded into dataframes.
# 3. These columns are required:
#  * Project (string) (such as Customer name or school class name)
#  * Date (date)
#  * Hours (float) 
# 4. These columns are optional:
#  * Billable (Null, or any value)
# 5. All other columns loaded (available for customizations) but ignored.
# 6. Filters include:
#  * Project 
#  * Date range
#  * Billable (if exists)
# 7. Output includes:
#  * Print of total hours (decimal format)
#  
# ## Version 1
# 1. Only CSV (.csv) are accepted.
# 2. Data is loaded into nested lists.
# 


import pandas as pd
from tkinter import filedialog
from pprint import pprint
import datetime


# #### Load Data

# Prompt for datafile 
#datafile = filedialog.askopenfilename(\
#    title='Select Timesheet CSV', \
#    filetypes=[("CSV","*.csv"),("All files","*.*")])
 
# hardcoded for testing TODO: go back to prompting for file
datafile = ('data/example.xlsx')

# load data
df = pd.read_excel(datafile) 

# TODO: add requirements validation

# #### Clean Data

# Convert Billable: any value == 1; Null == 0
df['Billable'] = (df['Billable'].notnull()).astype('int')

df.info()


df.head()


def prompt_filters():
    # Print report, prompting for filters. TODO: improve
    #  * variable number of filters w/defaults, calls such as:
    #     x, y, z = prompt_filters(Project=None, StartDate='01/01/1000', EndDate='12/31/2999')
    #    -or-
    #     x, y = prompt_filters(Project=None, Customer=None)

    project = input('Project: ') or None
    start_date = input('Start Date: ') or '01/01/1000'
    end_date = input('Start Date: ') or '12/31/9999'
    rate = input('Hourly Rate: ') or 60

    return (project, start_date, end_date, float(rate))
        

# TODO: Allow variable list of parameters
def filter_df(this_df, project=None, start_date=None, end_date=None, rate=None):
    '''
    Return dataframe of filtered date, with Billable NonBillable Hours separated.
    
    Input:  string (project name)
            string (date range start)
            string (date range end)
    Output: None
    Return: dataframe
    '''
    ## Build query
    # if no project specified, then set Project != None to return all 
    # TODO consider logic when there is no project name intentionally
    if not project:
        proj_equal = '!=' 
    else:
        proj_equal = '=='
        
    column =    ['Project',  'Date',     'Date']
    equal =     [proj_equal, '>=',       '<']
    condition = [project,    start_date, end_date]
    
    query = ' & '.join(f'{i} {j} {repr(k)}' for i, j, k in zip(column, equal, condition))
    print(query)
       
    return this_df.query(query)



project, start_date, end_date, rate = prompt_filters()
    
print('\nProject: {}\nStart Date: {}\nEnd Date: {}\nRate: {}'      .format(project, start_date, end_date, rate))


billing_df = filter_df(df, None, "2018-01-04", "2018-01-10" )

billing_df


billing_df.info()


billing_df[billing_df['Billable'] == 1]



print('Total Hours: {:4f}'.format(billing_df['Hours'].sum()))
print('Non-Billable Hours: {:.4f}'.format(         billing_df[billing_df['Billable'] == 0]['Hours'].sum()))
print('Billable Hours: {:.4f}'.format(         billing_df[billing_df['Billable'] == 1]['Hours'].sum()))
print('Hourly Rate: ${:.2f}'.format(rate))
print('Billable Amount: ${:.2f}'.format(         billing_df[billing_df['Billable'] == 1]['Hours'].sum() * rate))

