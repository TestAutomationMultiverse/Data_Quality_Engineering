docker compose up -d --build

``` mermaid
flowchart TD
    subgraph FlaskApp[Flask Application]
        A[Migration Logic]
        A --> |"/migrate-users"| MigrateUsersEndpoint[/migrate-users/]
        A --> |"/migrate-orders"| MigrateOrdersEndpoint[/migrate-orders/]
        A --> |"/migrate-cleaned-data"| MigrateCleanedDataEndpoint[/migrate-cleaned-data/]
    end

    subgraph SourceDB[Source Database]
        direction TB
        SourceTable1[Source Table: source_table</br>Fields:</br>- id</br>- name</br>- age</br>- city</br>- created_at]
        SourceTable2[Source Table: source_orders</br>Fields:</br>- order_id</br>- user_id </br>- order_total</br>- order_date]
        SourceTable3[Source Table: source_unnormalized</br>Fields:</br>- record_id</br>- full_name</br>- age </br>- location]
    end

    subgraph TargetDB[Target Database]
        direction TB
        TargetTable1[Target Table: target_users</br>Fields:</br>- user_id</br>- full_name</br>- age_group</br>- city</br>- registered_date]
        TargetTable2[Target Table: target_orders</br>Fields:</br>- order_id</br>- user_id </br>- order_total</br>- order_date]
        TargetTable3[Target Table: target_cleaned_data</br>Fields:</br>- record_id</br>- name</br>- age</br>- city]
    end

    FlaskApp --> |"Reads/Writes Data"| SourceDB
    FlaskApp --> |"Writes Transformed Data"| TargetDB

    SourceTable1 --> |"Schema Transformation"| TargetTable1
    SourceTable2 --> |"Data Transformation"| TargetTable2
    SourceTable3 --> |"Data Cleaning"| TargetTable3

```



| **Step/Phase** | **Topic/Skill** | **Description** | **Course/Example Tools** | **Duration** |
| --- | --- | --- | --- | --- |
| **1\. Basics** | Python Programming | Learn the basics of Python for data manipulation and scripting. | Python resources | 1-3 Months |
|  | Computing Fundamentals | Develop foundational knowledge of computing concepts. | General courses | 1-3 Months |
|  | SQL (Structured Query Language) | Learn SQL for data querying and manipulation in databases. | SQL resources | 1-3 Months |
|  | Introduction to Data Warehousing | Understand the fundamentals of data warehousing and its use cases. | Introductory courses | 1 Week |
|  | Data Warehouse Architecture | Learn about star schema and other components of a data warehouse. | DW resources | 1 Week |
|  | ETL Process Basics | Understand ETL (Extract, Transform, Load) and its role in data pipelines. | ETL resources | 1 Week |
|  | Introduction to Data Testing | Learn why data testing is crucial in pipelines and applications. | Testing basics | 1 Week |
|  | Types of Data Testing | Understand schema validation, data integrity, completeness, and performance testing. | Overview resources | 1 Week |
| **2\. Tools** | Relational Databases | Learn MySQL, PostgreSQL, or similar tools for data storage and retrieval. | MySQL, PostgreSQL | 1-2 Months |
|  | NoSQL Databases | Learn MongoDB, Cassandra, or other NoSQL systems for unstructured data. | MongoDB, Cassandra | 1-2 Months |
|  | ETL Tools Overview | Familiarize with ETL tools like Talend, Informatica, or Apache NiFi. | Tool-specific courses | 2 Weeks |
|  | Data Warehousing Tools | Explore tools like Snowflake, Amazon Redshift, and Google BigQuery. | Tool-specific courses | 2 Weeks |
|  | Data Testing Tools Overview | Learn about tools like Great Expectations, dbt test, and Apache Griffin for validation. | Tool-specific courses | 2 Weeks |
|  | SQL-Based Testing | Use SQL queries for validating data integrity and relationships. | SQL tutorials | 1 Week |
| **3\. Design** | Data Modeling | Learn about fact tables, dimension tables, and schema design concepts. | Data modeling resources | 2 Weeks |
|  | Designing ETL Pipelines | Understand best practices for scalable and efficient ETL pipeline design. | Pipeline design courses | 2 Weeks |
|  | Schema Validation | Learn to validate schemas, constraints, and relationships in data. | Validation techniques | 1 Week |
|  | Data Consistency and Integrity | Techniques to ensure consistent and reliable data across systems. | Data governance resources | 1 Week |
| **4\. Advanced** | Batch and Streaming Processing | Learn techniques for batch and real-time data processing. | Apache Kafka, Spark Streaming | 2-3 Months |
|  | Cloud Platforms | Explore AWS, Google Cloud, or Azure for deploying ETL pipelines. | Cloud-specific courses | 1-2 Months |
|  | Incremental Data Loading | Strategies for loading only new or updated data in pipelines. | Data pipeline resources | 1 Week |
|  | Performance Testing | Test the scalability and efficiency of ETL pipelines. | Testing frameworks | 1 Week |
|  | Data Quality and Governance | Ensure data compliance and quality in ETL processes. | Governance resources | 2 Weeks |
|  | Performance Tuning | Optimize ETL and data warehouse performance for better efficiency. | Tuning techniques | 1 Week |
|  | Data Validation in ETL | Implement robust data validation strategies in ETL workflows. | Validation frameworks | 1 Week |
| **5\. Practice** | Beginner Projects | Start with small-scale projects to implement basic pipelines. | Projects on GitHub | 1-2 Months |
|  | Intermediate Projects | Build moderately complex pipelines integrating various tools and techniques. | Portfolio projects | 2-4 Months |
|  | Advanced Projects | Work on end-to-end testing of complex systems for real-world scenarios. | Industry-level projects | 4+ Months |
|  | Mock Testing Projects | Simulate testing scenarios across domains like healthcare or finance. | Domain-specific projects | 2 Weeks |
|  | End-to-End Testing | Test entire data pipelines from source to analytics. | Testing frameworks | 1 Week |

