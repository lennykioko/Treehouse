# Build fron the node base image
FROM node:7

# Set up app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

# Bundle app source
COPY . /usr/src/app

# Expose the server to the host machine
EXPOSE 8080

# Run this command on startup
ENTRYPOINT ["npm", "start"]

# docker build -t node-js-app .
# docker run -p 8080:8080 -d node-js-app
# docker ps
# docker logs <cid> container id
# docker exec -it <cid> /bin/bash
