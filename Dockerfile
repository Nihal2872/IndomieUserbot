#━━━━━ Userbot Telegram ━━━━━
FROM indomie/indomie:buster
#━━━━━ By IndomieUserbot ━━━━━

RUN git clone -b IndomieTag https://github.com/Nihal2872/IndomieTag/blob/IndomieTag /home/IndomieTag/ \
    && chmod 777 /home/IndomieTag \
    && mkdir /home/IndomieTag/bin/

WORKDIR /home/IndomieTag/

RUN pip install -r requirements.txt

CMD ["python3", "-m", "indomie"]
