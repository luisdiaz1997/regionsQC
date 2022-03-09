import bioframe as bf
import cooler

def get_bins(assembly, resolution):
    chromsizes  = bf.fetch_chromsizes(assembly)[:22] #pick first 22 chromosomes only
    bins = bf.binnify(chromsizes, resolution)
    return bins

def hic_criteria(region, bins):
    weights = bf.select(bins, region)['weight']
    return not(sum(weights.isna())>0)


def find_nonnan(region, bins, resolution, criteria):
    chrom, start, end = bf.parse_region(region)
    
    if (end-start)< (4*resolution):
        if criteria(region, bins):
            return start
        else:
            return end
    
    middle = (start+end)//2
    region_right = bf.to_ucsc_string((chrom, middle, end))
    region_left = bf.to_ucsc_string((chrom, start, middle))
    
    if criteria(region_right, bins):
        return find_nonnan(region_left, bins, resolution, criteria)
    else:
        return find_nonnan(region_right, bins, resolution,  criteria)
    



def find_regions(chrom, chromsize, resolution, regionsize, bins, criteria):
    regions = []
    i = 0
    while i < (chromsize-regionsize):
        region = bf.to_ucsc_string((chrom, i, i+regionsize))
        if criteria(region, bins):
            regions.append(region)
            i+= regionsize
        else:
            i = find_nonnan(region, bins, resolution, criteria)
    
    return regions



def find_all_regions(cool_path, assembly, resolution, regionsize):
    chromsizes  = bf.fetch_chromsizes(assembly)[:22] #pick first 22 chromosomes only
    c = cooler.Cooler(cool_path+'::resolutions/'+str(resolution))
    all_regions = []
    for chrom, chromsize in zip(chromsizes.index, chromsizes):
        regions = find_regions(chrom, chromsize, resolution, regionsize, c.bins()[:], hic_criteria)
        all_regions += regions

    return all_regions


