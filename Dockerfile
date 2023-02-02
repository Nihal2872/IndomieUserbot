#━━━━━ Userbot Telegram ━━━━━
FROM indomie/indomie:buster
#━━━━━ By IndomieUserbot ━━━━━

RUN git clone -b IndomieTag https://github.com/Nihal2872/IndomieTag/blob/IndomieTag /home/IndomieTag/ \
    && chmod 777 /home/IndomieUserbot \
    && mkdir /home/IndomieUserbot/bin/

WORKDIR /home/IndomieTag/

RUN pip install -r requirements.txt

CMD ["python3", "-m", "indomie"]
