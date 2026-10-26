# ANSWERS.md - CENG413 hw-1

### 1. Explain the order of the instructions in your Dockerfile. What would happen to build time if you changed the order of two of them?
-In this Dockerfile example, we firstly copied `requirements.txt` and installed dependencies using `pip`, and then copied the application code using `COPY . .`. This makes it possible to use Docker's cache, as the dependencies are expected to change less frequently than the code. If we copied the code at first, even a small code change would trigger Docker to reinstall dependencies and increase the time of building the application.

### 2. What happens to data written inside a container when the container is removed? How would you keep the data, and where should an application keep important state?
-All information stored in a container's local filesystem is temporary and is lost once the container is destroyed. To ensure data continuity, Docker users need to make use of either Docker volumes or bind mounts connected to the host machine. Applications need to keep their important data outside of containers—typically in some kind of database, external cloud storage, or a persistent storage system.

### 3. Why is the `latest` tag a risk for reproducibility? What did you use instead?
-The use of the latest tag poses a threat to the reproducibility aspect; it points to the most recent version of some image which can be changed anytime leading to unexpected consequences related to all subsequent builds. Therefore, instead of latest we have specifically pinned our base image version to python:3.11-slim allowing us to achieve reproducible, consistent, and predictable builds across different environments.This ensures that every build uses the exact same underlying libraries without sudden breakages.

### Note on AI Assistant
I used an AI assistant to understand Docker build errors and format the documentation files.
