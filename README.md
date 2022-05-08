# regionsQC
This package outputs quality genomic regions from a given ChIP-seq or Hi-C map

# Example
```
regionsQC -c <mcool_path> -r 10000 -l 1000000 > data/regions_example.tsv
```

# Options
```
Options:
  -c, --cool_path TEXT      mcool path
  -r, --resolution INTEGER  resolution
  -a, --assembly TEXT       assembly
  -l, --regionsize INTEGER  region length
  -m, --merge BOOLEAN	    merge connected regions
  
```
# Todo

Flexible quality metrics
