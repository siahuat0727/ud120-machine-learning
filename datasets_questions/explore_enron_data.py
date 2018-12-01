#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
count = 0
three_person = ["LAY KENNETH L", "SKILLING JEFFREY K", "FASTOW ANDREW S"]
num_quantified_salary = 0
num_known_email_address = 0
num_nan_payment = 0
for d in enron_data:
  # print d
  # for key, value in enron_data[d].iteritems():
  #   print value
  print "payment ", enron_data[d]['total_payments']
  if enron_data[d]['total_payments'] == 'NaN':
    print "haha "
    num_nan_payment += 1
  if enron_data[d]['salary'] != 'NaN':
    num_quantified_salary += 1
  if enron_data[d]['email_address'] != 'NaN':
    num_known_email_address += 1
  if d in three_person:
    print d, enron_data[d]['total_payments']
  if d == "SKILLING JEFFREY K":
    # for dd in enron_data[d]:
    #   print dd
    print "haha ", enron_data[d]["exercised_stock_options"]

  if d == "COLWELL WESLEY":
    print enron_data[d]["from_this_person_to_poi"]
  if d == "PRENTICE JAMES":
    print enron_data[d]["total_stock_value"]
    # for dd in enron_data[d]:
    #   print dd
  if enron_data[d]['poi'] == 1:
    count += 1
print count
print "num salary ", num_quantified_salary
print "num email ", num_known_email_address
print "num nan payment/total ", float(num_nan_payment) / len(enron_data)
