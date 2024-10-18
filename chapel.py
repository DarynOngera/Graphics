import math

import cairo

from helpers import draw_side_house, draw_tapered_tower_with_cross, draw_center

# Example usage
# Create an image surface
WIDTH, HEIGHT = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Set the background color to white
ctx.set_source_rgb(1, 1, 1)  # White background
ctx.paint()

# Draw a house with the origin at (30, 30) and dimensions (90, 60)
draw_side_house(ctx, origin_x=40, origin_y=185, width=90, height=60)
draw_side_house(ctx, origin_x=350, origin_y=185, width=-90, height=60)
draw_center(ctx)
draw_tapered_tower_with_cross(ctx,170, 17, 50, 100)

# Save the image
surface.write_to_png("church.png")
