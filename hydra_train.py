import logging
from omegaconf import DictConfig, OmegaConf
import hydra

from train import main

# A logger for this file
log = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="config", config_name="config")
def my_app(cfg):
    log.info("Info level message")
    log.debug("Debug level message")
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
