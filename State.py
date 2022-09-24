from Person import Person

# Generate People
thief = Person("Thief", False)
police = Person("Police", True)
mother = Person("Mother", True)
father = Person("Father", True)
girl = Person("Girl", False)
girl2 = Person("Girl", False)
boy = Person("Boy", False)
boy2 = Person("Boy", False)

class State:
    def __init__(self, left_side, right_side, boat_side, depth, parent) :
        self.left_side = left_side
        self.right_side = right_side
        self.boat_side = boat_side
        self.depth = depth
        self.parent = parent

    def generator(self):
        states = []
        if self.boat_side :
            current_side = self.left_side
            other_side = self.right_side
        else:
            current_side = self.right_side
            other_side = self.left_side
        
        for role in  current_side:
            for role2 in current_side:
                current_side_copy = current_side.copy()
                other_side_copy = other_side.copy()
                
                if role == role2:
                    continue
                #Checking validation for person1 and person2 for transmission
                if not role.can_ride and not role2.can_ride:continue
                if not self.boatValidation([role, role2]):continue
                    
                #self current_side
                current_side_copy.remove(role)
                current_side_copy.remove(role2)

                #self other_side
                other_side_copy.append(role)
                other_side_copy.append(role2)
                
                if self.boat_side: new_state = State(current_side_copy, other_side_copy, False, self.depth + 1, self)
                else:new_state = State(other_side_copy,current_side_copy, True,self.depth + 1,self)
                if not new_state in states: states.append(new_state)
        
            for person in current_side:
                current_side_copy = current_side.copy()
                other_side_copy = other_side.copy()
                
                if person.can_ride:
                    current_side_copy.remove(person)
                    other_side_copy.append(person)
                    if self.boat_side: new_state = State(current_side_copy, other_side_copy, False, self.depth + 1, self)
                    else:new_state = State(other_side_copy, current_side_copy, True, self.depth + 1, self )
                    states.append(new_state)    
        return states
        

    
    def isValid(self):
        if self.sideValidation(self.right_side) and self.sideValidation(self.left_side): return True
        return False


    def sideValidation(self, side):
        if mother in side and father not in side and boy in side: return False
        elif father in side and mother not in side and girl in side: return False
        elif mother in side and father not in side and boy2 in side: return False
        elif father in side and mother not in side and girl2 in side: return False
        elif thief in side and len(side) > 1 and police not in side: return False
        else: return True
    
    def boatValidation(self, people):
        if girl in people and father in people: return False
        elif girl2 in people and father in people: return False
        elif boy in people and mother in people: return False
        elif boy2 in people and mother in people: return False
        elif thief in people and police not in people: return False
        else: return True

                   
    def isGoal(self):
        if len(self.right_side) == 0: return True
        return False

    def show(self):
        print('Boat left side: {}'.format([item.show() for item in self.left_side]))
        print('Boat Right_side: {}'.format([item.show() for item in self.right_side]))
        print('boat on left') if self.boat_side else print('boat on right')


START_STATE = State([], [police, thief, girl2, girl, father, boy, boy2, mother], False, 0, None)
