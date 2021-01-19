FROM debian:buster-slim
MAINTAINER Your Arjun
RUN apt-get update \
&& apt-get install -y python3-pip python3-dev \
&& cd /usr/local/bin \
&& ln -s /usr/bin/python3 python \
&& pip3 install flask joblib scikit-learn
COPY webapp.py webapp.py
COPY templates templates
COPY product_lkp.pickle1 product_lkp.pickle1
COPY model_pipeline.joblib model_pipeline.joblib
ENTRYPOINT ["python3","webapp.py"]