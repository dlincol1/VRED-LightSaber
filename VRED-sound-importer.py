# Import Sound files into a Group node

import os

audio_dir = "C:/VRED_Audio/"

scene_parent = createNode('Group', 'Sounds', True)

def importSound(filename):
    full_path = audio_dir + filename

    sound_node = createNode("Sound", filename, scene_parent)
    sound_node.setFieldString("soundFile", full_path)
    sound_node.setFieldBool("play", False)
    sound_node.setFieldBool("loop", False)

    return(sound_node)
    
for file in os.listdir(audio_dir):
    node = importSound(file)
    print(f'Imported {node.getName()}')

updateScenegraph(True)