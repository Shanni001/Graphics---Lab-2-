import cairo


# Image dimensions
WIDTH, HEIGHT = 500, 600

# Define colors


# Create the surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Draw background
context.set_source_rgb(0.9,0.9,1)
context.rectangle(0, 0, WIDTH, HEIGHT)
context.fill()

# Top rectangle (the top face of the cube)
context.set_source_rgb(0.4, 0.8, 0.4)
context.move_to(200, 310)
context.line_to(430, 350)
context.line_to(270, 490)
context.line_to(50, 450)
context.close_path()
context.fill()
# Front face (facing the viewer)
context.set_source_rgb(0.3, 0.7, 0.3)
context.move_to(50, 450)
context.line_to(270, 490)
context.line_to(270, 510)
context.line_to(50, 470)
context.close_path()
context.fill()
# Right side face (gives the 3D effect)
context.set_source_rgb(0.2, 0.6, 0.2)
context.move_to(270, 490)
context.line_to(430, 350)
context.line_to(430, 370)
context.line_to(270, 510)
context.close_path()
context.fill()



#House
context.set_source_rgb(1, 1, 1)
context.move_to(120, 415)
context.line_to(120, 210)
context.line_to(180, 190)
context.line_to(260, 260)
context.line_to(260, 440)
context.close_path()
context.fill()

context.set_source_rgb(0.9, 0.9, 0.9)
context.move_to(260, 440)
context.line_to(260, 260)
context.line_to(350, 190)
context.line_to(350, 365)
context.close_path()
context.fill()

#shadow
context.set_source_rgb(0.8, 0.8, 0.8)
context.move_to(120, 415)
context.line_to(120, 405)
context.line_to(260, 430)
context.line_to(350, 355)
context.line_to(350, 365)
context.line_to(260, 440)
context.close_path()
context.fill()


#Roof
context.set_source_rgb(0, 0, 0.2)
context.move_to(95, 220)
context.line_to(190, 150)
context.line_to(270, 120)
context.line_to(170, 200)
context.close_path()
context.fill()
context.set_source_rgb(0.03, 0.20, 0.36)
context.move_to(270, 120)
context.line_to(170, 200)
context.line_to(255, 265)
context.line_to(360, 180)
context.close_path()
context.fill()
#shadow
context.set_source_rgb(0.8, 0.8, 0.9)
context.move_to(260, 260)
context.line_to(260, 280)
context.line_to(350, 207)
context.line_to(350, 190)
context.close_path()
context.fill()

# Window 1
context.set_source_rgb(0.8, 0.8, 1)
context.move_to(140, 250)
context.line_to(140, 300)
context.line_to(175, 305)
context.line_to(175, 255)
context.close_path()
context.fill()

# Glare for Window 1
context.set_source_rgb(1, 1, 1)
context.move_to(140, 280)
context.line_to(175, 275)
context.set_line_width(10)
context.stroke()
context.set_source_rgb(1, 1, 1)
context.move_to(140, 290)
context.line_to(175, 285)
context.set_line_width(2)
context.stroke()

# Window 2 (moved right)
context.set_source_rgb(0.8, 0.8, 1)
context.move_to(185, 255)
context.line_to(185, 305)
context.line_to(220, 310)
context.line_to(220, 260)
context.close_path()
context.fill()

# Glare for Window 2
context.set_source_rgb(1, 1, 1)
context.move_to(185, 280)
context.line_to(220, 275)
context.set_line_width(10)
context.stroke()
context.set_source_rgb(1, 1, 1)
context.move_to(185, 290)
context.line_to(225, 285)
context.set_line_width(2)
context.stroke()

# Window 3 (moved down)
context.set_source_rgb(0.8, 0.8, 1)
context.move_to(140, 350)
context.line_to(140, 400)
context.line_to(175, 405)
context.line_to(175, 355)
context.close_path()
context.fill()

# Glare for Window 3
context.set_source_rgb(1, 1, 1)
context.move_to(140, 380)
context.line_to(175, 375)
context.set_line_width(10)
context.stroke()
context.set_source_rgb(1, 1, 1)
context.move_to(140, 390)
context.line_to(175, 385)
context.set_line_width(2)
context.stroke()

# Window 4 (moved down and right)
context.set_source_rgb(0.8, 0.8, 1)
context.move_to(185, 355)  # Position it down and right
context.line_to(185, 405)
context.line_to(220, 410)
context.line_to(220, 360)
context.close_path()
context.fill()

# Glare for Window 4
context.set_source_rgb(1, 1, 1)
context.move_to(185, 380)
context.line_to(220, 375)
context.set_line_width(10)
context.stroke()
context.set_source_rgb(1, 1, 1)
context.move_to(185, 390)
context.line_to(225, 385)
context.set_line_width(2)
context.stroke()

# Window right
context.set_source_rgb(0.8, 0.8, 1)
context.move_to(270, 278)
context.line_to(270, 328)
context.line_to(305, 300)
context.line_to(305, 250)
context.close_path()
context.fill()

context.set_source_rgb(0.8, 0.8, 1)
context.move_to(315, 245)
context.line_to(315, 295)
context.line_to(345, 270)
context.line_to(345, 220)
context.close_path()
context.fill()

context.set_source_rgb(1, 1, 1)
context.move_to(270, 303)
context.line_to(305, 273)
context.set_line_width(5)

context.stroke()

context.set_source_rgb(1, 1, 1)
context.move_to(270, 313)
context.line_to(305, 285)
context.set_line_width(2)
context.stroke()
# Glare for second window
context.set_source_rgb(1, 1, 1)
context.move_to(315, 270)
context.line_to(345, 240)
context.set_line_width(5)
context.stroke()

context.set_source_rgb(1, 1, 1)
context.move_to(315, 280)
context.line_to(345, 250)
context.set_line_width(2)
context.stroke()



#door

context.set_source_rgb(0,0,0)
context.move_to(315, 325)
context.line_to(315, 390)
context.line_to(345, 365)
context.line_to(345, 303)
context.close_path()
context.fill()

context.set_source_rgb(0.6, 0.6, 1)
context.move_to(320, 325)
context.line_to(320, 380)
context.line_to(330, 373)
context.line_to(330, 318)
context.close_path()
context.fill()

context.set_source_rgb(1, 1, 1)
context.move_to(317, 350)
context.line_to(317, 360)
context.set_line_width(5)
context.stroke()


#chimney

context.set_source_rgb(0.8, 0.8, 0.8)
context.move_to(290, 165)
context.line_to(290, 210)
context.line_to(310, 190)
context.line_to(310, 148)
context.close_path()
context.fill()
context.set_source_rgb(0.9, 0.9, 0.9)
context.move_to(290, 165)
context.line_to(290, 210)
context.line_to(270, 190)
context.line_to(270, 145)
context.close_path()
context.fill()

context.set_source_rgb(0.8, 0.8, 0.8)
context.move_to(290, 165)
context.line_to(310, 148)
context.line_to(290, 130)
context.line_to(270, 145)

context.close_path()
context.fill()

context.set_source_rgb(1,1,1)
context.move_to(290, 158)
context.line_to(303, 148)
context.line_to(290, 135)
context.line_to(278, 145)

context.close_path()
context.fill()






# Save the image
surface.write_to_png("house.png")
