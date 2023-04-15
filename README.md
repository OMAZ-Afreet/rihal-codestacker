###### Project submitted by Alqasim Alzakwani for Rihal’s (CODESTAKER Challenge)

# **_Approach_**

The first challenge, and probably the hardest, was how would I _define_ a sentence. Since there wasn't an example nor a PDF specimen to test my solution on, I took the liberty to come up with a definition of my own. Many ideas came to mind, and many trials were conducted. Eventually, I landed on the fact that sentences are separated by ". " (namely a period followed by a space).

Other than that, everything was relatively straight forward, from choosing the technologies to planning and execution. To note a few, I took performance and optimization up a notch by delegating heavy operations to background workers and caching repeated tasks, like parsing and top words respectively. In addition, practicality and usefulness were important to me that I added extra functionalities to most endpoints (check UI I built to interact with this API at "http://localhost:8000/" and the docs at "http://localhost:8000/docs/" or /docs/v2/)

# **_Instructions_**

Assuming git and docker compose (3.8) are installed and available to you. If you are using incompatible docker engine with this version, feel free to change it in docker-compose.yml (ex. 3).

### 1 Get the source code

Either download it from the email submission or clone it from this repo:

```shell
git clone https://github.com/qzakwani/rihal-codestacker.git
```

### 2 Run app using docker compose

Navigate to the root of the project (where file docker-compose.yml is located) and run:

```shell
docker compose up -d
```

and done! Running on localhost port 8000

Check the UI and the docs I made to interact with and describe the API.  
UI: http://localhost:8000/  
DOCS: http://localhost:8000/docs/ or http://localhost:8000/docs/v2/

#### IMPORTANT: All endpoints MUST end with a slash '/'

---

NOTE: I ran into some problems due to docker, versions and permissions. So please if these instructions do not work contact me at q.zak003@gmail.com should be easily fixed, but hopefully it runs smoothly (I trust it).  
Everything worked perfectly on my machine: MacBook macOS Monterey.

# Thank you for the opportunity
