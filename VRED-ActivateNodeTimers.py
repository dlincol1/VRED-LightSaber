index = 0 if node_ptrs[0].getActive() else 1
       
try:
    sound_ptrs[index].setFieldBool("play", True)
    
except:
    print('\nSound list not configured.')
    
for i in timer_lists[index]: i.setActive(True)
