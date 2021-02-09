import os.path as osp

CURRENT_PATH = osp.dirname(osp.realpath(__file__))

class Config():
    root_dir = osp.join(CURRENT_PATH, "..")
    data_dir = osp.join(root_dir, "data")

config = Config()
