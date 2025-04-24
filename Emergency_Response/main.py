import random
import time

class Location:
    def __init__(self, address, type_of_area):
        self.address = address  
        self.type_of_area = type_of_area 

class Person:
    def __init__(self, name, role, location):
        self.name = name
        self.role = role  
        self.location = location  
        self.status = 'safe'  

    def update_status(self, new_status):
        self.status = new_status
        print(f"{self.name}'s status updated to: {self.status}")

class Event:
    def __init__(self, event_type, location, description):
        self.event_type = event_type  
        self.location = location 
        self.description = description  
        self.status = 'pending'  

    def update_status(self, new_status):
        self.status = new_status
        print(f"Event at {self.location.address} is now {self.status}.")

class Responder:
    def __init__(self, name, responder_type):
        self.name = name  
        self.responder_type = responder_type  
        self.status = 'available' 

    def dispatch(self, event):
        self.status = 'responding'
        print(f"{self.name}, the {self.responder_type}, has been dispatched to the {event.event_type}.")
        event.update_status('in progress')

    def resolve_event(self, event):
        event.update_status('resolved')
        print(f"{self.name} has resolved the event at {event.location.address}.")
        self.status = 'available'
home = Location("123 Elm St", "residential")
street = Location("Main St & 5th Ave", "street")
office = Location("101 Corporate Blvd", "commercial")

def run_simulation():

    person1 = Person("John Deo", "victim", home)
    person2 = Person("Jane Smith", "bystander", street)
    event_types = ["fire", "accident", "medical emergency"]
    event_type = random.choice(event_types)
    if event_type == "fire":
        event_description = "House fire with people trapped inside"
    elif event_type == "accident":
        event_description = "Car accident with injuries"
    else:
        event_description = "Medical emergency with severe injuries"
    
    event_location = random.choice([home, street, office])
    emergency_event = Event(event_type, event_location, event_description)
    responder1 = Responder("Mike", "firefighter")
    responder2 = Responder("Emma", "paramedic")
    responder3 = Responder("John", "police officer")
    responders = [responder1, responder2, responder3]
    print(f"\nA new {emergency_event.event_type} has been reported at {emergency_event.location.address}.")
    
    for responder in responders:
        responder.dispatch(emergency_event)
        time.sleep(1)  
    time.sleep(2)
    for responder in responders:
        responder.resolve_event(emergency_event)
        time.sleep(1)  
    person1.update_status("rescued")
    person2.update_status("safe")

    print("\nSimulation complete!")

def random_event():
    event_types = ["fire", "accident", "medical emergency"]
    event_type = random.choice(event_types)
    location = random.choice([home, street, office])
    description = ""
    if event_type == "fire":
        description = "House fire with people trapped inside"
    elif event_type == "accident":
        description = "Car accident with injuries"
    else:
        description = "Medical emergency with severe injuries"
    return Event(event_type, location, description)
   
def simulate_response_time():
    response_time = random.randint(1, 5)  
    print(f"Responder will take {response_time} seconds to reach the location.")
    time.sleep(response_time)

def update_victim_status(person, status):
    print(f"{person.name} is now {status}.")
    person.update_status(status)

def handle_multiple_events():
    events = [random_event() for _ in range(3)]  
    for event in events:
        print(f"Handling event: {event.event_type} at {event.location.address}")
        run_simulation() 

if __name__ == "__main__":
    run_simulation()
