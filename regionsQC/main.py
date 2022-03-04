import click
from . import find_all_regions

@click.command()
@click.option('-c', '--cool_path', help='mcool path')
@click.option('-r', '--resolution', default=10000, help='resolution')
@click.option('-a','--assembly', default='hg38', help='assembly')
@click.option('-l', '--regionsize', default=1000000, help='region length')
def cli(cool_path, assembly, resolution, regionsize):
    all_regions = find_all_regions(cool_path, assembly, resolution, regionsize)
    click.echo(all_regions)

if __name__ == '__main__':
    cli()