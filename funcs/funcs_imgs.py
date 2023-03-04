## Main functions

from lavis.models import load_model_and_preprocess
import torch

def match_text_text(text1, text2):
    """
    Function to give matching score between two phrases (text1, text2)
    """

    # setup device to use
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model, vis_processors, txt_processors = load_model_and_preprocess(name="blip_feature_extractor", model_type="base", is_eval=True, device=device)

    text_input = txt_processors["eval"](text1)
    sample1 = {"image": None, "text_input": [text_input]}

    text_input = txt_processors["eval"](text2)
    sample2 = {"image": None, "text_input": [text_input]}

    features_text1 = model.extract_features(sample1, mode="text")
    features_text2 = model.extract_features(sample2, mode="text")

    similarity = features_text1.text_embeds_proj[:,0,:] @ features_text2.text_embeds_proj[:,0,:].t()

    return similarity.item()
