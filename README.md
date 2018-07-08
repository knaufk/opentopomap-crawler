### OpenTopMap Crawler

Simple tool to download a rectangular map from https://opentopomap.org/

#### Usage
```
Usage: getotm.py [OPTIONS] [OUTPUT]

  Simple tool to download a rectangular map from https://opentopomap.org/.

Options:
  --lon1 FLOAT        longitude of a corner. default: 7.06451  [default:
                      7.06451]
  --lon2 FLOAT        longitude of opposite corner.  [default: 6.83993]
  --lat1 FLOAT        latitude of a corner.  [default: 50.9821]
  --lat2 FLOAT        latitude of oppostite corner.  [default: 50.90433]
  --zoom INTEGER      map zoom level.  [default: 14]
  --working_dir PATH  working directory of the script.  [default: ./tmp]
  --help              Show this message and exit.
```

#### Prerequisites
* Python 3.6
* Install requirements.txt
* ImageMagick (tested with ImageMagick 7.0.7-38)

