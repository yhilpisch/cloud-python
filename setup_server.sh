#!/bin/bash
#
# Setting up a DigitalOcean Droplet
# with Basic Scientific Python stack
# and Jupyter Notebook
#
# (c) Dr Yves J Hilpisch
# The Python Quants GmbH
#

MASTER_IP=$1

IDENTITY=~/.ssh/digital_ocean  # change to your identity file

scp python-setup.sh root@${MASTER_IP}:
scp *.ipynb root@${MASTER_IP}:
scp *.zip root@${MASTER_IP}:
ssh root@${MASTER_IP} bash /root/python-setup.sh
