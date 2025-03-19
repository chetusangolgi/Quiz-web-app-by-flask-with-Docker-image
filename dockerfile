FROM python

WORKDIR /app

COPY . .

RUN pip3 install flask
RUN pip install supabase

CMD [ "python3", "app.py" ]