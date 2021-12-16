FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# 替换pip国内源
RUN pip install -i https://pypi.douban.com/simple pip -U \
    && pip config set global.index-url https://pypi.douban.com/simple \
    && pip config set global.trusted-host pypi.douban.com \

# For development, Jupyter remote kernel, Hydrogen
# Using inside the container:
# jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888
ARG INSTALL_JUPYTER=false
RUN bash -c "if [ $INSTALL_JUPYTER == 'true' ] ; then pip install jupyterlab ; fi"

COPY . /app
ENV PYTHONPATH=/app