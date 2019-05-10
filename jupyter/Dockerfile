FROM jupyter/minimal-notebook:2662627f26e0
#FROM jupyter/scipy-notebook:2662627f26e0


USER root

ARG JUPYTERHUB_VERSION=1.0.0
RUN pip install --no-cache \
    jupyterhub==$JUPYTERHUB_VERSION

RUN apt-get update && \
    apt-get install -y g++ gcc vim nano && \
    apt-get clean

RUN apt-get -y update

RUN echo "tini 0.18.0" > /opt/conda/conda-meta/pinned 

# install cyclus deps
RUN conda install -y openssh gxx_linux-64 gcc_linux-64 cmake make docker-pycreds git xo python-json-logger \
	                     python=3.6 glibmm glib=2.56 libxml2 libxmlpp libblas \
	                     libcblas liblapack pkg-config coincbc=2.9 boost-cpp hdf5 \
	                     sqlite pcre gettext bzip2 xz setuptools nose pytables \
	                     pandas jinja2 cython websockets pprintpp &&\
    conda clean -y --all

# CYCLUS
RUN mkdir -p $HOME/cyclus&&\
    cd $HOME/cyclus &&\
    git clone https://github.com/bam241/cyclus &&\
    cd $HOME/cyclus/cyclus &&\
    git fetch --all &&\
    git checkout fix_conda &&\
    python3 install.py --clean-build -j2 --prefix=/usr/local

# CYCAMORE
run cd $HOME/cyclus &&\
    git clone https://github.com/cyclus/cycamore &&\
    cd $HOME/cyclus/cycamore &&\
    python3 install.py --clean-build -j2 --prefix=/usr/local

# CYMETRIC
run cd $HOME/cyclus &&\
    git clone https://github.com/cyclus/cymetric &&\
    cd $HOME/cyclus/cymetric &&\
    python3 setup.py install --prefix=/usr/local

ENV PYTHONPATH=/usr/local/lib/python3.6/site-packages:$PYTHONPATH
#ENV LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:$HOME/.local/lib/"

USER $NB_UID

CMD ["jupyterhub-singleuser"]