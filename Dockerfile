FROM python:3.10
RUN pip install requests
ADD jbcaip.py .
EXPOSE 18433/tcp
CMD [ "python", "./jbcaip.py"]