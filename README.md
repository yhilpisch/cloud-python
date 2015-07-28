# Interactive Python in the Cloud

This repository contains a few small files that allow to easily deploy Python (cf. http://python.org) and Jupyter Notebook (cf. http://jupyter.org) in the cloud.

It all works (apart from the parallel computation example) even on the smallest **DigitalOcean droplet** (cf. https://www.digitalocean.com/?refcode=fbe512dd3dac).

When setting up such a droplet it is recommended to use the latest version of **Ubuntu**.

I assume that you have **cloned the repository** to your local machine (Linux or Mac):

```
git clone --depth=1 https://github.com/yhilpisch/cloud-python
```

## DigitalOcean Droplet

If you do not have a **DigitalOcean account** yet, generate one here

https://www.digitalocean.com/?refcode=fbe512dd3dac

You will start with 10 USD worth of compute power (= e.g. 2 monthly fees for the smallest droplet).

Now **create a droplet** giving it a name like "cloud-python" and chosing the size, location and operating system (e.g. Ubuntu 14.04).

I recommend to post a public key for easy **ssh access** (cf. the tutorial under http://hilpisch.com/rpi/00_basic_config.html).

When you have created the droplet, you are redirected to the droplet overview page which shows, among others, the **IP address of the droplet** which you should copy.

Then navigate to the **repository folder** and do:

```
cd path-to/cloud-python
bash setup_server.sh THE-IP-ADDRESS
```

The setup might take a while. The last step in the setup fires up a **Jupyter Notebook** server on the **port 8888**. You can access it in the browser under

```
THE-IP-ADDRESS:8888
```

You can now click on the example notebooks and play around.

## Flask Web app

In Jupyter Notebook open a new **terminal** and navigate to the stock_int folder:

```
cd stock_int
```

Start the **example Flask application** as follows:

```
python stock_interactive.py &
```

The app should now be reachable under

```
http://THE-IP-ADDRESS:777
```

## datapark.io

The easiest way to use Python, R, Julia, etc. in the cloud is to register under http://datapark.io.

With a single registration you have a comprehensive set of **techonlogies, libraries and tools** available to do **data science in the browser**.

## Copyright, License & Disclaimer

© Dr. Yves J. Hilpisch \| The Python Quants GmbH

The code of this repository is BSD licensed (cf. http://opensource.org/licenses/BSD-3-Clause).

The code in this repository comes with no representations or warranties, to the extent permitted by applicable law.

http://tpq.io \| team@tpq.io \|
http://twitter.com/dyjh

**datapark.io** \| http://datapark.io

**Quant Platform** \| http://quant-platform.com

**Derivatives Analytics with Python (Wiley Finance)** \|
http://derivatives-analytics-with-python.com

**Python for Finance (O'Reilly)** \|
http://python-for-finance.com

**For Python Quants Conference** \| http://fpq.io
