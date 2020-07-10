#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}
    route = []
    
    for ticket in tickets:
        if ticket.source not in hash:
            hash[ticket.source] = ticket.destination #key, value pair with source and dest
    
    cur = "NONE" #start at begining
    while True:
        for ticket in hash:
            if ticket == cur:
                route.append(hash[ticket])
                cur = hash[ticket]#move the pointer along the linked list
        
        print(cur)
        if cur == "NONE":
            break
            
    return route

