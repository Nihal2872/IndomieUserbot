#━━━━━ Userbot Telegram ━━━━━
FROM indomie/indomie:buster
#━━━━━ By IndomieUserbot ━━━━━

RUN git clone -b IndomieUserbot https://github.com/IndomieGorengSatu/IndomieUserbot /home/IndomieUserbot/ \
    && chmod 777 /home/IndomieUserbot \
    && mkdir /home/IndomieUserbot/bin/

WORKDIR /home/IndomieUserbot/

COPY ./sample.env ./config.env* /home/IndomieUserbot/

#Install python requirements
RUN pip install -r requirements.txt

# Finalization
CMD ["bash","start"]
