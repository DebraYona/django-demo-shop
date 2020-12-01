FROM python:3.8.0-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev fontconfig ttf-dejavu
WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY ./requirements/requirement.local.txt ./
RUN pip install -r  requirement.local.txt
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
COPY . .
ENTRYPOINT ["/entrypoint.sh"]
