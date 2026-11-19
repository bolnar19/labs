# docker-compose examples

* Reference: https://docs.docker.com/reference/compose-file/

```yaml
#version: '2'

services:
  app:

    # Build image using Dockerfile in current directory
    build: .

    # Build image using Dockerfile in another directory
    # build: ./docker/Dockerfile

    # Build image and assign a name/tag to the resulting image
    image: my-app:1.0.0

    restart: always #always on-failure
    container_name: my-app

    hostname: "host1"

    dns:
      - 8.8.8.8
      - 1.1.1.1

    ports:
      - "8080:8080"
      - "8443:8443"

    # Environment - array syntax
    # environment:
    #   - TZ=America/Bogota
    #   - JAVA_OPTS=-Xms512m -Xmx1024m

    # Environment - map syntax
    environment:
      TZ: America/Bogota
      JAVA_OPTS: "-Xms512m -Xmx1024m"

    networks:
      - networ_1

    volumes:
      - ./test.zip:/tmp/test.zip
      - ./data:/data

    # Set user to run container
    user: root

    # Keep container alive
    command: tail -f /dev/null

networks:
  networ_1:
    driver: bridge

```
