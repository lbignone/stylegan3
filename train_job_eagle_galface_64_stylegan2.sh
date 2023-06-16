
CONFIG=ray_p3.8xlarge_config.yaml
DATASET=eagle_galface_64x64.zip

# Start cluster
ray up -y ${CONFIG}

# wait a little
sleep 60

# Download dataset
ray exec ${CONFIG} "aws s3 cp s3://innova-conicet-imaging-datasets/galaxies/${DATASET} datasets/."

# wait a little
sleep 60

# launch hydra with training job
ray exec --screen ${CONFIG} "python hydra_train.py cfg=stylegan2 data='datasets/${DATASET}' gpus=4 batch=32 gamma=0.5 aug=noaug"

# wait for output folder structure creation
sleep 60

# start syncing output
ray exec --screen ${CONFIG} "python watch_and_sync_to_s3.py outputs s3://innova-conicet-output"
