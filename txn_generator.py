"""A module for simulating a full transaction history.

.. moduleauthor:: Ben Moyer <bmoyer@medicaid-genius.com>
"""
import datetime
import random

def generate_transaction(year, month, day, amount):
    """Generates one transaction consisting of a date and a dollar amount"""
    date = datetime.date(year, month, day)
    return date, amount


def get_amount():
    medium_amt_prob, large_amt_prob, debit_prob = [random.random() for i in range(3)]
    amount = random.random()*10
    if medium_amt_prob > 0.8:
        amount += random.random()*100
    if large_amt_prob > 0.9:
        amount += random.random()*1000
    if debit_prob > 0.25:
        amount *= -1
    return amount


def generate_history(start_date, end_date, density):
    """Generates a general, random, realistic transaction history
    between a start and end date.  Recurrent transactions and transfers
    are added by the other functions."""
    txn_list = list()
    for date in daterange(start_date, end_date):
        txn_prob = random.random()
        if txn_prob >= 0.2:
            amount = get_amount()
            txn = generate_transaction(date.year, date.month, date.day, round(amount,2))
            txn_list.append(txn)

            # Possibly add more transactions to this day
            mult_txn_prob = random.random()
            if mult_txn_prob > 0.8:
                for x in range(random.randint(1,3)):
                    amount = get_amount()
                    txn = generate_transaction(date.year, date.month, date.day, round(amount,2))
                    txn_list.append(txn)
        else:
            continue
    return txn_list


def daterange(start_date, end_date):
    """Returns generator for iterating between an inclusive range of dates"""
    for n in range(int ((end_date - start_date).days) + 1):
        yield start_date + datetime.timedelta(n)


def add_recurring_txns(txn_list, base_amt, frequency, amt_tol=0, freq_tol=0):
    """Adds recurring transactions to a list of transaction tuples (date, amt)"""

    
 

if __name__ == '__main__':
    start = datetime.date(2014, 7, 15)
    end = datetime.date(2014, 8, 7)
    num_dates = int((end - start).days)

    txns = generate_history(start, end, 1)
    txns_with_recurring = add_recurring_txns(txns, base_amt, frequency="monthly", freq_tol=0, amt_tol=0)


    print("Generated",len(txns), "transactions over", num_dates, "days.\n")
    print(*txns, sep='\n')
