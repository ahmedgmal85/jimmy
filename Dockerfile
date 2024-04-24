FROM python
WORKDIR /py
COPY . /py
CMD ["python", "py.py"] 
