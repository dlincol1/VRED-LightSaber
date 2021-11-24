# Create segmented cylinder
group_node  = createNode('Transform', 'Segments')

overall_length = 1000
cylinder_radius = 10
cylinder_sides = 18
cylinder_segments = 10

segment_length = round((overall_length / cylinder_segments), 2)
print(f'Segment length: {segment_length} ({cylinder_segments})')

offset = segment_length / 2
Y_pos = 0
count = 1

while count <= cylinder_segments:
    cylinder_segment = createCylinder(
        segment_length, cylinder_radius, cylinder_sides, True, False, False, 0, 1, 0)
    cylinder_segment.setTranslation(0, Y_pos + offset, 0)
    cylinder_segment.setName("_SL_" + str(segment_length) + "_" + str(count))

    group_node.addChild(cylinder_segment)
    Y_pos += segment_length
    count += 1