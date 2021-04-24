

import matplotlib.pyplot as plt

def show_simple_field(size_x, size_y, solutions):

    figure, axes = plt.subplots(figsize=(8, 8)) 

    for i in range(0, size_x * size_y):
        row = int(i / size_y)
        col = i % size_x
        cc = plt.Circle(( col/20 + .025 , row/20 + .025), .02, color="green" )
        axes.add_artist(cc)
        plt.text(col/20 + .015, row/20 + .015, solutions[i])

    axes.set_aspect(1)
    plt.title( 'Field' ) 
    plt.show()

def show_field_with_scouts(size_x, size_y, solutions, scouts, flower_patches):

    figure, axes = plt.subplots(figsize=(8, 8)) 
    for i in range(0, size_x * size_y):
        row = int(i / size_y)
        col = i % size_x
        cc = plt.Circle(( col/20 + .025 , row/20 + .025), .02, color="green" )
        if i in scouts:
            cc = plt.Circle(( col/20 + .025 , row/20 + .025), .02, color="blue" )
        axes.add_artist(cc)
        plt.text(col/20 + .015, row/20 + .015, solutions[i])
    # ar = plt.Arrow(.01, .02, .07, .05, width=.01)  
    # axes.add_artist(ar)

    for patch in flower_patches:
        row = int(patch[0] / size_y)
        col = patch[0] % size_x
        rect = plt.Rectangle((col/20-patch[1]/20, row/20-patch[1]/20), patch[1]/10+.05, patch[1]/10+.05, fill=False)
        axes.add_artist(rect)

    axes.set_aspect( 1 )
    plt.title( 'Field with scouts(Blue) and the flower patches' ) 
    plt.show()

def show_field_with_foragers(size_x, size_y, solutions, scouts, flower_patches, f):

    figure, axes = plt.subplots(figsize=(8, 8)) 
    for i in range(0, size_x * size_y):
        row = int(i / size_y)
        col = i % size_x
        cc = plt.Circle(( col/20 + .025 , row/20 + .025), .02, color="green" )
        if i in scouts:
            cc = plt.Circle(( col/20 + .025 , row/20 + .025), .02, color="blue" )
        if i in f:
            cc = plt.Circle(( col/20 + .025 , row/20 + .025), 0.02, color="red" )
        axes.add_artist(cc)
        plt.text(col/20 + .015, row/20 + .015, solutions[i])
    # ar = plt.Arrow(.01, .02, .07, .05, width=.01)  
    # axes.add_artist(ar)

    for patch in flower_patches:
        row = int(patch[0] / size_y)
        col = patch[0] % size_x
        rect = plt.Rectangle((col/20-patch[1]/20, row/20-patch[1]/20), patch[1]/10+.05, patch[1]/10+.05, fill=False)
        axes.add_artist(rect)

    axes.set_aspect( 1 )
    plt.title( 'Field with scouts(Blue), foragers(Red), and the flower patches' ) 
    plt.show()

def show_field_with_scouts_and_maximums(size_x, size_y, solutions, scouts, flower_patches, local_maximums):

    figure, axes = plt.subplots(figsize=(8, 8)) 
    for i in range(0, size_x * size_y):
        row = int(i / size_y)
        col = i % size_x
        cc = plt.Circle(( col/20 + .025 , row/20 + .025), .02, color="green" )
        if i in local_maximums:
            cc = plt.Circle(( col/20 + .025 , row/20 + .025), .02, color="yellow" )
        if i in scouts:
            cc = plt.Circle(( col/20 + .025 , row/20 + .025), .02, color="blue" )
        axes.add_artist(cc)
        plt.text(col/20 + .015, row/20 + .015, solutions[i])
    # ar = plt.Arrow(.01, .02, .07, .05, width=.01)  
    # axes.add_artist(ar)

    for patch in flower_patches:
        row = int(patch[0] / size_y)
        col = patch[0] % size_x
        rect = plt.Rectangle((col/20-patch[1]/20, row/20-patch[1]/20), patch[1]/10+.05, patch[1]/10+.05, fill=False)
        axes.add_artist(rect)

    axes.set_aspect( 1 )
    plt.title( 'Field with scouts(Blue), local maximums found(Yellow), and the flower patches' ) 
    plt.show()

