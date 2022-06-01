import logging

import hydra
from hydra.core.hydra_config import HydraConfig

from train import main, parse_comma_separated_list

# A logger for this file
log = logging.getLogger(__name__)


@hydra.main(
    version_base=None, config_path="hydra_config/train", config_name="config"
)
def my_app(cfg):
    cfg = {key: cfg[key] for key in cfg.keys()}
    log.info("Info level message")
    log.debug("Debug level message")

    cfg["metrics"] = parse_comma_separated_list(cfg["metrics"])

    if cfg["outdir"] is None:
        hydra_config = HydraConfig.get()
        cfg["outdir"] = hydra_config.runtime.output_dir

    main.callback(**cfg)


if __name__ == "__main__":
    my_app()
