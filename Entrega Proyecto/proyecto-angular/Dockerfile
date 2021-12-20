#Primera Etapa

FROM node:17-alpine as build-step

RUN mkdir -p /app

WORKDIR /app

COPY  package.json /app

RUN npm install

COPY . /app

RUN npm run build --prod

#Segunda Etapa

FROM nginx:1.21.4-alpine

COPY --from=build-step /app/dist/angular-app /usr/share/nginx/html