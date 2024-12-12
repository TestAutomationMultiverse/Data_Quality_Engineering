# **A guide to ETL Testing**

[

![Mohit Mair](https://miro.medium.com/v2/resize:fill:66:66/1*9pgCDEawG-bviQsbfsGcCQ.jpeg)





](https://medium.com/@mohitmair?source=post_page---byline--f1967115a996--------------------------------)

[

![Analytics Vidhya](https://miro.medium.com/v2/resize:fill:36:36/1*Qw8AOQSnnlz7SLiwAda2jw.png)





](https://medium.com/analytics-vidhya?source=post_page---byline--f1967115a996--------------------------------)

[Mohit Mair](https://medium.com/@mohitmair?source=post_page---byline--f1967115a996--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fa2950d4ee4b5&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fanalytics-vidhya%2Fetl-testing-in-a-nutshell-f1967115a996&user=Mohit+Mair&userId=a2950d4ee4b5&source=post_page-a2950d4ee4b5--byline--f1967115a996---------------------post_header-----------)

Published in

[

Analytics Vidhya

](https://medium.com/analytics-vidhya?source=post_page---byline--f1967115a996--------------------------------)

·

8 min read

·

Jul 26, 2021

[

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fanalytics-vidhya%2Ff1967115a996&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fanalytics-vidhya%2Fetl-testing-in-a-nutshell-f1967115a996&user=Mohit+Mair&userId=a2950d4ee4b5&source=---header_actions--f1967115a996---------------------clap_footer-----------)

44

2

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff1967115a996&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fanalytics-vidhya%2Fetl-testing-in-a-nutshell-f1967115a996&source=---header_actions--f1967115a996---------------------bookmark_footer-----------)

[

Listen







](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Df1967115a996&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fanalytics-vidhya%2Fetl-testing-in-a-nutshell-f1967115a996&source=---header_actions--f1967115a996---------------------post_audio_button-----------)

Share

> Get started with ETL Testing using this blog which is written based on real-world industry case studies and experience.

![](https://miro.medium.com/v2/resize:fit:1000/1*pCNgyBol6B8pUwRY0JgG3Q.png)

A typical ETL flow (stage names may vary)

Even though the above diagram is a bit of simplification, this is how most ETL workflows may look like.

To put simply, ETL is an automated process to move data from source systems to target systems, involving various stages for **E**xtract, **T**ransform and **L**oad sub-processes, _without data-loss_ and while maintaining _data-integrity_. This also, is usually referred to as _data-migration_.

The objective of ETL is to have a clean, classified, enriched and curated data at one place (_data warehouse or data lake_). Thats the first-step and a prerequisite for running _data-analytics_ and _data-science_. Machine-learning models and analytic tools are run against this data to fetch useful information and predictions, based on which business decisions can be taken.

Now, this data may arrive from source in _batches_ (one-time, on-demand loads) or _real-time_ (continuous, periodic streams). While the ETL approach for both may differ, but, the essence remains the same- which is to successfully move data from source to target without any data loss or errors. And if there are any unexpected errors, they should be traceable and manageable.

In this article, let’s focus on the approach and strategy to test a typical ETL workflow.

There are several Big Data technologies available in market to implement ETL. Some are on-prem and some are cloud-based. Testing technology and tools also vary depending on that. Thats why, we will keep this article as much technology-agnostic as possible.

# Testing Types:

## 1\. Testing of ETL components in isolation

This includes testing of any component thats involved in ETL workflow. It could be micro-services, transformation engines (like Google Dataflow, Spark, etc), pipelines (Kafka, Google PubSub, etc.), storage components (like HDFS, Google GCS buckets, etc.), landing zones (like unix directories, etc.), workflow managers & orchestrators (like Argo, etc.) and any other participating component.

It is important to assure that each component is working as expected as per business requirements and system design- both functionally and non-functionally (performance, load, disaster recovery, etc).

This testing focuses on testing of component in isolation using mocks and also its integration with other components.

## 2\. Data Quality Checks

Data quality checks verify that the source data is of acceptable quality as per metadata agreements defined in requirements. There should not be any inconsistency or inaccuracy in data. Some common checks could be null-value check on certain columns, dup-checks, blank header and/or footers, etc.

![](https://miro.medium.com/v2/resize:fit:651/1*QtMdu-lf3FdxqdRs7SQDUQ.png)

Any bad data is rejected, separated and logged for audit purposes. The good data is _ingested_ and goes through the rest of the ETL stages. Testing should cover both scenarios.

## 3\. Testing Filter conditions

The source systems usually send a lot of raw data. Some of that data may not be relevant from business perspective. Thats why it needs to be filtered. While the RAW data layer stores all the data, only _FILTERed IN_ data gets propagated to further processing. _FILTER OUT_ data is, again, segregated and logged for audit purposes. Filter conditions are defined as per business requirements.

![](https://miro.medium.com/v2/resize:fit:700/1*x9Kr7CTlWAUr_1-5ppet-w.png)

Some examples:

1.  filter all records older than a certain date. E.g all accounts opened before 01/03/21
2.  filter all records where a specific column has a specific value. E.g all accounts with _Acc\_Status_ = Open

## 4\. Testing Data Transformation logics

Just like filter conditions, transformation logics are also defined in business requirements. Data is transformed and enriched based on these requirements. Some transformations are as simple as direct conversion of values whereas some transformations can be complex calculations.

![](https://miro.medium.com/v2/resize:fit:700/1*FAagTrpR5i1oHXrYEmOEtg.png)

Test scenarios are derived based on the logics and cover positive, negative and boundary-value scenarios. It is also important to test how transformation engines behave when any expected errors are encountered, especially in calculation-based rules.

Output of data transformation is clean and curated data.

Some transformation rule examples:

1.  Transform True/False value in source to 1/0 in target.
2.  Transform _Account\_Id_ in target by prefixing 0s in Account\_Id of source e.g 72737455 to 00072737455
3.  Transform _predictive\_index_ in target by multiplying _eod\_balance_ by 0.025

## 5\. Schema Validation

Schema validation refers to testing of source and target schemas. Schemas are structure definitions of source and target, defined by solution architects. This typically includes column data-types, max/min length, unique check, header/footers, etc.

For example: _Telephone\_Number_ field in source schema could be 11 digits whereas 10 in target schema. This will lead to a schema error during ETL.

## 6\. Testing Data Mappings

This refers to which column(s) in source map to which column(s) in target. It is defined in business requirements usually in a simple excel format. However technical implementation treats this differently and uses other technologies.

For example:

1.  _Account\_Id_ in source should map to _int\_acc\_id_ in target
2.  _telephone\_num_ in source should map to _prim\_tele\_no_ on target

## 7\. Data Validation & Reconciliation Testing

Data reconciliation is a verification process to ensure that the data-migration or ETL process has transferred the data correctly from source (LHS)to target (RHS) by comparing the target data against the original source. This comparison can be between two ETL stages OR between source and target.

Since the volume of data is huge, it is nearly impossible to compare data manually of using generic comparison tools. Reconciliation rules are special mathematical checks using which confidence is gained that the data has moved successfully. Recon rules typically generate 3 types of reports- _DIFF_, _DETAIL_ and _SUMMARY_.

Common types of reconciliation techniques are:

-   **Record Count Reconciliation**: Comparing # of records at source vs target.
-   **Missing Records (Destination break)**: Records that exist at source but not exist in target.
-   **Extra Records (Source break)**: Records that exist in target but not at source.
-   **Duplicate Records**: Records that occur multiple times in target.
-   **Summary Reconciliation (MIN, MAX, SUM, AVG)**: Mathematical calculations on column(s) at source vs target. For e.g average eod\_balance on source should be equal to average eod\_balance in target.
-   **Record Content Reconciliation**: Field-by-field comparison of source and target records.

Recons are driven by Financial and Operational proof points.

Reconciliation testing is usually done on full volume data; that’s where it yields most value.

Reconciliations are automated using technologies like Spark or similar which are capable of handle huge data processing. There are some commercial tools available as well like QuerySurge. Some organisations prefer to build their own bespoke tools as well.

Some recons (like record content) can be very resource intensive and may take quite long to run (depending on volume of data). This needs to be kept in mind and such recons should be done only if absolutely necessary.

## 8\. End-to-end testing

When all ETL stages and their components are well tested, E2E testing is performed. This is to ensure that the ETL process works flawlessly from start to finish and everything is orchestrated as expected.

## 9\. Full Volume Testing

Full Volume testing refers to E2E testing of ETL with large datasets (millions and billions of records.) The objective is to test how ETL behaves and performs with huge and varied dataset. This helps to uncover unforeseen scenarios and performance issues, if any.

Apart from above there are some very specialised testings that are performed on ETL like Data Integrity, Data Lineage and Data Classification Testing.

## 10\. Testing extraction at source

This is to ensure that the source file(s) are created as expected and contain right data from the source system(s). Testing of all data extraction conditions and logics.

# Test Data Strategy:

## 1\. Synthetic or Manufactured Data

-   This test data is manufactured using bespoke test-data creation tools/mechanisms
-   Format and schema is aligned with the source file format and schema
-   Test data combinations are manufactured according to test scenarios
-   Test data manufacturing is automated, on-demand and is usually embedded in automation scripts
-   Synthetic test data is best suited for smaller sets and functional/acceptance testing of stories during the sprint.
-   The objective to use synthetic data is to prove that ETL components are “functionally” working as expected in both negative and positive scenarios.
-   Large volume of synthetic data can be used for load testing.

## 2\. Obfuscated Data

-   Obfuscated data is real data but with _masked_ (hidden) PI information like names, NiNo, Social Security number etc. These values are often replaced with random, junk characters to protect data confidentiality.
-   Creating this type data requires effort of obfuscation (masking)
-   Its a high quality test data with good variety of values because of which it helps in uncovering edge-case scenarios.
-   Ideal for full volume E2E testing

## 3\. Real Data

-   Real data without masking
-   Typically used on PROD environments
-   Tight access controls

# Indicative Test Plan

This is an indicative test plan for an ETL testing project.

![](https://miro.medium.com/v2/resize:fit:1000/1*nw0I2CbLC7fwOeyCJjgoIw.png)

Key points are:

-   Component testing on BUILD (usually as part of CI/CD)
-   Followed by few rounds of E2E Testing on INT
-   Followed by 1-n cycles of Full Volume Testing with Obfuscated Data
-   Followed by 1-n cycles of Full Volume Testing with Real Data on a PROD-like environment
-   Followed by Live-Proving
-   Environment clean-up after each test cycle to bring everything to base-state.

# Common Challenges

Some common challenges faced could be:

-   Data Obfuscation capability is often complex to build
-   Strict data access controls and mechanism are involved which sometimes can limit testing activities
-   Environment clean-up can be a tricky exercise so a proper runbook must be prepared
-   E2E flow usually takes a while to work due to numerous dependencies. Until then mocks must be used. ETL stages can be difficult to mock.
-   Getting hold of accurate source and target schemas mapping can be challenging.
-   Choosing right testing tool is key. Native technologies may work best as they seamlessly integrate with source code and CI/CD process.
-   Full volume testing and data reconciliations need powerful test environment which can be costly to build and execute

[

](https://medium.com/tag/etl-testing?source=post_page-----f1967115a996--------------------------------)



