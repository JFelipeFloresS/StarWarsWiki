import math
import SWAPI.api_connect as swapi
import pygame
import ctypes
from PIL import Image, ImageSequence

pygame.init()

sys = ctypes.windll.user32
width = sys.GetSystemMetrics(0)
height = sys.GetSystemMetrics(1)
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

black = (39, 43, 48)
blue = (163, 180, 202)
orange = (252, 101, 25)
white = (247, 247, 249)

def draw_text(text, size, color, pos_x, pos_y, text_center=True):
    options_text = pygame.font.SysFont("TAHOMA", size)
    text_surf = options_text.render(text, True, color)
    text_rect = text_surf.get_rect()
    if text_center: text_rect.center = (int(pos_x), int(pos_y))
    else: text_rect = (int(pos_x), int(pos_y))
    win.blit(text_surf, text_rect)

select_categories = ("PLANETS", "CHARACTERS", "STARSHIPS", "VEHICLES", "SPECIES", "FILMS")
selected_category = select_categories[0]

info = swapi.get_json(selected_category)

def draw_top_panel():
    bg_img = pygame.image.load('bg.png')
    win.blit(pygame.transform.scale(bg_img, (width, height)), (0, 0, width, height))
    logo_img = pygame.image.load('logo.png')
    pygame.draw.rect(win, white, [15, 15, logo_img.get_width(), logo_img.get_height()])
    win.blit(logo_img, (15, 15))
    p_x = width / (len(select_categories) + 1)
    for category in select_categories:
        colour = white
        bg = black
        if selected_category == category:
            colour = orange
            bg = blue
        pygame.draw.rect(win, bg, [p_x - (width / 20), height / 35, width / 10, height / 20])
        draw_text(category, 20, colour, p_x, height / 20)
        p_x += width / (len(select_categories) + 1)

def print_long_text(text, colour, pos_x, pos_y, size, limit_per_line):
    if len(text) <= limit_per_line:
        draw_text(text, size, colour, pos_x, pos_y)
        return
    p_y = pos_y
    for i in range(int(math.ceil(len(text) / limit_per_line))):
        if (i * limit_per_line) + limit_per_line <= len(text):
            draw_text(text[int(i * limit_per_line):int((i * limit_per_line) + limit_per_line)], size, colour, pos_x, p_y)
        else:
            draw_text(text[(i * limit_per_line):], size, colour, pos_x, p_y)
        p_y += size

def print_details(results, category, pos_x, pos_y):
    if category == select_categories[0]:
        draw_text("Population: " + results['population'], 12, black, pos_x, pos_y + (height / 20))
        draw_text("Climate: " + results['climate'], 12, black, pos_x, pos_y + (1.5 * (height / 20)))
        print_long_text("Terrain: " + results['terrain'], black, pos_x, pos_y + (2 * (height / 20)), 12, 30)
        draw_text("Day length: " + results['rotation_period'], 12, black, pos_x, pos_y + (3 * (height / 20)))
        draw_text("Year length: " + results['orbital_period'], 12, black, pos_x, pos_y + (3.5 * (height / 20)))
        draw_text("Diameter: " + results['diameter'], 12, black, pos_x, pos_y + (4 * (height / 20)))
    elif category == select_categories[1]:
        if results['height'] != 'unkown':
            draw_text("Height: " + results['height'] + " cm", 12, black, pos_x, pos_y + (1.5 * (height / 20)))
        else:
            draw_text("Height: " + results['height'], 12, black, pos_x, pos_y + (1.5 * (height / 20)))

        if results['mass'] != 'unknown':
            draw_text("Weight: " + results['mass'] + "Kg", 12, black, pos_x, pos_y + (2 * (height / 20)))
        else:
            draw_text("Weight: " + results['mass'], 12, black, pos_x, pos_y + (2 * (height / 20)))
        draw_text("Hair colour: " + results['hair_color'], 12, black, pos_x, pos_y + (2.5 * (height / 20)))
        draw_text("Skin colour: " + results['skin_color'], 12, black, pos_x, pos_y + (3 * (height / 20)))
        draw_text("Eye colour: " + results['eye_color'], 12, black, pos_x, pos_y + (3.5 * (height / 20)))
        draw_text("Year of birth: " + results['birth_year'], 12, black, pos_x, pos_y + (4 * (height / 20)))
        draw_text("Gender: " + results['gender'], 12, black, pos_x, pos_y + (4.5 * (height / 20)))
        # draw_text("Home world: " + swapi.get_selected(results['homeworld'])['name'], 12, black, pos_x, pos_y + (5 * (height / 20)))
    elif category == select_categories[2]:
        draw_text("Model: " + results['model'], 12, black, pos_x, pos_y + (1.5 * (height / 20)))
        print_long_text("Manufacturer: " + results['manufacturer'], black, pos_x, pos_y + (2 * (height / 20)), 12, 30)
        if results['cost_in_credits'] != ' unknown':
            print_long_text("Price: R " + results['cost_in_credits'], black, pos_x, pos_y + (3 * (height / 20)), 12, 30)
        else:
            draw_text("Price: " + results['cost_in_credits'], 12, black, pos_x, pos_y)
        draw_text("Crew: " + results['crew'], 12, black, pos_x, pos_y + (3.5 * (height / 20)))
        draw_text("Passenger capacity: " + results['passengers'], 12, black, pos_x, pos_y + (4 * (height / 20)))
        draw_text("Cargo capacity: " + results['cargo_capacity'], 12, black, pos_x, pos_y + (4.5 * (height / 20)))
        draw_text("Hyperdrive rating: " + results['hyperdrive_rating'], 12, black, pos_x, pos_y + (5 * (height / 20)))
    elif category == select_categories[3]:
        draw_text("Model: " + results['model'], 12, black, pos_x, pos_y + (1.5 * (height / 20)))
        print_long_text("Manufacturer: " + results['manufacturer'], black, pos_x, pos_y + (2 * (height / 20)), 12, 30)
        if results['cost_in_credits'] != ' unknown':
            print_long_text("Price: R " + results['cost_in_credits'], black, pos_x, pos_y + (3 * (height / 20)), 12, 30)
        else:
            draw_text("Price: " + results['cost_in_credits'], 12, black, pos_x, pos_y)
        draw_text("Crew: " + results['crew'], 12, black, pos_x, pos_y + (3.5 * (height / 20)))
        draw_text("Passenger capacity: " + results['passengers'], 12, black, pos_x, pos_y + (4 * (height / 20)))
        draw_text("Cargo capacity: " + results['cargo_capacity'], 12, black, pos_x, pos_y + (4.5 * (height / 20)))
        draw_text("Vehicle class: " + results['vehicle_class'], 12, black, pos_x, pos_y + (5 * (height / 20)))
        draw_text("Max speed: " + results['max_atmosphering_speed'] + " Km/h", 12, black, pos_x, pos_y + (5.5 * (height / 20)))
    elif category == select_categories[4]:
        draw_text("Classification: " + results['classification'], 12, black, pos_x, pos_y + (1.5 * (height / 20)))
        draw_text("Designation: " + results['designation'], 12, black, pos_x, pos_y + (2 * (height / 20)))
        draw_text("Average height: " + results['average_height'], 12, black, pos_x, pos_y + (2.5 * (height / 20)))
        print_long_text("Skin colours: " + results['skin_colors'], black, pos_x, pos_y + (3 * (height / 20)), 12, 30)
        print_long_text("Hair colours: " + results['hair_colors'], black, pos_x, pos_y + (3.7 * (height / 20)), 12, 30)
        print_long_text("Eye colours: " + results['eye_colors'], black, pos_x, pos_y + (4.5 * (height / 20)), 12, 30)
        draw_text("Average lifespan: " + results['average_lifespan'], 12, black, pos_x, pos_y + (5.3 * (height / 20)))
        draw_text("Language: " + results['language'], 12, black, pos_x, pos_y + (5.8 * (height / 20)))
    elif category == select_categories[5]:
        draw_text(str(results['episode_id']), 20, black, pos_x, pos_y + (1.5 * (height / 20)))

def draw_main_panel():
    items_per_row = 5
    if selected_category == select_categories[5]:
        items_per_row = 3
    p_x = width / (items_per_row + 1)
    p_y = (height / 5)
    c = 0
    for i in info['results']:
        pygame.draw.rect(win, white, [p_x - (width / ((items_per_row * 2) + 3)), p_y - (height / 30), width / (items_per_row + 1), height / 3])
        pygame.draw.rect(win, blue, [p_x - (width / ((items_per_row * 2) + 3)), p_y - (height / 30), width / (items_per_row + 1), height / 3], 2)
        if "name" not in i:
            print_long_text(i['title'], black, p_x, p_y, 30, int(75 / items_per_row))
        elif "name" in i:
            print_long_text(i['name'], black, p_x, p_y, 30, int(75 / items_per_row))

        print_details(i, selected_category, p_x, p_y)
        p_x += width / (items_per_row + 1)
        c += 1
        if c >= items_per_row:
            c = 0
            p_x = width / (items_per_row + 1)
            p_y += (height / 3)

    previous_colour = black
    next_colour = black
    if info['previous'] is None:
        previous_colour = blue
    if info['next'] is None:
        next_colour = blue

    pygame.draw.rect(win, orange, [(0.2 * width) - 2, (0.95 * height) - 2, (0.06 * width) + 4, (0.03 * height) + 4])
    pygame.draw.rect(win, white, [0.2 * width, 0.95 * height, 0.06 * width, 0.03 * height])
    pygame.draw.rect(win, orange, [(0.69 * width) - 2, (0.95 * height) - 2, (0.05 * width) + 4, (0.03 * height) + 4])
    pygame.draw.rect(win, white, [0.69 * width, 0.95 * height, 0.05 * width, 0.03 * height])
    draw_text("PREVIOUS", 20, previous_colour, width / 5, 0.95 * height, False)
    draw_text("NEXT", 20, next_colour, (width / 5) + (width / 2), 0.95 * height, False)

def screen_transition():
    surf = pygame.Surface((width, height))
    surf.set_alpha(128)
    surf.fill(black)
    win.blit(surf, (0, 0))
    loading = pygame.image.load('loading.gif')
    win.blit(loading, [0.45 * width, 0.35 * height])

def main_loop():
    while True:
        global info
        win.fill(white)
        draw_top_panel()
        draw_main_panel()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 0.4 * width >= pos[0] >= width / 5 and height >= pos[1] >= 0.95 * height:
                    if info['previous'] is not None:
                        screen_transition()
                        info = swapi.get_selected(info['previous'])

                if 0.9 * width >= pos[0] >= 0.7 * width and height >= pos[1] >= 0.95 * height:
                    if info['next'] is not None:
                        screen_transition()
                        info = swapi.get_selected(info['next'])

                if (height / 35) + (height / 20) >= pos[1] >= height / 35:
                    p_x = (width / (len(select_categories) + 1)) - (width / 20)
                    for s in select_categories:
                        if p_x + (width / 10) >= pos[0] >= p_x:
                            global selected_category
                            screen_transition()
                            selected_category = s
                            info = swapi.get_json(selected_category)

                        p_x += width / (len(select_categories) + 1)

        pygame.display.update()

main_loop()
