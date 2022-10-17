# Base image
FROM node:lts-alpine

# Install serve package
RUN npm install -g http-server

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the project files
COPY . .

# Build the project
RUN npm run build

# Expose a port
EXPOSE 8080

# Executables
CMD ["http-server", "dist"]
