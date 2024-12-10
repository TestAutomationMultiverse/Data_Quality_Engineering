FROM apache/zeppelin:0.11.2

RUN pip install -U pip &&\
    pip install --no-cache-dir \
    pandas \
    openpyxl \
    findspark \
    # tensorflow-serving-api \
    great_expectations \
    pydeequ \
    pandera \
    soda-core-postgres \
    ydata-profiling[notebook,unicode,pyspark] jupyter-contrib-nbextensions \
    chispa pyspark
    # bamboolib==1.30.19 install_nbextensions 
    #&& python -m  && jupyter nbextension enable --py widgetsnbextension
