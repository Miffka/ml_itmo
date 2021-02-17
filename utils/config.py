import os.path as osp
import torch


CURRENT_PATH = osp.dirname(osp.realpath(__file__))

class Config():
    root_dir = osp.join(CURRENT_PATH, "..")
    data_dir = osp.join(root_dir, "data")
    model_dir = osp.join(root_dir, "models")
    log_dir = osp.join(root_dir, "runs")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

config = Config()
