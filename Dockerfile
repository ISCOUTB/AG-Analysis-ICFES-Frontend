FROM node:22-alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install --omit=dev

COPY . .

RUN npm run build

CMD [ "node", "/app/.output/server/index.mjs" ]



