FROM python:3.6.5


RUN  pip install awscli \
	&& pip install boto3 \
	
CMD ["python3", "costScript.py]
