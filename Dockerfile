FROM indomie/indomie:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By IndomieUserbot ━━━━━

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b IndomieUserbot https://github.com/IndomieGorengSatu/IndomieUserbot /home/IndomieUserbot/ \
    && chmod 777 /home/IndomieUserbot \
    && mkdir /home/IndomieUserbot/bin/
WORKDIR /home/IndomieUserbot/
COPY ./sample.env ./config.env* /home/IndomieUserbot/

#Install python requirements
RUN pip install -r requirements.txt

# Finalization
CMD ["python3", "-m", "userbot"]
