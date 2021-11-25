# Creates 2 lists of vrTimers for each Child node
# 1st list turns nodes on from first to last
# 2nd list turns nodes off from last to first

off_interval = 0.04
on_interval = 0.03

# parent_node = vrNodeService.getNodeFromId(selected_node.getID())
parent_node = vrNodeService.findNode('Segments')

# Create 2 Lists for Off & On Sequence
children_on = parent_node.getChildren()
children_off = children_on[::-1]

node_lists = [children_off, children_on]
timer_lists = []

def createTimer(interval, node, state):
    t = vrTimer(interval, True)
    t.connect(lambda: node.setActive(state))
    t.connect(lambda: updateScenegraph(True))
    return(t)

node_ptrs = []
def createTimerList(lst):
    t = 0
    timers = []

    if len(timer_lists) == 0:
        state = False
        interval_type = off_interval
    else:
        state = True
        interval_type = on_interval
    
    for count, value in enumerate(lst, start=0):       
        node_name = getNodeName(value)
        node_ptr = findNode(node_name)
        node_ptrs.append(node_ptr)
        
        t = t + interval_type
        timers.append(createTimer(t, node_ptr, state))
        
    return(timers)

for i in node_lists:
    timer_lists.append(createTimerList(i))
    
for i in timer_lists[0]:
    i.setActive(True)

print('Timers created.')
