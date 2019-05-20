# Dockerized PySpark Jupyter Notebook and Cluster

### Description:
This project provides a dockerized pyspark environment for both running Jupyter notebooks and for submitting scripts to a local cluster.

### General Usage:
* Lint the repo: ` make flake `
* Test the files in *./test/*: ` make test `
* Clean the repo of unnecessary caches: ` make clean `
* Stop the Dockerized environments: ` make down `
* Fill in *.env.template* with your aws credentials and save as *.env* in order to use aws services

### Jupyter Notebook Usage:
* Start a jupyter server which runs on a workerless pyspark cluster: ` make upn `
* Useful for quick testing, particularly in conjunction with pyspark sql
* The spark session is initialized on startup and can be accessed by **spark**

### Local Cluster Usage:
* Start a local pyspark cluster: ` make upc `
* Useful for testing python scripts before deployment on a production cluster
