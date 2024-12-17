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

