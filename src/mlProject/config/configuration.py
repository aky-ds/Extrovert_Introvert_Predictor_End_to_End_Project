from src.mlProject.constants import *
from src.mlProject.utils.common import read_yaml, create_directories
from src.mlProject.entity.config_entity import data_ingestion_config
from dataclasses import dataclass
from pathlib import Path

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> data_ingestion_config:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return data_ingestion_config(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )