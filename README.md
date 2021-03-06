# rtlsdr_analyzer

A spectrum analyzer program I made as part of my thesis. It uses cheap USB dongles intended as DVB-T receivers as front-end hardware. The dongles are based on the RTL2832U demodulator chip, which thanks to unofficial drivers can stream raw samples.

The interface is meant to resemble working with real swept spectrum analyzers as much as possible. It features standard controls and functions such as markers, averaging and saving traces.

## Getting Started

The GUI is written using the Qt framework, so theoretically it should work on both Windows and Linux, but I personally only tested in on Fedora 29. Of course good signal reception requires a proper analog front-end (antenna, LNA, etc.), but it's outside the scope of this project.

### Prerequisites

For the program to do anything useful you need to have a compatible USB dongle. To work with the dongle you have to install the unofficial driver. See https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr for instructions for your OS. The code was tested on Python 3.7, but should work on anything 3.4+.

### Installing

The program itself is just a Python script so it requires no installation. Just clone the repo wherever you want and install the dependencies.

First clone the repository and go into the project folder:

```bash
git clone https://github.com/wojcik91/rtlsdr_analyzer.git
cd rtlsdr_analyzer/
```

Next create a virtual environment and activate it:

```bash
python3 -m venv env
source env/bin/activate
```

Then install required Python libraries:

```bash
pip install -r requirements.txt
```

## Usage

To start the program go into the project folder and simply 
type:

```bash
python main.py
```

To start the analyzer insert the dongle into a USB port and press the START button.

## Built With

* [librtlsdr](https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr) - Unofficial driver for RTL2832U based devices
* [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) -Python wrapper for Qt5 framework
* [pyqtgraph](http://www.pyqtgraph.org/) - PyQt-based graphics framework used for plotting
* [pyrtlsdr](https://github.com/roger-/pyrtlsdr) - Python wrapper for interfacing with rtlsdr devices
* [numpy](http://www.numpy.org/) - Used for efficient computations on arrays
* [matplotlib](https://matplotlib.org/) - Used for window functions