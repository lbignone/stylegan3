import os
import pickle

import click
import torch


@click.command()
@click.option('--network', 'network_pkl', help='Network pickle filename', required=True)
@click.option('--outdir', help='Where to save the output .pt file', type=str,
              required=True, metavar='DIR')
def export(
        network_pkl: str,
        outdir: str,
):
    """Export the G_ema generator to `.pt` format"""

    with open(network_pkl, "rb") as f:
        decoder = pickle.load(f)['G_ema'].cuda()
    state_dict = decoder.state_dict()

    os.makedirs(outdir, exist_ok=True)
    filename = os.path.splitext(os.path.basename(network_pkl))[0]
    torch.save(state_dict, f'{outdir}/{filename}.pt')


if __name__ == "__main__":
    export()  # pylint: disable=no-value-for-parameter
