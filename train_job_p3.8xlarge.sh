
CONFIG=ray_p3.8xlarge_config.yaml
DATASET=eagle_galrand_64x64.zip

# Start cluster
ray up -y ${CONFIG}

# install hydra
ray exec ${CONFIG} "pip install hydra-core==1.2"

# Download dataset
ray exec ${CONFIG} "aws s3 cp s3://innova-conicet-imaging-datasets/galaxies/${DATASET} datasets/."

# launch hydra with training job
ray exec --screen ${CONFIG} "python hydra_train.py cfg=stylegan3-r data='datasets/${DATASET}' gpus=4 batch=32 gamma=0.5 aug=noaug"

