#!/usr/bin/python

def takeThird(elem):
  return elem[2]

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    print len(predictions)

    ### your code goes here
    all_data = [(age, net_worth, abs(prediction-net_worth))
        for age, net_worth, prediction in zip(ages, net_worths, predictions)]
    all_data.sort(key=takeThird)
    cleaned_data = all_data[:int(len(all_data)*0.9)]
    print len(cleaned_data)



    return cleaned_data
