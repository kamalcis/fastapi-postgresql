# Build Docker image to Local Docker Desktop
        CMD> docker build -t fastapi-app 
# Run the docker container from your local
        CMD> docker run -d -p 8000:80 fastapi-app

# Push to docker hub
        # First need to rename the image with appropriate tag
        CMD> docker tag fastapi-app:latest kamalcis/fastapi-app:latest

        # Then push it to the docker hub
        CMD> docker push kamalcis/fastapi-app:latest


The docker image name is fastapi-app