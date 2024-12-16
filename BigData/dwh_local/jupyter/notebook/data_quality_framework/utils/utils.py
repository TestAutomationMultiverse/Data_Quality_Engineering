import logging
from bokeh.plotting import figure, show, column, output_file, save
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    NumeralTickFormatter,
    BasicTicker,
    LabelSet,
    CustomJS,
    DataTable,
    TableColumn,
    NumberFormatter,
)

logger = logging.getLogger(__name__)


def create_df_from_dq_results(spark, dq_results):
    """
    Creates a DataFrame from data quality (DQ) results.

    Args:
        spark (SparkSession): A SparkSession object.
        dq_results (dict): A dictionary containing DQ results.

    Returns:
        pyspark.sql.DataFrame: A DataFrame containing DQ data.
    """

    logger.info("Starting to create DataFrame from DQ results.")
    dq_data = []
    for result in dq_results["results"]:
        status = "PASSED" if result["success"] else "FAILED"
        dq_data.append((
            result["expectation_config"]["kwargs"]["column"],
            result["expectation_config"]["meta"]["dimension"],
            status,
            result["expectation_config"]["expectation_type"],
            result["result"]["unexpected_count"],
            result["result"]["element_count"],
            result["result"]["unexpected_percent"],
            float(100 - result["result"]["unexpected_percent"]),
        ))

    dq_columns = [
        "column",
        "dimension",
        "status",
        "expectation_type",
        "unexpected_count",
        "element_count",
        "unexpected_percent",
        "percent",
    ]
    logger.debug(f"Creating DataFrame with columns: {dq_columns}")
    dq_df = spark.createDataFrame(data=dq_data, schema=dq_columns)
    logger.info("DataFrame created successfully.")
    return dq_df


def create_data_qa_report(dq_df):
    """
    Creates a Bokeh HTML report for data quality analysis.

    Args:
        dq_df (pyspark.sql.DataFrame): A DataFrame containing DQ data.

    Returns:
        None: Creates a data_qa_report.html file.
    """

    # Specify the output file before creating the plot
    output_file("data_qa_report.html")

    source = ColumnDataSource(dq_df)

    # Overall Status Bar Chart
    overall_status_counts = dq_df.groupby("status").size().toPandas()
    overall_status_chart = figure(
        x_range=overall_status_counts.index.tolist(),
        height=300,
        title="Overall Data Quality Status",
        toolbar_location=None,
        tools="",
    )
    overall_status_chart.vbar(
        x="status",
        top="size",
        width=0.5,
        source=overall_status_counts,
        legend_field="status",
        color=["green", "red"],
        line_color="white",
    )
    overall_status_chart.yaxis.major_label_orientation = "horizontal"
    overall_status_chart.yaxis.formatter = NumeralTickFormatter(format="0")

    # Breakdown by Expectation Type
    expectation_types_counts = dq_df.groupby("expectation_type").size().toPandas()
    expectation_types_chart = figure(
        x_range=expectation_types_counts.index.tolist(),
        height=300,
        title="Breakdown by Expectation Type",
        toolbar_location=None,
        tools="",
    )
    expectation_types_chart.vbar(
        x="expectation_type",
        top="size",
        width=0.5,
        source=expectation_types_counts,
        legend_field="expectation_type",
        color=["skyblue"],
        line_color="white",
    )
    expectation_types_chart.xaxis.major_label_orientation = 0.75  # Rotate for readability
    expectation_types_chart.yaxis.major_label_orientation = "horizontal"
    expectation_types_chart.yaxis.formatter = NumeralTickFormatter(format="0")

    # Details Table
    columns = [
        TableColumn(field="column", title="Column"),
        TableColumn(field="dimension", title="Dimension"),
        TableColumn(field="expectation_type", title="Expectation Type"),
        TableColumn(
            field="unexpected_count",
            title="Unexpected Count",
            formatter=NumberFormatter(format="0,0"),
        ),
        TableColumn(
            field="element_count", title="Element Count", formatter=NumberFormatter(format="0,0")
        ),
        TableColumn(
            field="unexpected_percent",
            title="Unexpected %",
            formatter=NumeralTickFormatter(format='0.0%'),
        ),
        TableColumn(field="percent", title="Pass %", formatter=NumeralTickFormatter(format='0.0%')),
    ]
    data_table = DataTable(source=source, columns=columns, width=800, height=400)

    # Layout
    layout = column(
        overall_status_chart,
        expectation_types_chart,
        data_table,
    )

    # Save the plot to the specified file
    save(layout)
