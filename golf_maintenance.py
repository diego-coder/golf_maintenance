
from math import pi
from math import ceil
from math import floor

def calculate_rough_sod_area(length, width):

    rough_sod_area = ((length * width) - (calculate_smooth_sod_area(course_width) + calculate_sandtrap_area(course_width)))
    rough_sod_area_rounded_up = ceil(rough_sod_area)
    return rough_sod_area_rounded_up

def calculate_smooth_sod_area(width):
    radius_of_smooth_sod = ((width / 2) / 2)
    one_smooth_sod_area = pi * radius_of_smooth_sod ** 2
    total_smooth_sod_area = ceil(one_smooth_sod_area * 2)
    return total_smooth_sod_area

def calculate_sandtrap_area(width):
    radius_of_sand_trap = ((width / 3) / 2)
    sand_trap_area = pi * radius_of_sand_trap ** 2
    return sand_trap_area

def calculate_tons_of_sand(area_of_sand):
    area_of_trap_in_feet = area_of_sand * 9
    volume_of_sand = area_of_trap_in_feet * 1
    amount_of_sand_needed_in_lbs = volume_of_sand * 100
    sand_in_tons = ceil(amount_of_sand_needed_in_lbs / 2000)
    return sand_in_tons

def calculate_number_of_bricks(width):
    radius_of_sand_trap = ((width / 3) / 2)
    circumference_of_sand_trap = 2 * pi * radius_of_sand_trap
    circumference_in_feet = circumference_of_sand_trap * 3
    half_circumference = circumference_in_feet / 2
    number_of_bricks_needed = ceil(half_circumference * 3)
    return number_of_bricks_needed

def calculate_number_of_bushes(length, width):
    perimeter = 2 * (length + width)
    width_of_trails = 1 + 1
    number_of_bushes = floor(perimeter - width_of_trails)
    return number_of_bushes

def calculate_time_to_mow():
    smooth_sod_time_to_mow_in_minutes = calculate_smooth_sod_area(course_width) / 60
    rough_sod_area_time_to_mow_in_minutes = (calculate_rough_sod_area(course_length, course_width) * .5) / 60
    total_time_to_mow = ceil(smooth_sod_time_to_mow_in_minutes + rough_sod_area_time_to_mow_in_minutes)
    return total_time_to_mow

course_length = float(input("Enter course length in yards: "))
course_width = float(input("Enter course width in yards: "))

print("Total square yards of rough sod: " + str(calculate_rough_sod_area(course_length, course_width)) + ".")
print("Total square yards of smooth sod: " + str(calculate_smooth_sod_area(course_width)) + ".")
print("Tons of sand: " + str(calculate_tons_of_sand(calculate_sandtrap_area(course_width))) + ".")
print("Number of retaining wall bricks: " + str(calculate_number_of_bricks(course_width)) + ".")
print("Number of bushes: " + str(calculate_number_of_bushes(course_length, course_width)) + ".")
print("Total mowing time (mins): " + str(calculate_time_to_mow()) + ".")
