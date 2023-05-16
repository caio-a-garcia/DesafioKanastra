# Desafio Kanastra
## Billing System

This project implements a simple billing API. Commands are expected to be run from project root directory.

### Setup
Create virtual environment:
`python -m venv .env`

Activate environment (Windows):
`.env\Scripts\activate`

Install dependencies:
`pip install -r requirements.txt`

### Running Project
Commands in this section should be run with environment activated.

The server exposes endpoints for billing and payment.
To start the server run (Windows):
`start-server`

The scheduler checks for standing debts, and simulates the generation of invoices and sending of email. It is configured to run this task every 6 hours.
To start the scheduler run (Windows):
`scheduler`

For running tests:
`pytest`

### API
For SwaggerUI documentation of the API, start the server and point your browser to the "/docs" endpoint. When running on the default port, go to the url:
`http://localhost:8000/docs`

The "/billing" endpoint expects to receive a CSV file from the user with the fields:
  - name: string
  - governmentId: int
  - email: string
  - debtAmount: int
  - debtDueDate: str (a date with format "YYYY-MM-DD")
  - debtId: int
  
The "/payment" endpoint is to be used as a webhook and expects a JSON with fields:
  - debtId: str (string representation of an int)
  - paidAt: str (a date with format "YYYY-MM-DD HH:mm:ss")
  - paidAmount: int
  - paidBy: str

### Docker
The current iteration of the project is configured to run a development server inside a container exposing the APIs endpoints, as well as the built-in documentation endpoints, at the usual addresses.

After installing docker, the first step is to build a docker image from the Dockerfile at the root of this repository. To do that, go to the root of the cloned project with the command line, then:
`docker build -t dk/server .`

The command above should be run with administrator priviledges, so precede the command with `sudo` on Linux; on Windows, open the command line as admin. Don't forget the period ('.') at the end of the command, that is what indicates to `docker build` that the Dockerfile used to build the image should be found in the present directory.

Having built the image, you can run a container from it with:
`docker run --rm -d -p 8000:8000 --name server dk/server`

This command too should be run with admin priviledges. 
The `--rm` argument makes sure the container is removed once it stops running. It can be usefull to omit this argument if there is any need to look at the container logs after it stops.
The `-d` argument runs the container in the background (as a daemon).
The `-p` flag connects a port on the host to a port on the container. Using `-p 5000:8000`, for instance, will make the server available on the host at port 5000. If there is any need to change the port in the container, modifications would be required to the Dockerfile, and very likely to the application code as well.
The `--name` argument defines the name given to the container.
The last argument to `docker run` is the name of the image from which the container will be built. This should be the same name given to `docker bulid`s `-t` flag.
The use of the "/" character in `dk/server` is a convention (i.e. it is used to pass information to the user, not needed by the machine).
