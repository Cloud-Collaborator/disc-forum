FROM node

WORKDIR /app/frontend
COPY /node_modules/ /app/frontend/node_modules
COPY package.json /app/frontend

RUN npm install

EXPOSE 3000
CMD ["npm", "start"]