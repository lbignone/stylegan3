import logging
import hydra
from hydra.core.hydra_config import HydraConfig

from gen_images import generate_images
from gen_images import parse_range, parse_vec2

# A logger for this file
log = logging.getLogger(__name__)


@hydra.main(
    version_base=None, config_path="hydra_config", config_name="config"
)
def my_app(cfg):
    log.info("Info level message")
    log.debug("Debug level message")
    cfg.gen_images["seeds"] = parse_range(cfg.gen_images["seeds"])
    cfg.gen_images["translate"] = parse_vec2(cfg.gen_images["translate"])

    if cfg.gen_images["outdir"] is None:
        hydra_config = HydraConfig.get()
        cfg.gen_images["outdir"] = hydra_config.runtime.output_dir

    generate_images.callback(**cfg.gen_images)


if __name__ == "__main__":
    my_app()
