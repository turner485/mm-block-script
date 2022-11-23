from helpers import encode
from pathlib import Path
from os import path
import os.path
import os
import xlrd

_path = Path.cwd()
absolute_path = (str(_path)) + '..\\..'
image_urls = absolute_path + '\\resources\\Media_gb_1.csv'
image_links = absolute_path + '\\resources\\mm-blocks-links.xlsx'
alt_data_sheet = absolute_path + '\\resources\\mm-blocks-data-alt-output.xls'

alt_x = xlrd.open_workbook(alt_data_sheet)
alt_x_sheet = alt_x.sheet_by_name('data')
alt_x_sheet_us = alt_x.sheet_by_name('us_data')
alt_x_sheet_de = alt_x.sheet_by_name('de_data')

print('Building MM block impexes')

def general_MM():
    for subdir, dirs, files in os.walk(sub_path):
        for file in files:
            with open(os.path.join(subdir, file)) as outfile:
                html_file_data = outfile.read()
                if "UK" in subdir:
                    try:
                        women_alt = alt_x_sheet.cell_value(1,0)
                        men_alt = alt_x_sheet.cell_value(2,0)
                        gifts_alt = alt_x_sheet.cell_value(0,0)
                    except IndexError:
                        pass
                    for image in open(image_urls):
                        if "UK" in image and "jpg" in image:
                            file_string = file.replace(".html", "")
                            if file_string in image:
                                try: 
                                    html_file_data = html_file_data.replace('[IMAGE_SOURCE_JPG]', image)
                                    html_file_data = html_file_data.replace('[WOMEN_ALT_TEXT]', women_alt)
                                    html_file_data = html_file_data.replace('[MEN_ALT_TEXT]', men_alt)
                                    html_file_data = html_file_data.replace('[GIFTS_ALT_TEXT]', gifts_alt)
                                    html_file_data = html_file_data.replace('\n', '')
                                except:
                                    pass
                                with open(absolute_path + '\\production\\UK\\'  + file, 'w') as file_data:
                                    file_data.write(html_file_data)
                                    file_data.close()
                        if "UK" in image and "webp" in image:
                            file_string = file.replace(".html", "")
                            if file_string in image:
                                html_file_data = html_file_data.replace('[IMAGE_SOURCE_WEBP]', image)
                                html_file_data = html_file_data.replace('\n', '')
                                with open(absolute_path + '\\production\\UK\\'  + file, 'w') as file_data:
                                    file_data.write(html_file_data)
                                    file_data.close()
                if "US" in subdir:
                    try:
                        newin_alt = alt_x_sheet_us.cell_value(0,0)
                        gifts_alt = alt_x_sheet_us.cell_value(1,0)
                        women_alt = alt_x_sheet_us.cell_value(2,0)
                        men_alt = alt_x_sheet_us.cell_value(3,0)
                        girls_alt = alt_x_sheet_us.cell_value(4,0)
                        boys_alt = alt_x_sheet_us.cell_value(5,0)
                        baby_alt = alt_x_sheet_us.cell_value(6,0)
                    except IndexError:
                        pass
                    for image in open(image_urls):
                        if "US" in image and "jpg" in image:
                            file_string = file.replace(".html", "")
                            if file_string in image:
                                try:
                                    html_file_data = html_file_data.replace('[IMAGE_SOURCE_JPG]', image)
                                    html_file_data = html_file_data.replace('[NEWIN_ALT_TEXT]', newin_alt)
                                    html_file_data = html_file_data.replace('[GIFTS_ALT_TEXT]', gifts_alt)
                                    html_file_data = html_file_data.replace('[WOMEN_ALT_TEXT]', women_alt)
                                    html_file_data = html_file_data.replace('[MEN_ALT_TEXT]', men_alt)
                                    html_file_data = html_file_data.replace('[GIRLS_ALT_TEXT]', girls_alt)
                                    html_file_data = html_file_data.replace('[BOYS_ALT_TEXT]', boys_alt)
                                    html_file_data = html_file_data.replace('[BABY_ALT_TEXT]', baby_alt)
                                except:
                                    pass
                                html_file_data = html_file_data.replace('\n', '')
                                with open(absolute_path + '\\production\\US\\' + file, 'w') as file_data:
                                    file_data.write(html_file_data)
                                    file_data.close()
                        if "US" in image and "webp" in image:
                            file_string = file.replace(".html", "")
                            if file_string in image:
                                html_file_data = html_file_data.replace('[IMAGE_SOURCE_WEBP]', image)
                                html_file_data = html_file_data.replace('\n', '')
                                with open(absolute_path + '\\production\\US\\'  + file, 'w') as file_data:
                                    file_data.write(html_file_data)
                                    file_data.close()
                if "DE" in subdir:
                    try: 
                        newin_alt = alt_x_sheet_de.cell_value(0,0)
                        gifts_alt = alt_x_sheet_de.cell_value(1,0)
                        women_alt = alt_x_sheet_de.cell_value(2,0)
                        men_alt = alt_x_sheet_de.cell_value(3,0)
                        girls_alt = alt_x_sheet_de.cell_value(4,0)
                        boys_alt = alt_x_sheet_de.cell_value(5,0)
                        baby_alt = encode(alt_x_sheet_de.cell_value(6,0))
                    except IndexError:
                        pass
                    for image in open(image_urls):
                        if "DE" in image and "jpg" in image:
                            file_string = file.replace(".html", "")
                            if file_string in image:
                                try:
                                    html_file_data = html_file_data.replace('[IMAGE_SOURCE_JPG]', image)
                                    html_file_data = html_file_data.replace('[NEWIN_ALT_TEXT]', newin_alt)
                                    html_file_data = html_file_data.replace('[GIFTS_ALT_TEXT]', gifts_alt)
                                    html_file_data = html_file_data.replace('[WOMEN_ALT_TEXT]', women_alt)
                                    html_file_data = html_file_data.replace('[MEN_ALT_TEXT]', men_alt)
                                    html_file_data = html_file_data.replace('[GIRLS_ALT_TEXT]', girls_alt)
                                    html_file_data = html_file_data.replace('[BOYS_ALT_TEXT]', boys_alt)
                                    html_file_data = html_file_data.replace('[BABY_ALT_TEXT]', baby_alt)
                                    html_file_data = html_file_data.replace('\n', '')
                                except:
                                    pass
                                with open(absolute_path + '\\production\\DE\\' + file, 'w') as file_data:
                                    file_data.write(html_file_data)
                                    file_data.close()
                        if "DE" in image and "webp" in image:
                            file_string = file.replace(".html", "")
                            if file_string in image:
                                html_file_data = html_file_data.replace('[IMAGE_SOURCE_WEBP]', image)
                                html_file_data = html_file_data.replace('\n', '')
                                with open(absolute_path + '\\production\\DE\\'  + file, 'w') as file_data:
                                    file_data.write(html_file_data)
                                    file_data.close()
def multi_MM():
    pet_template = absolute_path + "\\templates\\Regular\\uk\\Pet.html"
    rooms_template = absolute_path + "\\templates\\Regular\\uk\\Rooms.html"
    pet_url_jpg = []
    pet_url_webp = []
    rooms_url_jpg = []
    rooms_url_webp = []
    try: 
        for image in open(image_urls):
            if "pet".lower() in image.lower() and "webp" not in image:
                pet_url_jpg.append(image)
            if "pet".lower() in image.lower() and "webp" in image:
                pet_url_webp.append(image)
            if "room".lower() in image.lower() and "webp" not in image:
                rooms_url_jpg.append(image)
            if "room".lower() in image.lower() and "webp" in image:
                rooms_url_webp.append(image)
    except:
        pass
    x = xlrd.open_workbook(image_links)
    xl_pets = x.sheet_by_name('Pets')
    xl_rooms = x.sheet_by_name('Rooms')
    try:
        pet_cta_one = xl_pets.cell_value(0,1).split('/')[len(xl_pets.cell_value(0,1).split('/')) - 1].replace('-', ' ')
        pet_cta_two = xl_pets.cell_value(1,1).split('/')[len(xl_pets.cell_value(1,1).split('/')) - 1].replace('-', ' ')
        pet_cta_three = xl_pets.cell_value(2,1).split('/')[len(xl_pets.cell_value(2,1).split('/')) - 1].replace('-', ' ')
        pet_cta_four = xl_pets.cell_value(3,1).split('/')[len(xl_pets.cell_value(3,1).split('/')) - 1].replace('-', ' ')
        # pet_alt_one = alt_x_sheet.cell_value(5,0)
        # pet_alt_two = alt_x_sheet.cell_value(6,0)
        # pet_alt_three = alt_x_sheet.cell_value(7,0)
        # pet_alt_four = alt_x_sheet.cell_value(8,0)
        pet_tracking_one = pet_cta_one.replace(' ', '')
        pet_tracking_two = pet_cta_two.replace(' ', '')
        pet_tracking_three = pet_cta_three.replace(' ', '')
        pet_tracking_four = pet_cta_four.replace(' ', '')
        rooms_cta_one = xl_rooms.cell_value(0,1).split('/')[len(xl_rooms.cell_value(0,1).split('/')) - 1].replace('-', ' ')
        rooms_cta_two = xl_rooms.cell_value(1,1).split('/')[len(xl_rooms.cell_value(1,1).split('/')) - 1].replace('-', ' ')
        rooms_cta_three = xl_rooms.cell_value(2,1).split('/')[len(xl_rooms.cell_value(2,1).split('/')) - 1].replace('-', ' ')
        rooms_cta_four = xl_rooms.cell_value(3,1).split('/')[len(xl_rooms.cell_value(3,1).split('/')) - 1].replace('-', ' ')
        rooms_tracking_one = rooms_cta_one.replace(' ', '')
        rooms_tracking_two = rooms_cta_two.replace(' ', '')
        rooms_tracking_three = rooms_cta_three.replace(' ', '')
        rooms_tracking_four = rooms_cta_four.replace(' ', '')
    except: 
        pass
    with open(pet_template) as outfile:
        html_file_data = outfile.read()
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_JPG_1]", pet_url_jpg[0])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_JPG_2]", pet_url_jpg[1])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_JPG_3]", pet_url_jpg[2])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_JPG_4]", pet_url_jpg[3])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_WEBP_1]", pet_url_webp[0])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_WEBP_2]", pet_url_webp[1])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_WEBP_3]", pet_url_webp[2])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_WEBP_4]", pet_url_webp[3])
        html_file_data = html_file_data.replace(f"[CTA_COPY_1]", pet_cta_one)
        html_file_data = html_file_data.replace(f"[CTA_COPY_2]", pet_cta_two)
        html_file_data = html_file_data.replace(f"[CTA_COPY_3]", pet_cta_three)
        html_file_data = html_file_data.replace(f"[CTA_COPY_4]", pet_cta_four)
        html_file_data = html_file_data.replace(f"[TRACKING_1]", pet_tracking_one)
        html_file_data = html_file_data.replace(f"[TRACKING_2]", pet_tracking_two)
        html_file_data = html_file_data.replace(f"[TRACKING_3]", pet_tracking_three)
        html_file_data = html_file_data.replace(f"[TRACKING_4]", pet_tracking_four)
        html_file_data = html_file_data.replace("[LINK_1]", xl_pets.cell_value(0,1))
        html_file_data = html_file_data.replace("[LINK_2]", xl_pets.cell_value(1,1))
        html_file_data = html_file_data.replace("[LINK_3]", xl_pets.cell_value(2,1))
        html_file_data = html_file_data.replace("[LINK_4]", xl_pets.cell_value(3,1))
        html_file_data = html_file_data.replace("[PETS_ALT_TEXT_1]", alt_x_sheet.cell_value(6,0))
        html_file_data = html_file_data.replace("[PETS_ALT_TEXT_2]", alt_x_sheet.cell_value(7,0))
        html_file_data = html_file_data.replace("[PETS_ALT_TEXT_3]", alt_x_sheet.cell_value(8,0))
        html_file_data = html_file_data.replace("[PETS_ALT_TEXT_4]", alt_x_sheet.cell_value(9,0))
        html_file_data = html_file_data.replace('\n', '').replace('</a>', '</a>\n').replace('<div class="explore-mm-container">', '<div class="explore-mm-container">\n')
    with open(absolute_path + '\\production\\UK\\Pet.html', 'w') as file_data:
        file_data.write(html_file_data)
        file_data.close()   
    with open(rooms_template) as outfile:
        html_file_data = outfile.read()
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_JPG_1]", rooms_url_jpg[0])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_JPG_2]", rooms_url_jpg[1])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_JPG_3]", rooms_url_jpg[2])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_JPG_4]", rooms_url_jpg[3])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_WEBP_1]", rooms_url_webp[0])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_WEBP_2]", rooms_url_webp[1])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_WEBP_3]", rooms_url_webp[2])
        html_file_data = html_file_data.replace(f"[IMAGE_SOURCE_WEBP_4]", rooms_url_webp[3])
        html_file_data = html_file_data.replace(f"[CTA_COPY_1]", rooms_cta_one)
        html_file_data = html_file_data.replace(f"[CTA_COPY_2]", rooms_cta_two)
        html_file_data = html_file_data.replace(f"[CTA_COPY_3]", rooms_cta_three)
        html_file_data = html_file_data.replace(f"[CTA_COPY_4]", rooms_cta_four)
        html_file_data = html_file_data.replace(f"[TRACKING_1]", rooms_tracking_one)
        html_file_data = html_file_data.replace(f"[TRACKING_2]", rooms_tracking_two)
        html_file_data = html_file_data.replace(f"[TRACKING_3]", rooms_tracking_three)
        html_file_data = html_file_data.replace(f"[TRACKING_4]", rooms_tracking_four)
        html_file_data = html_file_data.replace("[LINK_1]", xl_rooms.cell_value(0,1))
        html_file_data = html_file_data.replace("[LINK_2]", xl_rooms.cell_value(1,1))
        html_file_data = html_file_data.replace("[LINK_3]", xl_rooms.cell_value(2,1))
        html_file_data = html_file_data.replace("[LINK_4]", xl_rooms.cell_value(3,1))
        html_file_data = html_file_data.replace("[ROOM_ALT_TEXT_1]", alt_x_sheet.cell_value(11,0))
        html_file_data = html_file_data.replace("[ROOM_ALT_TEXT_2]", alt_x_sheet.cell_value(12,0))
        html_file_data = html_file_data.replace("[ROOM_ALT_TEXT_3]", alt_x_sheet.cell_value(13,0))
        html_file_data = html_file_data.replace("[ROOM_ALT_TEXT_4]", alt_x_sheet.cell_value(14,0))
        html_file_data = html_file_data.replace('\n', '').replace('</a>', '</a>\n').replace('<div class="explore-mm-container">', '<div class="explore-mm-container">\n')
    with open(absolute_path + '\\production\\UK\\Rooms.html', 'w') as file_data:
        file_data.write(html_file_data)
        file_data.close()

def garden():
    with open(sub_path + "\\UK\\Garden.html") as outfile:
        html_file_data = outfile.read()
        for image in open(image_urls):
            garden_alt = alt_x_sheet.cell_value(10,0)
            if "Garden" in image and "jpg" in image:
                html_file_data = html_file_data.replace('[IMAGE_SOURCE_JPG]', image)
                html_file_data = html_file_data.replace('[GARDEN_ALT_TEXT]', garden_alt)
            if "Garden" in image and "webp" in image:
                html_file_data = html_file_data.replace('[IMAGE_SOURCE_JPG]', image)    
            with open(absolute_path + '\\production\\UK\\Garden.html', 'w') as file_data:
                file_data.write(html_file_data)
                file_data.close()
            with open(absolute_path + '\\production\\UK\\Garden.html') as outfile:
                html_file_data = outfile.read()
                x = xlrd.open_workbook(image_links)
                xl_other = x.sheet_by_name('Garden')
                html_file_data = html_file_data.replace("[LINK]", xl_other.cell_value(0,1))
            with open(absolute_path + '\\production\\UK\\Garden.html', 'w') as file_data:
                file_data.write(html_file_data)
                file_data.close()
        
def move_to_impex():
    try:
        with open(absolute_path + '\\templates\\impex\\UK.impex') as outfile:
            impex_file_data = outfile.read()
            for subdir, dirs, files in os.walk(absolute_path + "\\production\\uk\\"):
                for file in files:
                    with open(os.path.join(subdir, file)) as outfile:
                        html_file_data = outfile.read()
                        html_file_data = html_file_data.replace('"', '""')
                        if 'Rooms' in html_file_data:
                            impex_file_data = impex_file_data.replace("[ROOMS_MM_BLOCK]", html_file_data)
                        if 'Pet' in html_file_data:
                            impex_file_data = impex_file_data.replace("[PET_MM_BLOCK]", html_file_data)
                        if "MENS" in html_file_data:
                            impex_file_data = impex_file_data.replace("[MEN_MM_BLOCK]", html_file_data)
                        if "WOMENS" in html_file_data:
                            impex_file_data = impex_file_data.replace("[WOMEN_MM_BLOCK]", html_file_data)
                        if "GIFTS" in html_file_data:
                            impex_file_data = impex_file_data.replace("[GIFTS_MM_BLOCK]", html_file_data)
                        if "GARDEN" in html_file_data:
                            impex_file_data = impex_file_data.replace("[GARDEN_MM_BLOCK]", html_file_data)
                        # print(impex_file_data)
                        with open(absolute_path + '\\production\\impex\\UK.impex', 'w') as file_data:
                            file_data.write(impex_file_data)
                            file_data.close()
    except:
        pass
    try:
        with open(absolute_path + '\\templates\\impex\\US.impex') as outfile:
            impex_file_data = outfile.read()
            for subdir, dirs, files in os.walk(absolute_path + "\\production\\US\\"):
                for file in files:
                    with open(os.path.join(subdir, file)) as outfile:
                        html_file_data = outfile.read()
                        html_file_data = html_file_data.replace('"', '""')
                        if 'BABY' in html_file_data:
                            impex_file_data = impex_file_data.replace("[BABY_MM_BLOCK]", html_file_data)
                        if 'BOYS' in html_file_data:
                            impex_file_data = impex_file_data.replace("[BOYS_MM_BLOCK]", html_file_data)
                        if "GIFTS" in html_file_data:
                            impex_file_data = impex_file_data.replace("[GIFTS_MM_BLOCK]", html_file_data)
                        if "GIRLS" in html_file_data:
                            impex_file_data = impex_file_data.replace("[GIRLS_MM_BLOCK]", html_file_data)
                        if "MENS" in html_file_data:
                            impex_file_data = impex_file_data.replace("[MEN_MM_BLOCK]", html_file_data)
                        if "NEWIN" in html_file_data:
                            impex_file_data = impex_file_data.replace("[NEWIN_MM_BLOCK]", html_file_data)
                        if "WOMEN" in html_file_data:
                            impex_file_data = impex_file_data.replace("[WOMEN_MM_BLOCK]", html_file_data)
                        with open(absolute_path + '\\production\\impex\\US.impex', 'w') as file_data:
                            file_data.write(impex_file_data)
                            file_data.close()
    except:
        pass
    try:
        with open(absolute_path + '\\templates\\impex\\DE.impex') as outfile:
            impex_file_data = outfile.read()
            for subdir, dirs, files in os.walk(absolute_path + "\\production\\DE\\"):
                for file in files:
                    with open(os.path.join(subdir, file)) as outfile:
                        html_file_data = outfile.read()
                        html_file_data = html_file_data.replace('"', '""')
                        if 'BABY' in html_file_data:
                            impex_file_data = impex_file_data.replace("[BABY_MM_BLOCK]", html_file_data)
                        if 'BOYS' in html_file_data:
                            impex_file_data = impex_file_data.replace("[BOYS_MM_BLOCK]", html_file_data)
                        if "GIFTS" in html_file_data:
                            impex_file_data = impex_file_data.replace("[GIFTS_MM_BLOCK]", html_file_data)
                        if "GIRLS" in html_file_data:
                            impex_file_data = impex_file_data.replace("[GIRLS_MM_BLOCK]", html_file_data)
                        if "MENS" in html_file_data:
                            impex_file_data = impex_file_data.replace("[MEN_MM_BLOCK]", html_file_data)
                        if "NEWIN" in html_file_data:
                            impex_file_data = impex_file_data.replace("[NEWIN_MM_BLOCK]", html_file_data)
                        if "WOMEN" in html_file_data:
                            impex_file_data = impex_file_data.replace("[WOMEN_MM_BLOCK]", html_file_data)
                        # print(impex_file_data)
                        with open(absolute_path + '\\production\\impex\\DE.impex', 'w') as file_data:
                            file_data.write(impex_file_data)
                            file_data.close()
    except:
        pass
def remove_empty():
    try:
        with open(absolute_path + '\\production\\impex\\UK.impex') as outfile:
            impex_file_data = outfile.read()
            if "[GIFTS_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[GIFTS_MM_BLOCK]"', "<ignore>")
            if "[GARDEN_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[GARDEN_MM_BLOCK]"', "<ignore>")
            if "[PET_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[PET_MM_BLOCK]"', "<ignore>")
            if "[ROOMS_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[ROOMS_MM_BLOCK]"', "<ignore>")
            if "[WOMEN_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[WOMEN_MM_BLOCK]"', "<ignore>")
            if "[MEN_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[MEN_MM_BLOCK]"', "<ignore>")
            with open(absolute_path + '\\production\\impex\\UK.impex', 'w') as file_data:
                file_data.write(impex_file_data)
                file_data.close()
    except:
        pass
    try:
        with open(absolute_path + '\\production\\impex\\DE.impex') as outfile:
            impex_file_data = outfile.read()
            if "[BABY_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[BABY_MM_BLOCK]"', "<ignore>")
            if "[BOYS_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[BOYS_MM_BLOCK]"', "<ignore>")
            if "[GIRLS_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[GIRLS_MM_BLOCK]"', "<ignore>")
            if "[GIFTS_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[GIFTS_MM_BLOCK]"', "<ignore>")
            if "[MEN_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[MEN_MM_BLOCK]"', "<ignore>")
            if "[NEWIN_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[NEWIN_MM_BLOCK]"', "<ignore>")
            if "[WOMEN_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[WOMEN_MM_BLOCK]"', "<ignore>")
            with open(absolute_path + '\\production\\impex\\DE.impex', 'w') as file_data:
                file_data.write(impex_file_data)
                file_data.close()
    except:
        pass
    try:
        with open(absolute_path + '\\production\\impex\\US.impex') as outfile:
            impex_file_data = outfile.read()
            if "[BABY_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[BABY_MM_BLOCK]"', '<ignore>')
            if "[BOYS_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[BOYS_MM_BLOCK]"', '<ignore>')
            if "[GIRLS_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[GIRLS_MM_BLOCK]"', '<ignore>')
            if "[GIFTS_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[GIFTS_MM_BLOCK]"', '<ignore>')
            if "[MEN_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[MEN_MM_BLOCK]"', '<ignore>')
            if "[NEWIN_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[NEWIN_MM_BLOCK]"', '<ignore>')
            if "[WOMEN_MM_BLOCK]" in impex_file_data:
                impex_file_data = impex_file_data.replace('"[WOMEN_MM_BLOCK]"', '<ignore>')
            with open(absolute_path + '\\production\\impex\\US.impex', 'w') as file_data:
                file_data.write(impex_file_data)
                file_data.close()
    except:
        pass
general_MM()
multi_MM()
garden()
move_to_impex()
remove_empty()