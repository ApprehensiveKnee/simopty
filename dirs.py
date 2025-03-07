import os

CONFIG_FILES_DIR = os.path.join(os.path.dirname(__file__), "config_files")
EX_DIR = "/home/ecabiati/cellar/restart/bin/run_restart"
ARCH_FILE = os.path.join(CONFIG_FILES_DIR, "arch.json")
RUN_FILES_DIR = os.path.join(CONFIG_FILES_DIR, "runs")
CONFIG_DUMP_DIR = os.path.join(CONFIG_FILES_DIR, "dumps")
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")