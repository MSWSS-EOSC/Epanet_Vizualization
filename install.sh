#!/bin/bash

# git clone https://github.com/MSWSS-EOSC/Epanet_Vizualization.git

GALAXY_DIRECTORY="/home/export/galaxy-central"
MSWSS_DIRECTORY="${GALAXY_DIRECTORY}/tools_mswss"
PLUGIN_DIRECTORY="${MSWSS_DIRECTORY}/vizualization"

mkdir $PLUGIN_DIRECTORY

/home/export/galaxy_venv/bin/pip install wntr
/home/export/galaxy_venv/bin/pip install folium
/home/export/galaxy_venv/bin/pip install plotly==4.14.3
/home/export/galaxy_venv/bin/pip install --upgrade isa-rwval
/home/export/galaxy_venv/bin/pip install utm

mv -v ./source/* $PLUGIN_DIRECTORY/
chmod u=rwx,g=rwx,o=rwx -R $PLUGIN_DIRECTORY/

docker exec galaxy supervisorctl restart galaxy:
