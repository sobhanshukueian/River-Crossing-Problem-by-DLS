import collections
import time

class Problem:
    un_ex = []
    expanded = []
    def __init__(self, start_state, max_depth) -> None:
        self.un_ex.append(start_state) 
        self.max_depth = max_depth
        
    def serach(self):
        while True:
            try:
                head = self.un_ex[-1]
                if head.isValid():
                    if head.isGoal():
                        self.pathShow(head, 0.5) 
                        print('Done !!!')
                        return
                    
                    if not self.expandeded(head):
                        self.expanded.append(head) 
                        self.un_ex.pop(-1)
                        
                        if head.depth < self.max_depth:
                            self.un_ex.extend(head.generator())  
                    else:
                        self.un_ex.pop(-1)
                else:
                    self.un_ex.pop(-1)
            except IndexError:
                print('Depth Limit : {}'.format(self.max_depth))
                return
                
    
    def expandeded(self, state):
        for node in self.expanded:
            if (collections.Counter(node.left_side) == collections.Counter(state.left_side) and
                collections.Counter(node.right_side) == collections.Counter(state.right_side) and 
                node.boat_side == state.boat_side):
                return True
        return False
            
    def pathShow(self, state, delay):
        print(state.show(), '\n')
        while state.parent != None:
            time.sleep(delay)
            state = state.parent
            print(state.show(), '\n')
        