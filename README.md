# Knowledge Graph Exchange

[![Build Status](https://travis-ci.org/NCATS-Tangerine/kgx.svg?branch=master)](https://travis-ci.org/NCATS-Tangerine/kgx)
[![Documentation Status](https://readthedocs.org/projects/kgx/badge/?version=latest)](https://kgx.readthedocs.io/en/latest/?badge=latest)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)]()

KGX (Knowledge Graph Exchange) is a Python library and set of command line utilities for exchanging Knowledge Graphs (KGs) that conform to or are aligned to the [Biolink Model](https://biolink.github.io/biolink-model/).

The core datamodel is a [Property Graph](https://neo4j.com/developer/graph-database/) (PG), represented internally in Python using a [networkx MultiDiGraph model](https://networkx.github.io/documentation/stable/reference/classes/generated/networkx.MultiDiGraph.edges.html).

KGX allows conversion to and from:

 * RDF serializations (read/write) and SPARQL endpoints (read)
 * Neo4J endpoints (read) or Neo4J dumps (write)
 * CSV/TSV and JSON (see [associated data formats](./data-preparation.md) and [example script to load CSV/TSV to Neo4j](./examples/scripts/load_csv_to_neo4j.py))
 * Any format supported by networkx


KGX will also provide validation, to ensure the KGs are conformant to the Biolink model: making sure nodes are categorized using Biolink classes, edges are labeled using valid Biolink relationship types, and valid properties are used.


## Internal Representation

Internal representation is networkx MultiDiGraph which is a property graph.

The structure of this graph is expected to conform to the Biolink Model standard, briefly summarized here:

 * [Nodes](https://biolink.github.io/biolink-model/docs/NamedThing.html)
    * id : required
    * name : string
    * category : string. broad high level type. Corresponds to label in neo4j
    * extensible other properties,  depending on the node
 * [Edges](https://biolink.github.io/biolink-model/docs/Association.html)
    * subject : required
    * edge_label : required
    * object : required
    * extensible other properties, depending on the edge


## Installation

### Python 3.7 Version and Core Tool Dependencies

> **Note:** the installation of KGX requires Python 3.7+

You should first confirm what version of Python 
you have running and upgrade to v3.7 as necessary, following best practices in your operating system. 
It is also assumed that the common development tools are installed including git, pip, and all necessary development libraries for your operating system.


### Getting the Project Code

Go to where you wish to host your local project repository and git clone the project, namely:

```bash
cd /path/to/your/local/git/project/folder
git clone https://github.com/NCATS-Tangerine/kgx.git

# then  enter  into the cloned project repository
cd kgx
```

### Configuring a Safe Virtual Environment for KGX

For convenience, make use of the Python `venv` module to create a lightweight virtual environment. 

> Note that you may also have to install the appropriate `venv` package for Python 3.7. 
> 
> For example, under Ubuntu Linux, you might 
> 
> ```bash
> sudo apt-get install python3.7-venv  
> ```


Once `venv` is available, type:

```bash
python3 -m venv venv
source venv/bin/activate
```

To exit the environment, type:

```
deactivate
```

To reenter, source the `activate` command again.

Alternately, you can also use use **conda env** to manage packages and the development environment:

```bash
conda create -n translator-modules python=3.7
conda activate translator-modules
```

Some IDE's (e.g. PyCharm) may also have provisions for directly creating a virtual environment. This should work fine.


### Installing Python Dependencies 

The Python dependencies of the application need to be installed into the local environment using a version of `pip` matched to your Python 3.7 installation (assumed here to be called `pip3`). 

Again, follow the specific directives of your operating system for the installation.

For example, under Ubuntu Linux, to install the Python 3.7 matched version of pip, type the following:

```bash
sudo apt-get install python3-pip
```

which will install the `pip3` command.  

At this point, it is advisable to separately install the `wheel` package dependency before proceeding further 
(Note: it is  assumed here that your `venv` is activated)


```bash
pip3 install wheel
```
 
After installation of the `wheel` package, we install the remaining KGX Python package dependencies without error:

```bash
pip3 install .
```

It is *sometimes* better to use the 'python -m pip' version of pip rather than just 'pip'
to ensure that the proper version of pip - i.e. for the python3 in your virtual environment - is used 
(i.e. once again, better check your pip version.  On some systems, it may run the operating system's version, 
which may not be compatible with your `venv` installed Python 3.7)

```bash
python -m pip install .
```

## Docker Dependencies

Some components of KGX leverage the use of Docker. If not installed in your Operating system environment, the following
[instructions to install Docker](DOCKER_README.md) may be followed to install it.

