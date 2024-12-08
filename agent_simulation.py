import random

class LocationState:
    def __init__(self):
        self.room1="dirty"
        self.room2="dirty"
    
    def set_room_state(self, room, state):
        if room == 'room1':
            self.room1= state
        elif room=='room2':
            self.room2=state
        else:
            raise ValueError("Invalid room. choose room1 or room2.")
    def get_room_state(self,room):
        if room=='room1':
            return self.room1
        elif room=='room2':
            return self.room2
        else:
            raise ValueError("Invalid room. Choose room1 or room2.")
class Agent:
    def __init__(self, name, location):
        self.name=name
        self.location=location

    def move(self):
        if self.location=="room1":
            self.location="room2"
        elif self.location=="room2":
            self.location="room1"
        else:
            "invalid room you are in"        
        print(f"{self.name} moved to {self.location}")

    def clean(self, location_state):
        location_state.set_room_state(self.location,"clean")
        print(f"{self.name} cleaned {self.location}")

    def observe(self, location_state):
        state = location_state.get_room_state(self.location)
        print(f"{self.name} observes that {self.location} is {state}")
        return state
def random_agent_function(location_state,agent):
    random_number = random.randint(1, 3)
    if random_number== 1:
        agent.move()
    elif random_number== 2:
        agent.clean(location_state)
    else:
        agent.observe(location_state)
iteration=0

def table_based_agent_function(location_state,agent):
    global iteration
    move_table=[2,1,2]

    move_number=move_table[iteration%3]
    if move_number== 1:
        agent.move()
    elif move_number== 2:
        agent.clean(location_state)
    else:
        agent.observe(location_state)
    iteration +=1
def reflex_based_agent_function(location_state, agent):
    state = agent.observe(location_state)
    if state == "dirty":
        agent.clean(location_state)
    elif state == "clean":
        agent.move()  
def one_iteration_of_simulation(agent_function,location_state,agent):
    for i in range(10):
        agent_function(location_state,agent)
    if location_state.room1=="clean" and location_state.room2=="clean":
        return "success"
    else: 
        return "failiure"
    


def simulation():
    random_agent= Agent("Random Agent","room1")
    reflex_agent= Agent("Reflex Agent","room1")
    table_agent= Agent("Table Agent","room1")
    succes_iteration_random=0
    succes_iteration_reflex=0
    succes_iteration_table=0
    location_state = LocationState()
    for i in range(10):
        success_state=one_iteration_of_simulation(table_based_agent_function,location_state,table_agent)
        if(success_state=="success"):
            succes_iteration_table +=1
        print(success_state)
    location_state = LocationState()
    
    for i in range(10):
        success_state=one_iteration_of_simulation(random_agent_function,location_state,random_agent)
        if(success_state=="success"):
            succes_iteration_random +=1
    location_state = LocationState()
    
    for i in range(10):
        success_state=one_iteration_of_simulation(reflex_based_agent_function,location_state,reflex_agent)
        if(success_state=="success"):
            succes_iteration_reflex +=1
    print(f"random agent:{succes_iteration_random}")
    print(f"reflex agent:{succes_iteration_reflex}")
    print(f"table agent:{succes_iteration_table}")

simulation()