FROM node:18-alpine AS builder

WORKDIR /app

ENV CI=false \
    SKIP_PREFLIGHT_CHECK=true

COPY package*.json ./
RUN npm ci --prefer-offline --no-audit

COPY . .
RUN npm run build

FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 3000

HEALTHCHECK --interval=10s --timeout=5s --retries=5 \
    CMD wget --quiet --tries=1 --spider http://localhost:3000/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
