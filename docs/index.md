# Fundamentals of data engineering

## What is data engineering?

Data engineering is the process of designing, building, and maintaining systems within a business that enable the deriving of meaningful insights from operational data. In an era where data is frequently likened to oil or gold, data engineering emerges as the refining process that refines the raw data into a potent fuel for innovation and strategy.

Data engineering uses various tools, techniques, and best practices to achieve end goals. Data is collected from diverse sources like human-generated forms, human and system-generated content like documents, images, videos, transaction logs, IoT systems, geolocation data and tracking, application logs, and events. It results in data that fits into three broad categories.

-   Structured data organized in databases with a clear schema, often in tabular formats like SQL databases.
-   Unstructured data like images, videos, emails, and text documents that cannot fit into schemas.
-   Semi-structured data that includes both structured and unstructured elements.

Each dataset and its use case for analysis requires a different strategy. For example, some data types are processed infrequently in batches, while others are processed continuously as soon as they are generated. Sometimes, data integration is done from several sources, and all data is stored centrally for analytics. At other times, subsets of data are pulled from different sources and prepared for analytics.

``` mermaid
graph TB
    subgraph Data_Engineering["Data Engineering insights"]
        D["Wisdom"] --> D_desc["Organization Wisdom: The organization gains wisdom, leveraging insight for growth."]
        C["Insights"] --> C_desc["Data Insights: Actionable insights emerge, driving informed decision making."]
        B["Analytics"] --> B_desc["Data Analytics: Unlocks patterns, trends, and correlations."]
        A["Data"] --> A_desc["Raw Data Chaos: Unorganized data sources create a chaotic landscape."]
    end
```

## The data engineering lifecycle

The data engineering lifecycle is one of the key fundamentals of data engineering. It focuses on the stages a data engineer controls. Undercurrents are key principles or methodologies that overlap across the stages.

``` mermaid
graph TD
    A[Generation] --> B[Ingestion]
    B --> C[Transformation]
    C --> D[Serving]
    D --> E[Analytics]
    D --> F[Machine Learning]
    D --> G[Reverse ETL]
    B -->|Data flows| H[Storage]
    C -->|Data flows| H
    D -->|Data flows| H

    subgraph MainFlow
        A
        B
        C
        D
        E
        F
        G
        H
    end

    subgraph Undercurrents
        direction TB
        I[Security]
        J[Data Management]
        K[DataOps]
        L[Data Architecture]
        M[Orchestration]
        N[Software Engineering]
    end

    MainFlow --> Undercurrents
```

**Data ingestion** incorporates data from generating sources into the processing system. For instance, in the push model, data from the source system gets written to the desired destination, while in the pull model, it is the other way around. The line separating push and pull methodologies blurs as data transits through numerous stages in a pipeline. Nevertheless, mastering data ingestion is paramount to ensuring the seamless flow and preparation of data for subsequent analytical stages.

**Data transformation** refines raw data through operations that enhance its quality and utility. For example, it normalizes values to a standard scale, fills gaps where data might be missing, converts between data types, or adds even more complex operations to extract specific data features. The goal is to mold the data into a structured, standardized format primed for analytical operations.

**Data serving** makes processed and transformed data available for end-users, applications, or downstream processes. It delivers data in a structured and accessible manner, often through APIs. It ensures that data is timely, reliable, and accessible to support various analytical, reporting, and operational needs of an organization.

**Data storage** is the underlying technology that stores data through the various data engineering stages. It bridges diverse and often isolated data sources—each with its own fragmented data sets, structure, and format. Storage merges the disparate sets to offer a cohesive and consistent data view. The goal is to ensure data is reliable, available, and secure.


``` mermaid
graph TD
    A[Requirement Analysis] --> B[Data Identification]
    B --> C[Data Extraction]
    C --> D[Data Anonymization & Masking]
    D --> E[Data Transformation]
    E --> F[Data Subsetting]
    F --> G[Data Validation]
    G --> H[Data Storage & Versioning]
    H --> I[Data Provisioning]
    I --> J[Monitoring & Maintenance]
    J --> A[Feedback Loop to Requirement Analysis]
``` 


### Key considerations

#### Security

Data engineers prioritize security at every stage so that data is accessible only to authorized users. They adhere to the principle of least privilege as a best practice, so users only access what is necessary for their work and for the required duration only. Data is often encrypted as it moves through the stages and in storage.

#### Data management

Data management provides frameworks that incorporate a broader perspective of data utility across the organization. It encompasses various facets like data governance, modeling, lineage, and meeting ethical and privacy considerations. The goal is to align data engineering processes with an organization's broader legal, financial, and cultural policies.

#### DataOps

DataOps applies principles from Agile, DevOps, and statistical process control to enhance data product quality and release efficiency. It combines people, processes, and technology for improved collaboration and rapid innovation. It fosters transparency, efficiency, and cost control at every stage.

#### Data architecture

Data architecture supports an organization’s long-term business goals and strategy. This involves knowing the trade-offs and making informed choices about design patterns, technologies, and tools that balance cost and innovation.

#### Software engineering

While data engineering has become more abstract and tool-driven, data engineers still need to write core data processing code proficiently in different frameworks and languages. They must also employ proper code-testing methodologies and may need to solve custom coding problems beyond their chosen tools, especially when managing infrastructure in cloud environments through Infrastructure as Code (IaC) frameworks.

## Data engineering best practices

Navigating the data engineering world demands precision and a deep understanding of best practices. Low-quality data leads to skewed analytics, resulting in poor business decisions.

| Best practice | Importance |
| --- | --- |
| Proactive data monitoring | Regularly checks datasets for anomalies to maintain data integrity. This includes identifying missing, duplicate, or inconsistent data entries. |
| Schema drift management | Detects and addresses changes in data structure, ensuring compatibility and reducing data pipeline breaks. |
| Continuous documentation | Manages descriptive information about data, aiding in discoverability and comprehension. |
| Data security measures | Controls and monitors access to data sources, enhancing security and compliance. |
| Version control and backups | Tracks change to datasets over time, aiding in reproducibility and audit trails. |

# References
[1] "[**Fundamentals of Data Engineering**](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)" 