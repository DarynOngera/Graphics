import math


def draw_side_house(context, origin_x, origin_y, width, height):
    """
    Draws a house with a roof and two windows.

    Parameters:
    context -- the Cairo drawing context
    origin_x, origin_y -- the starting point (origin) for the drawing
    width, height -- the dimensions of the house (main body, not including roof overhang)
    """

    # Scaling factors for the house components
    roof_height_ratio = 0.4  # Roof height relative to house height
    window_width_ratio = 0.2  # Window width relative to house width
    window_height_ratio = 0.25  # Window height relative to house height
    window_spacing_ratio = 0.1  # Space between windows relative to house width

    # Derived dimensions for components
    roof_height = height * roof_height_ratio
    window_width = width * window_width_ratio
    window_height = height * window_height_ratio
    window_spacing = width * window_spacing_ratio

    # Set color to black for the house base
    context.set_source_rgb(0, 0, 0)  # Black

    # Draw the base of the house (main rectangle)
    context.rectangle(origin_x, origin_y + roof_height, width, height)
    context.fill()

    # Draw the roof as a right-angled trapezium
    roof_overhang = width * 0.15  # Roof overhang relative to house width
    context.move_to(origin_x - roof_overhang, origin_y + roof_height)  # Start at left bottom corner, overhangs
    context.line_to(origin_x + width, origin_y + roof_height)  # Right bottom corner of roof (aligned with the house)
    context.line_to(origin_x + width, origin_y)  # Top-right corner of roof
    context.line_to(origin_x + width * 0.4, origin_y)  # Slanted side of roof on left side
    context.close_path()  # Close the shape
    context.fill()

    # Draw the two windows
    context.set_source_rgb(1, 1, 1)  # White for windows

    # Left window
    window1_x = origin_x + window_spacing
    window1_y = origin_y + roof_height + (height / 2) - (window_height / 2)
    context.rectangle(window1_x, window1_y, window_width, window_height)
    context.fill()

    # Right window
    window2_x = origin_x + width - window_spacing - window_width
    window2_y = window1_y  # Same y-coordinate as the left window
    context.rectangle(window2_x, window2_y, window_width, window_height)
    context.fill()


def draw_center(ctx):
    # Center
    ctx.move_to(130, 170)
    ctx.line_to(130, 270)
    ctx.line_to(260, 270)
    ctx.line_to(260, 170)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill_preserve()
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()

    ctx.rectangle(160, 220, 34, 47)
    ctx.rectangle(196, 220, 34, 47)
    ctx.fill()

    ctx.move_to(160, 220)
    ctx.curve_to(170, 210, 180, 210, 194, 210)
    ctx.line_to(194, 220)
    ctx.close_path()
    ctx.fill()

    ctx.move_to(196, 210)
    ctx.curve_to(210, 210, 220, 210, 229, 220)
    ctx.line_to(196, 220)
    ctx.close_path()
    ctx.fill()

    # Structure of center block
    ctx.move_to(130, 170)
    ctx.line_to(130, 270)
    ctx.line_to(260, 270)
    ctx.line_to(260, 170)
    ctx.line_to(240, 160)
    ctx.line_to(150, 160)
    ctx.close_path()
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill_preserve()
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()

    # Structure of center roof
    ctx.move_to(120, 180)
    ctx.line_to(150, 160)
    ctx.line_to(240, 160)
    ctx.line_to(270, 180)
    ctx.line_to(270, 170)
    ctx.line_to(240, 150)
    ctx.line_to(150, 150)
    ctx.line_to(120, 170)
    ctx.close_path()
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill_preserve()
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()

    # Center block window
    ctx.arc(195, 175, 10, math.radians(0), math.radians(360))
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

    # Roof above the door
    ctx.move_to(150, 220)
    ctx.line_to(195, 200)
    ctx.line_to(240, 220)
    ctx.line_to(240, 210)
    ctx.line_to(195, 190)
    ctx.line_to(150, 210)
    ctx.close_path()
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill_preserve()
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()

    # Doors
    ctx.rectangle(160, 220, 34, 47)
    ctx.rectangle(196, 220, 34, 47)
    ctx.fill()

    ctx.move_to(160, 220)
    ctx.curve_to(170, 210, 180, 210, 194, 210)
    ctx.line_to(194, 220)
    ctx.close_path()
    ctx.fill()

    ctx.move_to(196, 210)
    ctx.curve_to(210, 210, 220, 210, 229, 220)
    ctx.line_to(196, 220)
    ctx.close_path()
    ctx.fill()

    # Top part
    ctx.rectangle(170, 100, 50, 50)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(1)
    ctx.fill_preserve()
    ctx.stroke()

    ctx.move_to(180, 120)
    ctx.line_to(180, 147)
    ctx.line_to(210, 147)
    ctx.line_to(210, 120)
    ctx.arc(195, 120, 15, math.pi, 0)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(1)
    ctx.fill_preserve()
    ctx.stroke()


def draw_tapered_tower_with_cross(ctx, origin_x, origin_y, width, height):

    # Set black color for the shape
    ctx.set_source_rgb(0, 0, 0)  # Black color

    # Draw the tapered tower (trapezoid)
    bottom_y = origin_y + height * 0.8
    top_y = origin_y + height * 0.2
    taper_left_x = origin_x + width * 0.1
    taper_right_x = origin_x + width * 0.9
    near_top_left_x = origin_x + width * 0.4
    near_top_right_x = origin_x + width * 0.6

    # Trapezoid coordinates
    ctx.move_to(taper_left_x, bottom_y)  # Bottom-left
    ctx.line_to(taper_right_x, bottom_y)  # Bottom-right
    ctx.line_to(near_top_right_x, top_y)  # Near top-right
    ctx.line_to(near_top_left_x, top_y)  # Near top-left

    ctx.close_path()  # Close the shape
    ctx.fill()

    # Draw the cross at the top
    ctx.set_line_width(width * 0.05)  # Set line width relative to the width of the tower

    # Vertical part of the cross
    cross_center_x = origin_x + width * 0.5
    cross_top_y = origin_y
    cross_bottom_y = origin_y + height * 0.2
    ctx.move_to(cross_center_x, cross_top_y)  # Vertical top
    ctx.line_to(cross_center_x, cross_bottom_y)  # Vertical bottom
    ctx.stroke()

    # Horizontal part of the cross
    cross_left_x = origin_x + width * 0.4
    cross_right_x = origin_x + width * 0.6
    cross_mid_y = origin_y + height * 0.1
    ctx.move_to(cross_left_x, cross_mid_y)  # Horizontal left
    ctx.line_to(cross_right_x, cross_mid_y)  # Horizontal right
    ctx.stroke()