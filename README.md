# rtlsdr_analyzer

A spectrum analyzer program I made as part of my thesis. It uses cheap USB dongles intended as DVB-T receivers as front-end hardware. The dongles are based on the RTL2832U demodulator chip, which thanks to unofficial drivers can stream raw samples.

The interface is meant to resemble working with real swept spectrum analyzers as much as possible. It features standard controls and functions such as markers, averaging and saving traces.

## Getting Started

### Prerequisites

### Installing

## Usage

## Built With

* [librtlsdr](https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr) - Unofficial driver for RTL2832U based devices
* [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) -Python wrapper for Qt5 framework
* [pyqtgraph](http://www.pyqtgraph.org/) - PyQt-based graphics framework used for plotting
* [pyrtlsdr](https://github.com/roger-/pyrtlsdr) - Python wrapper for interfacing with rtlsdr devices
* [numpy](http://www.numpy.org/) - Used for efficient computations on arrays
* [matplotlib](https://matplotlib.org/) - Used for window functions