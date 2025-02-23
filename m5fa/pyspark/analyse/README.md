## Analyse data using pyspark
### Docker
```
docker build -t myspark37 .
```
Add the second mount if original is a link
ben
```
docker run -it \
    -e DATADIR=/opt/data \
    -v /home/wwagner4/prj/kaggle/m5fa/pyspark/analyse:/opt/project \
    -v /data/kaggle:/opt/data \
    -p 4040:4040 \
    myspark37 bash


    docker run \
    --rm \
    --name sp \
    -e DATADIR=/opt/data \
    -v /home/wwagner4/prj/kaggle/m5fa/pyspark/analyse:/opt/project \
    -v /data/kaggle:/opt/data \
    -p 4040:4040 \
    myspark37 /opt/spark/bin/spark-submit --executor-memory 25G --driver-memory 25g --driver-java-options -Duser.timezone=CET \
        /opt/project/analyse.py &
```
bob
```
docker run -it \
    -e DATADIR=/opt/data \
    -v /home/wwagner4/prj/kaggle/m5fa/pyspark/analyse:/opt/project \
    -v /home/wwagner4/work/kaggle:/opt/data \
    -p 4040:4040 \
    myspark37 bash

docker run \
    -e DATADIR=/opt/data \
    -v /home/wwagner4/prj/kaggle/m5fa/pyspark/analyse:/opt/project \
    -v /home/wwagner4/work/kaggle:/opt/data \
    -p 4040:4040 \
    myspark37 /opt/spark/bin/spark-submit --executor-memory 6G --driver-memory 6g --driver-java-options -Duser.timezone=CET \
        /opt/project/analyse.py &
```
wallace
```
docker run -it \
    -e DATADIR=/opt/data \
    -v /Users/wwagner4/prj/kaggle/m5fa/pyspark/analyse:/opt/project \
    -v /Users/wwagner4/work/kaggle:/opt/data \
    -p 4040:4040 \
    myspark37 bash
```
work
```
docker run -it \
    -e DATADIR=/opt/data \
    -v /opt/wwa/prj/kaggle/m5fa/pyspark/analyse:/opt/project \
    -v /opt/wwa/work/kaggle:/opt/data \
    -p 4040:4040 \
    myspark37 bash
```

### Data
Copy the original data from kaggle into data/original. They are too big for git.
```
kaggle: https://www.kaggle.com/c/m5-forecasting-accuracy/data
drive: https://drive.google.com/drive/folders/1koGlsp1fcV0JsPvIUtrFS1E-UhMHV2aa
```
### Options
For changing the timezone call spark-submit with the following option
````
--driver-java-options -Duser.timezone=CET
````
For changing memeory management
```
--executor-memory 25G 
--driver-memory 25g
```
Example call
```$bash
sps --executor-memory 25G --driver-memory 25g --driver-java-options -Duser.timezone=CET analyse.py 
```
```$bash
sps --executor-memory 10G --driver-memory 10g --driver-java-options -Duser.timezone=CET analyse.py 
```

pipenv
```
docker build -t pipenv -f DockerfilePipenv .

docker run --user 501:20 -e HOME=/opt/project -it -v /Users/wwagner4/prj/kaggle/m5fa/pyspark/analyse:/opt/project pipenv bash

docker run --user 499807169:499800513 -e HOME=/opt/project -it -v /Users/wwagner4/prj/kaggle/m5fa/pyspark/analyse:/opt/project pipenv bash
```
