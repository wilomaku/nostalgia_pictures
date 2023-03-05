## Main functions

import torch
from PIL import Image
from lavis.models import load_model_and_preprocess

def caption_image(path_image):
    """
    Function to return caption for a given image
    """

    # setup device to use
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # load sample image
    raw_image = Image.open(path_image).convert("RGB")

    # loads BLIP caption base model, with finetuned checkpoints on MSCOCO captioning dataset.
    # this also loads the associated image processors
    model, vis_processors, _ = load_model_and_preprocess(name="blip_caption", model_type="base_coco", is_eval=True, device=device)
    # preprocess the image
    # vis_processors stores image transforms for "train" and "eval" (validation / testing / inference)
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    # generate caption
    caption = model.generate({"image": image})
    return caption

    #########################

    #model, vis_processors, txt_processors = load_model_and_preprocess(name="blip_vqa", model_type="vqav2", is_eval=True, device=device)
    # ask a random question.
    #question = "Which city is this photo taken?"
    #image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    #question = txt_processors["eval"](question)
    #caption = model.predict_answers(samples={"image": image, "text_input": question}, inference_method="generate")
    #print(caption)

    ########################
