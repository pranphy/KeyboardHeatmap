# Keyboard Heatmap

This project helps to create heatmap of keys in keyboard for some given text. Supports Nepali `नेपाली` keyboard layout, the popular `बकमान`(bakamana) for now and the usual `qwerty` layout. Other layouts will be added in due course.

# Installation
Clone the repository and run setup.
```
git clone https://github.com/pranphy/KeyboardHeatmap
cd KeyboardHeatmap
python3 setup.py install
```
You will find an executable `kbhmap` in your path. 
# Usage

`kbhmap --help` shows the following


```
Usage: kbhmap [OPTIONS]

  a tool to generate the keyboard heatmap. It reads the text from  the input
  file and generates the heatmap. The heatmap can be configured.  The output
  heatmap image is saved in a file with name passed  as the `output`
  parameter. The smoothness of the heatmap can be controlld with `-s
  --sigma` option. The resolution of th output image can be set with `-d
  --dpi` parameter.

Options:
  -i, --input TEXT                input file name
  -o, --output TEXT               output file name
  -l, --layout [qwerty|bakamana]  keyboard layout to use
  -s, --sigma FLOAT               sigma value to smoothen heatmap
  -c, --cmap TEXT                 colormap to use
  -d, --dpi INTEGER               dpi of resulting image
  --help                          Show this message and exit.
```

# Example
For example if you want to see the heatmap of keys in a file named `test.txt` and
output the heatmap image as `heatmap_test.png` you will do the following
```
kbhmap -i test.txt -o heatmap_test.png
```

You can configure other options. Cmap takes any valid matplotlib
color map. passing `--dpi=100` sets the dpi of output image to 100. 
The smoothing `--sigma` parameter is to smooth out the heatmap. Since
the keys have precise location they will have high density at the key
location and sharp fall at th key edge. If sigma is supplied it 
applies gaussian smoothing to the heatmap to make it smoother and nicer.


See [notebook](http://github.com/pranphy/keyboardheatmap/test/MakeHeatmap.ipynb) for usage as a library.

# Outputs
Example heatmap for QWERTY
![An example heatmap](http://github.com/pranphy/keyboardheatmap/keyhmap/images/example_qwerty.png)


Example heatmap for बकमान 
![An example heatmap](http://github.com/pranphy/keyboardheatmap/keyhmap/images/example_bakamana.png)
