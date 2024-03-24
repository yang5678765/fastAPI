**Docker on windows**
----
* **Get image**

    build by docker file: 
    `docker build -t myimage .`

    OR

    pull from docker hub: 
    
    `docker push yang5678765/fastapi_server`

* **Run container based on the image**

    `docker run -d -p 8080:8080 myimage`

* **Check API doc**

    `http://127.0.0.1:8080/docs`
