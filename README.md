# Distance-over-sphere
When traveling great distances, the curvature of the earth has to considered when calculating the distance. This python script calculates the distance between two geo-coordinates of format signed decimal degrees (lat,lon), eg. (40.6386, -73.9464).

### Prerequisites
python 3

## script explained

* see the *distance over sphere.py*  file for comments
* There may be rounding errors for coordinates really close to eachother due to the *floating-point-precision* of computer systems. For *64-bit floating-point numbers*, there should not be any serius rounding errors for distances over a few meters. But if the two coordinates equals to eachother the rounding error is significant, therefore the script contains a "quick fix" to handle it. 

## Authors
* **David Mårsäter** - *Initial work* 

See also the list of [contributors](https://github.com//DavidMarsater/distance-over-sphere/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
