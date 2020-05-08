#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
#      starting location is the key and
#   the destination is the value
    route = []
    dicty = {}

    for i in tickets:
        dicty[i.source] = i.destination

    route.append(dicty["NONE"])
    final_destination = dicty["NONE"]

    while final_destination != "NONE":
        if final_destination == "NONE":
            continue
        else:
            route.append(dicty[final_destination])
            final_destination = dicty[final_destination]
    return route
  


