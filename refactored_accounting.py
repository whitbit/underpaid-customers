melon_cost = 1.00

def get_underpaid_customers(data_file):
    """ parse customer payment data to search for customers who underpaid """

    data = open(data_file)

    for line in data:

        customer_data = line.split('|')
        
        name = customer_data[1]

        correct_total = float(customer_data[2]) * melon_cost

        payment_total = float(customer_data[3])

        if correct_total > payment_total:
            
            print '{} paid ${:.2f}'.format(name, payment_total)
            print 'The correct total was ${:.2f}'.format(correct_total)

    data.close()

get_underpaid_customers('customer-orders.txt')
