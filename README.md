### OpenTopMap Crawler

Simple tool to download a rectangular map from https://opentopomap.org/

#### Usage
```
Usage: getotm.py [OPTIONS] [OUTPUT]

  Simple tool to download a rectangular map from https://opentopomap.org/.

Options:
  --lon1 FLOAT        longitude of a corner
  --lon2 FLOAT        longitude of opposite corner
  --lat1 FLOAT        latitude of a corner
  --lat2 FLOAT        latitude of oppostite corner
  --zoom INTEGER      map zoom level
  --working_dir PATH  working directory of the script
  --help              Show this message and exit.

```

#### Prerequisites
* Python 3.6
* Install requirements.txt
* ImageMagick (tested with ImageMagick 7.0.7-38)

