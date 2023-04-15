FROM python:3.11
WORKDIR /app
ENV SECRET_KEY="alqasim-alzakwani-(g_e!(#=h0n-2*mevcagx^7=e@4m4g160#6&yo*4sigu+2sqr4"
ENV DEBUG="True"
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/

RUN chmod +x /app/app-entrypoint.sh
RUN chmod +x /app/worker-entrypoint.sh


