# Big Data Cluster Docker

## Software

* [Apache Hadoop](https://hadoop.apache.org/):
  * For distributed processing of large data sets 
  * urls:
    * ResourceManager cluster: http://localhost:8088/cluster
    * NameNode health: http://localhost:9870/dfshealth.html#tab-overview
    * Datanode1:        http://localhost:9864
    * Datanode2:        http://localhost:9865
    * HistoryServer:    http://localhost:19888
    * NodeManager1:     http://localhost:8042
    * NodeManager2:     http://localhost:8043

* [Apache Hive](http://hive.apache.org/):
  *  For 
* [Apache Spark](https://spark.apache.org/):
  * For batch processing 
  * urls:
    * master:           http://localhost:8080
    * spark worker1:          http://localhost:8081
    * worker2:          http://localhost:8082
    * history:          http://localhost:18080

* [Apache Kafka](https://kafka.apache.org/):
  * For message queue
* [Apache Airflow](https://airflow.apache.org/): 
  * For orchestration
* [Apache Flink](https://flink.apache.org/):
  * For stream processing

* [Apache Nifi](https://nifi.apache.org/):
  * For stream processing
  * url: https://localhost:8443/nifi/#/login

* [Apache Griffin](https://griffin.apache.org/):
  * For Big data Quality
  * url: http://localhost:38080/#/health


- Jupyter Notebook: http://localhost:8888





## Architecture

``` mermaid
@startuml
skinparam componentStyle rectangle

package "Network: sparknet" {
    component Metastore {
        [metastore]
        note bottom of metastore
          - PostgreSQL database
          - Hostname: metastore
          - IP: 172.28.1.1
        end note
    }

    component Master {
        [master]
        note bottom of master
          - Spark Master node
          - Hostname: master
          - IP: 172.28.1.2
        end note
    }

    component Worker1 {
        [worker1]
        note bottom of worker1
          - Spark Worker node
          - Hostname: worker1
          - IP: 172.28.1.3
        end note
    }

    component Worker2 {
        [worker2]
        note bottom of worker2
          - Spark Worker node
          - Hostname: worker2
          - IP: 172.28.1.4
        end note
    }

    component History {
        [history]
        note bottom of history
          - Spark History server
          - Hostname: history
          - IP: 172.28.1.5
        end note
    }

    component Jupyter {
        [jupyter]
        note bottom of jupyter
          - Jupyter Notebook
          - Hostname: jupyter
          - IP: 172.28.1.6
        end note
    }

    component NiFi {
        [nifi]
        note bottom of nifi
          - Apache NiFi
          - Hostname: nifi
          - IP: 172.28.1.7
        end note
    }

    component Airflow {
        [airflow]
        note bottom of airflow
          - Apache Airflow
          - Hostname: airflow
          - IP: 172.28.1.8
        end note
    }
}

metastore -[hidden]-> master
master --> worker1 : Spark communication
master --> worker2 : Spark communication
worker1 --> history : Log communication
worker2 --> history : Log communication
jupyter --> master : Notebook jobs
jupyter --> worker1 : Distributed jobs
jupyter --> worker2 : Distributed jobs
airflow --> metastore : Database access
airflow --> master : Orchestrates jobs
airflow --> jupyter : Workflow integration
nifi --> master : Data flow jobs
nifi --> airflow : Orchestrates data flows
@enduml

```

## Quick Start
1. build docker images "any platform engineering project must have a build lifecycle", simple as follows:
    - Build the base image:     `docker build ./base -t hadoop-hive-spark-base`
    - Build the master image:   `docker build ./master -t hadoop-hive-spark-master`
    - Build the worker image:   `docker build ./worker -t hadoop-hive-spark-worker`
    - Build the history image:  `docker build ./history -t hadoop-hive-spark-history`
    - Build the jupyter image:  `docker build ./jupyter -t hadoop-hive-spark-jupyter`

``` mermaid
graph TD
    A[Start] --> B[Build Base Image]
    B -->|docker build ./base -t hadoop-hive-spark-base| C[Base Image Built]
    C --> D[Build Master Image]
    D -->|docker build ./master -t hadoop-hive-spark-master| E[Master Image Built]
    C --> F[Build Worker Image]
    F -->|docker build ./worker -t hadoop-hive-spark-worker| G[Worker Image Built]
    C --> H[Build History Image]
    H -->|docker build ./history -t hadoop-hive-spark-history| I[History Image Built]
    C --> J[Build Jupyter Image]
    J -->|docker build ./jupyter -t hadoop-hive-spark-jupyter| K[Jupyter Image Built]
    E --> L[End]
    G --> L
    I --> L
    K --> L

```

2. deploy the cluster, run: docker-compose up -d



