
CONFIG=ray_g4dn.xlarge_config.yaml
DATASET=HSC_redshift_intermediate_rescaled.zip

# Start cluster
ray up -y ${CONFIG}

# Download dataset
ray exec ${CONFIG} "aws s3 cp s3://innova-conicet-imaging-datasets/galaxies/${DATASET} datasets/."

# launch hydra with training job
ray exec --screen ${CONFIG} "python hydra_train.py cfg=stylegan3-r data='datasets/${DATASET}' gpus=1 batch=32 gamma=0.5 aug=noaug dataset_class=fits"

# start syncing output
ray exec --screen ${CONFIG} "python watch_and_sync_to_s3.py outputs s3://innova-conicet-output"
