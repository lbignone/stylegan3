# Start cluster
ray up -y ray_g4dn.xlarge_config.yaml

ray exec ray_g4dn.xlarge_config.yaml "pip install hydra-core==1.2"

# For some reason the sync does not work when first executing from local... Or maybe
# is just network problems

# launch hydra with gen job
ray exec ray_g4dn.xlarge_config.yaml "python hydra_gen_images.py seeds='1-100' network_pkl='https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-afhqv2-512x512.pkl'"
