import os
from glob import glob
import json

from funcs import funcs_text as ft
from funcs import funcs_imgs as fi

def get_match_text():

    t1 = 'This is a example'
    t2 = 'A cute dog'
    t3 = 'A cute table'
    t4 = 'A cute animal'

    score_sim = ft.match_text_text(t1, t2)
    print(score_sim)
    score_sim = ft.match_text_text(t1, t3)
    print(score_sim)
    score_sim = ft.match_text_text(t2, t3)
    print(score_sim)

    score_sim = ft.match_text_text(t4, t1)
    print(score_sim)
    score_sim = ft.match_text_text(t4, t2)
    print(score_sim)
    score_sim = ft.match_text_text(t4, t3)
    print(score_sim)

def get_path(folder):

    imgfiles = []
    extensions = ['png', 'jpg', 'jpeg']
    for extension in extensions:
        imgfiles.extend([y for x in os.walk(folder) for y in glob(os.path.join(x[0], '*.{}'.format(extension)))])
        imgfiles.extend([y for x in os.walk(folder) for y in glob(os.path.join(x[0], '*.{}'.format(extension.upper())))])

    return imgfiles

def get_captions(folder, save_path):

    path_dict = "{}capt_images.json".format(save_path)

    if os.path.isfile(path_dict):
        with open(path_dict) as json_file:
            dict_captions = json.load(json_file)
    else:
        dict_captions = {}

    all_images = get_path(folder)

    for image in all_images:
        caption = fi.caption_image(image)
        dict_captions[image] = caption[0]

    with open(path_dict, "w") as fp:
        json.dump(dict_captions, fp)

    return caption


#get_match_text()
path = '/DOC/backup/fotos/'
save_path = '/home/wilomaku/Downloads/'


for sub_path in []:
    print('Processing {}'.format(sub_path))
    get_captions('{}{}/'.format(path, sub_path), save_path)
