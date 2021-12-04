# Creates 2 lists of vrTimers for each Child node
# 1st list turns nodes On, first to last
# 2nd list turns nodes Off, last to first

interval_off = 0.04
interval_on = 0.03

# parent_node = vrNodeService.getNodeFromId(selected_node.getID())
parent_node = vrNodeService.findNode('Segments')

# Create 2 Lists for Off & On Sequence
children_on = parent_node.getChildren()
children_off = children_on[::-1]

node_lists = [children_off, children_on]
timer_lists = []

def createTimer(interval, node, state):
    timer = vrTimer(interval, True)
    timer.connect(lambda: node.setActive(state))
    # Comment or remove next line if Scenegraph update is not required
    timer.connect(lambda: updateScenegraph(True))
    return(timer)

node_ptrs = []
def createTimerList(lst):
    interval = 0
    timers = []

    if len(timer_lists) == 0:
        state = False
        interval_type = interval_off
    else:
        state = True
        interval_type = interval_on
    
    for count, value in enumerate(lst, start=0):       
        node_name = getNodeName(value)
        node_ptr = findNode(node_name)
        node_ptrs.append(node_ptr)
        
        interval += interval_type
        timers.append(createTimer(interval, node_ptr, state))
        
    return(timers)

for i in node_lists:
    timer_lists.append(createTimerList(i))

print('Timers created.')
