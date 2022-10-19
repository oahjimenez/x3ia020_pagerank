#!/bin/bash

## En local ->
## pig -x local -
## pig -embedded jython dataproc.py

## copy data
gsutil cp small_page_links.nt gs://pagerank/

## copy PySpark code
gsutil cp dataproc.py gs://pagerank/

## Clean out directory
gsutil rm -rf gs://pagerank/out

## create the cluster 2 workers
gcloud dataproc clusters create cluster-a35a --enable-component-gateway --region europe-west1 --zone europe-west1-c --master-machine-type n1-standard-4 --master-boot-disk-size 500 --num-workers 2 --worker-machine-type n1-standard-4 --worker-boot-disk-size 500 --image-version 2.0-debian10 --project master-2-large-scale-data

## run
## (suppose that out directory is empty !!)
gcloud dataproc jobs submit pig --region europe-west1 --cluster cluster-a35a -f gs://pagerank/dataproc.py

## access results
gsutil cat gs://pagerank/out*

## delete cluster...
gcloud dataproc clusters delete cluster-a35a --region europe-west1
