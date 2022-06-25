#━━━━━ Userbot Telegram ━━━━━
FROM indomie/indomie:buster
#━━━━━ By IndomieUserbot ━━━━━



RUN git clone -b IndomieUserbot https://github.com/IndomieGorengSatu/IndomieUserbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot


#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/IndomieGorengSatu/IndomieUserbot/IndomieUserbot/requirements.txt

# Finalization
CMD ["python3", "-m", "userbot"]
