# supercisor + uwsgi
FROM shop_admin:base
RUN mkdir /shop_admin
WORKDIR /shop_admin
COPY . /shop_admin
COPY supervisord.conf /etc/supervisor/
RUN chmod +x /shop_admin/start.sh && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]