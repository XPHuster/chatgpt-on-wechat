FROM python:3.9

COPY . /app

RUN pip install --no-cache -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn \
  && pip install --no-cache -r /app/requirements-optional.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn \
  && chmod +x /app/entrypoint.sh

WORKDIR /app

ENTRYPOINT ["./entrypoint.sh"]
