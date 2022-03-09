import click
import bioframe as bf
from . import find_all_regions

@click.command()
@click.option('-c', '--cool_path', help='mcool path')
@click.option('-r', '--resolution', default=10000, help='resolution')
@click.option('-a','--assembly', default='hg38', help='assembly')
@click.option('-l', '--regionsize', default=1000000, help='region length')
@click.option('-m', '--merge', default=False, help='merge regions')

def cli(cool_path, assembly, resolution, regionsize, merge):
    all_regions = find_all_regions(cool_path, assembly, resolution, regionsize)
    if merge:
        regions_df = bf.from_any(all_regions)
        merged_regions_df = bf.merge(regions_df).iloc[:, :-1]
        idx = bf.arrops.argnatsort(merged_regions_df['chrom'])
        merged_regions_df = merged_regions_df.iloc[idx].reset_index(drop=True)
        all_regions = list(merged_regions_df.chrom +':'+merged_regions_df.start.astype(str) + '-' + merged_regions_df.end.astype(str))

    all_regions_str = '\n'.join(all_regions)

    click.echo(all_regions_str)

if __name__ == '__main__':
    cli()