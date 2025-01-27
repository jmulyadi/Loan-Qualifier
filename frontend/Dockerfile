# Use official Node.js image to build and run the frontend
FROM node:16-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json /app/
RUN npm install

# Copy the rest of the frontend code
COPY . /app/


# Copy SSL certificates into the container
COPY ./private.key /app/private.key
COPY ./certificate.crt /app/certificate.crt

# Build the app for testing
RUN npm run build

# Expose the port the app will run on
EXPOSE 3000

# Serve the build with a simple web server
CMD ["npm", "run", "dev"]
