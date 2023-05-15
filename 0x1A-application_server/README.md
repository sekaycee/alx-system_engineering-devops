# Application server

Project completed during **Fullstack software engineering** program at **ALX**. It aims to learn about the deployment of application servers and gunicorn.

## Tools

* Script is written in Bash
* Nginx and Gunicorn are used
* Tested on Ubuntu 20.04 LTS

## Tasks, Files and Descriptions

| Task | File | Description |
| ---- | ---- | ----------- |
| 0. Set up development with Python || Let's serve what you built for AirBnB clone v2 - Web framework on web-01 |
| 1. Set up production with Gunicorn || Let's get my production application server set up with Gunicorn on web-01, port 5000 |
| 2. Serve a page with Nginx | `2-app_server-nginx_config` | Build on my work in the previous tasks, by configuring Nginx to serve my page from the route /airbnb-onepage/ |
| 3. Add a route with query parameters | `3-app_server-nginx_config` | Let's expand my web application by adding another service for Gunicorn to handle |
| 4. Let's do this for your API | `4-app_server-nginx_config` | Let's serve what I built for AirBnB clone v3 - RESTful API on web-01 |
| 5. Serve your AirBnB clone | `5-app_server-nginx_config` | Let's serve what I built for AirBnB clone - Web dynamic on web-01 |
| 6. Deploy it! | `gunicorn.service` | Write a systemd script which starts a Gunicorn process to serve the same content as the previous task (web_dynamic/2-hbnb.py) |
| 7. No service interruption | `4-reload_gunicorn_no_downtime` | Write a simple Bash script to reload Gunicorn in a graceful way |

