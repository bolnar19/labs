Reference: https://docs.docker.com/reference/compose-file/

### docker-compose.yml examples
```yaml
version: '2'

networks:
  networ_1:
    driver: bridge
services:
  networ_1:
    # Build image with Dockerfile
    build: . or ./directory_Dockerfile
    image: nameImage:1.0.0
    restart: Always #Always on-failure
    container_name: networ_1
    hostname: "host1"
    ports:
      - "11:11"
      - "22:22"
    # Array syntax
    environment:
      - TZ=America/Bogota
    # Map syntax
    environment:
      TZ: "America/Bogota"
    networks:
      - networ_1
    volumes:
      - ./test.zip:/tmp/test.zip
    # Set user to run container
    user: root
    # Docker alive
    command: tail -f /dev/null
