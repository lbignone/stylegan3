
# Start cluster
ray up -y ray_g4dn.xlarge_config.yaml

# install hydra
ray exec ray_g4dn.xlarge_config.yaml "pip install hydra-core==1.2"

# Download dataset
ray exec ray_g4dn.xlarge_config.yaml "aws s3 cp s3://innova-conicet-imaging-datasets/galaxies/eagle_galrand_64x64.zip datasets/."

# launch hydra with training job
ray exec --screen ray_g4dn.xlarge_config.yaml "python hydra_train.py cfg=stylegan3-r data='datasets/eagle_galrand_64x64.zip' gpus=1 batch=32 gamma=0.5 batch_gpu=16"

