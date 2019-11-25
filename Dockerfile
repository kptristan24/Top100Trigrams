FROM python:3
ADD ngrams.py / 
RUN pip install -U pytest argparse
RUN chmod +x ngrams.py
COPY tests/ tests/
CMD [ "python", "ngrams.py", "tests/kjb.txt" ] 
#CMD [ "python", "-m", "pytest" ]
