FROM node:15
EXPOSE 3000
ENV VCAP_APP_HOST="0.0.0.0"
WORKDIR /var
RUN git clone https://github.com/simplicitesoftware/nodejs-demo.git
WORKDIR /var/nodejs-demo
RUN npm install
CMD [ "npm", "start"]
