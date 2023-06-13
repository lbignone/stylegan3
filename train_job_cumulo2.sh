
CONFIG=ray_p3.8xlarge_config_06.yaml
DATASET=cumulo2.zip

# Start cluster
ray up -y ${CONFIG}

# Download dataset
ray exec ${CONFIG} "aws s3 cp s3://innova-conicet-imaging-datasets/cumulo/${DATASET} datasets/."

# launch hydra with training job
ray exec --screen ${CONFIG} "python hydra_train.py cfg=stylegan2 data='datasets/${DATASET}' gpus=4 batch=32 gamma=0.5 mirror=True aug=noaug dataset_class=hdf5"

# wait for output folder structure creation
sleep 60

# start syncing output
ray exec --screen ${CONFIG} "python watch_and_sync_to_s3.py outputs s3://innova-conicet-output"
