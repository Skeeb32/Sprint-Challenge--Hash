from hashtable import (HashTable,
                        put,
                        delete,
                        get,
                        resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length-1)

    for t in tickets:
        put(hashtable, t.source, t.destination)
    
    route[0] = get(hashtable, "NONE")
    for t in range(1, length-1):
        val = get(hashtable, route[t-1])
        if val != None:
            route[t] = get(hashtable, route[t-1])
    
    return route