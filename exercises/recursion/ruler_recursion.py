# Recursion example - English Ruler.  
# from Goodrich et al

def draw_line(tick_length, tick_label = ' '):
    """ Draw one line with given length, label optional """
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """ Draw tick interval based on central line length"""
    if center_length > 0:
        draw_interval(center_length -1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    """Draw English ruler with a given number of inches, center tick length"""
    for j in range (1,1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

draw_ruler(3,5)
        
    