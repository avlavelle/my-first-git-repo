

my_shapes = ['circle', 'heart', 'triangle', 'square']

with open('my_shapes.txt', 'w') as f:
    for shape in my_shapes:
        f.write(shape)
