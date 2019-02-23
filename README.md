# Dockerized PySpark Jupyter Notebook and Cluster


### Description:
This project provides a dockerized pyspark environment for both running Jupyter notebooks and for submitting scripts to a local cluster.


### Jupyter Notebook Usage:
* Start a jupyter server which runs on a workerless pyspark cluster: ` make upn `
* Useful for quick testing, particularly in conjunction with pyspark sql
* The spark session is initialized on startup and can be accessed by **spark**


### Local Cluster Usage:
* Start a local pyspark cluster: ` make upc `
* Useful for testing python scripts before deployment on a production cluster
