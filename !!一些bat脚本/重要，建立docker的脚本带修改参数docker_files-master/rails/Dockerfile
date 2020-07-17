FROM ruby:2.6.3

RUN apt-get update \
    && apt-get update -qq \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get install -y libxml2-dev libxslt1-dev \
    && groupadd -r rails \
    && useradd --no-log-init -r -g rails rails \
    && mkdir /home/rails \
    && chown -R rails:rails /home/rails \
    && curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get install -y nodejs

USER rails

WORKDIR /home/rails

RUN gem install rails -v 5.2.3

EXPOSE 3000

CMD ["bash"]
