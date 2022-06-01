import logging
import hydra
from hydra.core.hydra_config import HydraConfig

from gen_images import generate_images
from gen_images import parse_range, parse_vec2

# A logger for this file
log = logging.getLogger(__name__)


@hydra.main(
    version_base=None, config_path="hydra_config/gen_images", config_name="config"
)
def my_app(cfg):
    log.info("Info level message")
    log.debug("Debug level message")
    cfg["seeds"] = parse_range(cfg["seeds"])
    cfg["translate"] = parse_vec2(cfg["translate"])

    if cfg["outdir"] is None:
        hydra_config = HydraConfig.get()
        cfg["outdir"] = hydra_config.runtime.output_dir

    generate_images.callback(**cfg)


if __name__ == "__main__":
    my_app()
