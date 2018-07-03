
# coding: utf-8

# In[ ]:


from tkinter import filedialog
import csv
from pprint import pprint
import datetime


# In[ ]:


def csv_to_list(csv_filename):    
    '''
    Create nested list with contents of a CSV file.
    
    Input: string (csv filename)
    Return: list (of lists)
    '''

    result_list = []

    with open(csv_filename, encoding="ISO-8859-1") as f: # encoding to avoid UnicodeDecodeError: 'utf-8'...
        csv_f = csv.reader(f)
        for row in csv_f:
            result_list.append(row)

    return result_list


def lists_to_dicts(my_list):
    '''
    Convert nested list to list of dictionaries. Assumption: first list contains column headings.
    
    Input: list (of lists)
    Return: list (of dictionaries)
    '''
    
    columns = list(map(lambda x : x.strip(), my_list.pop(0)))
    return list(map(lambda x_list : dict(zip(columns, x_list)), my_list))


def print_report(customer, start_dt, end_dt, rate):  
    '''    
    Print billable hours report.
    
    Input:  string (customer name)
            string (date range start)
            string (date range end)
            
    Output: report
    Return: None
    '''
    
    billable_list = []
    not_billable_list = []
    total_hours = 0
    
    start_date = datetime.datetime.strptime(start_dt, '%m/%d/%Y')
    end_date = datetime.datetime.strptime(end_dt, '%m/%d/%Y')
    
    for timecard in dict_list:
        if timecard['Customer'] == customer            and start_date <= datetime.datetime.strptime(timecard['Date'], '%m/%d/%y') < end_date: 
            if timecard['Billable']:
                billable_list.append([timecard['Customer'], timecard['Date'], timecard['Hours'], timecard['Details']])
            else:                    
                not_billable_list.append([timecard['Customer'], timecard['Date'], timecard['Hours'], timecard['Details']])
                    
            total_hours += float(timecard['Hours'])
    
    
    print("\nNon-Billables\n-------------\n")
    pprint(not_billable_list, width=160)
    print_summary(customer, sum(float(n) for n in list(item[2] for item in not_billable_list)), 'Non-Billable', rate)
    
    print("\nBillables\n-------------\n")
    pprint(billable_list, width=160)
    billable_hours = sum(float(n) for n in list(item[2] for item in billable_list))
    print_summary(customer, billable_hours, 'Billable', rate)
        
    
    while True:
        adjusted_hours = input("Hours to add/subtract: ")
        if not adjusted_hours: 
            print("... end of report.")
            break
            
        print("Rate is", rate)
        print_summary(customer, billable_hours + float(adjusted_hours), 'Billable', 60)
        
        
def print_summary(customer, hours, billtype, rate):    
    print("\n{} hours for {}: {} @ ${}/hour = ${:,.2f}\n".format(billtype, customer, hours, rate, hours*rate))


# In[ ]:


# ----------------------------------------------------------------------
# Main
if __name__ == '__main__':

    # Prompt for CSV file and convert it to a nested list
    time_list = csv_to_list(filedialog.askopenfilename(title='Select Timesheet CSV', filetypes=[("CSV","*.csv"),("All files","*.*")]))
  
    # Convert nested list to list of dictionaries 
    dict_list = lists_to_dicts(time_list)
    print("{} dictionary entries created.".format(len(dict_list)))

    # Print report, prompting for filters. (This is inelegant. Improve method of default values.)
    start_default = '01/01/2000'
    end_default = '01/01/2999'
    rate_default = 60

    customer = input("Customer: ")
    if not customer:
        print("Customer Name Required.\nTry running again.")

    else:
        start_date = input("Start Date ({}): ".format(start_default))
        end_date = input("Start Date ({}): ".format(end_default))

        if not start_date:
            start_date = start_default
        if not end_date:
            end_date = end_default

        print_report(customer, start_dt=start_date, end_dt=end_date, rate=rate_default)

