# Frontend Dockerfile - Fixed version
FROM node:18-bullseye

WORKDIR /app

# Copy package files first
COPY package*.json ./

# Install Quasar CLI globally
RUN npm install -g @quasar/cli

# Debug: Show what files are available in the build context
RUN echo "Files in current directory before copying:" && ls -la

# Copy only necessary files for build
COPY . ./

# 1. Remove stale lock & modules
RUN rm -rf package-lock.json node_modules

# 2. Force install with legacy peer deps to resolve conflicts
RUN npm install --platform=linux --arch=x64 --omit=optional --legacy-peer-deps --force

# 3. Install rollup specifically for the platform
RUN npm install --no-save @rollup/rollup-linux-x64-gnu --legacy-peer-deps

RUN ls node_modules/@rollup/rollup-linux-x64-gnu/

# 4. Now build
RUN npm run build

EXPOSE 9000
CMD ["quasar", "dev"]