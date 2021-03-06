[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
![Tests](https://github.com/jfuruness/lib_bgp_simulator/actions/workflows/tests.yml/badge.svg)

# lib\_bgp\_simulator
This package simulates BGP, ROV, BGP propagation, various attack/defend scenarios, draws diagrams of the internet, etc

* [Description](#package-description)
* [Usage](#usage)
* [Installation](#installation)
* [Testing](#testing)
* [Development/Contributing](#developmentcontributing)
* [History](#history)
* [Credits](#credits)
* [Licence](#license)
* [TODO](#todo)

## Package Description

TODO

## Usage
* [lib\_bgp\_simulator](#lib_bgp_simulator)

Note: the simulator takes about 1-2GB per core. Make sure you don't run out of RAM!

TODO

## Installation
* [lib\_bgp\_simulator](#lib_bgp_simulator)

Install python and pip if you have not already. Then run:

```bash
# Needed for graphviz and Pillow
sudo apt-get install -y graphviz libjpeg-dev zlib1g-dev
pip3 install pip --upgrade
pip3 install wheel
```

For production:

```bash
pip3 install git@github.com:jfuruness/lib_bgp_simulator.git
```

This will install the package and all of it's python dependencies.

If you want to install the project for development:
```bash
git clone https://github.com/jfuruness/lib_bgp_simulator.git
cd lib_bgp_simulator
pip3 install -e .[test]
```

To test the development package: [Testing](#testing)


## Testing
* [lib\_bgp\_simulator](#lib_bgp_simulator)

To test the package after installation:

```
cd lib_bgp_simulator
pytest lib_bgp_simulator
flake8 lib_bgp_simulator
mypy lib_bgp_simulator
```

If you want to run it across multiple environments, and have python 3.9 installed:

```
cd lib_bgp_simulator
tox
```


## Development/Contributing
* [lib\_bgp\_simulator](#lib_bgp_simulator)

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Add an engine test if you've made a change in the simulation_engine, or a system/unit test if the simulation_framework was modified
5. Run tox (for faster iterations: flake8, mypy, and pytest can be helpful)
6. Commit your changes: `git commit -am 'Add some feature'`
7. Push to the branch: `git push origin my-new-feature`
8. Ensure github actions are passing tests
9. Email me at jfuruness@gmail.com

## History
* [lib\_bgp\_simulator](#lib_bgp_simulator)

* 0.0.4 Major refactor
* 0.0.2 Fixed dependencies so that they weren't relying off ssh, since github doesn't support pip installs with ssh and github actions failed
* 0.0.1 Refactored package. Semi working version

## Credits
* [lib\_bgp\_simulator](#lib_bgp_simulator)

Thanks to Cameron Morris for helping with extending the BGP policy to include withdrawals, RIBsIn, RIBsOut

Thanks to Cameron and Reynaldo for helping out with the refactor

Thanks to Reynaldo for helping out with lots of type hinting

Thanks to Dr. Herzberg and Dr. Wang for employing me and allowing this project to be open source

## License
* [lib\_bgp\_simulator](#lib_bgp_simulator)

BSD License (see license file)

## TODO
* [lib\_bgp\_simulator](#lib_bgp_simulator)

See Jira
