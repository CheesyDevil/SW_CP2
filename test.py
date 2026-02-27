import turtle

def recursive_clone_draw(t, depth):
    if depth == 0:
        return
    
    # Clone the current turtle without naming it
    new_clone = t.clone()
    
    # Manipulate the new clone
    new_clone.forward(50)
    new_clone.right(60)
    
    # Recursive call
    recursive_clone_draw(new_clone, depth - 1)

# Set up original turtle
t = turtle.Turtle()
t.speed(0)

# Start recursion
recursive_clone_draw(t, 5)

turtle.done()