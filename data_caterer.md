``` mermaid
flowchart TB
    subgraph Data Caterer
        direction TB
        Generate["Generate"] -->|Data Source A| A["Data Source A"]
        Generate -->|Data Source B| B["Data Source B"]
        A -->|Consumed by| Consume["Consume"]
        B -->|Consumed by| Consume
        Consume -->|Writes to| Write["Write"]
        Write -->|Data Source C| C["Data Source C"]
        Write -->|Data Source D| D["Data Source D"]
        C -->|Validated by| Validate["Validate"]
        D -->|Cleaned by| Validate
    end
```



1. Database: elasticsearch
2. Data Collector: logstash
3. Database: mongodb
4. Database: postgres
5. Data Catalog: amundsen
6. Data Visualisation: metabase
7. Job Orchestrator: airflow
8. Messaging: kafka
9. Notebook: jupyter
10. Query Engine: duckdb
11. Real-time OLAP: clickhouse
12. Test Data Management: data-caterer	[✅](https://blog.det.life/data-catering-how-you-could-replicate-your-production-data-flow-in-your-local-laptop-fd435b45ece7)
