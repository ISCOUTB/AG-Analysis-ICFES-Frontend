FROM node:18-alpine as build

WORKDIR /app
COPY package*.json ./
COPY . .
RUN npm install
RUN npm run build

FROM node:18-alpine

WORKDIR /app
COPY --from=build /app/.output .output
COPY package*.json ./
RUN npm install --production

EXPOSE 3000
CMD [ "node", ".output/server/index.mjs" ]