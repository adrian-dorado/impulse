# Impulse

- Adrian, Front-End Software Engineer and Designer
- Evan, Backend Software Engineer
- Morgan, Front-End Software Engineer and Designer
- Nellie, Backend Software Engineer

# Intended Market

- Anyone who is curious about trying new things or anyone who is delighted by the novelty of things and stuff.
- For people who like the novelty of receiving a box of products catered directly to them.

# Functionality

## Users:

- Users will create an account to log in and be able to log out as well.
- Users will choose between a "Things" bow or a "Clothing" box, and a certain number of items will be in the box.

## Inventory:

- Inventory will update with current items and things available for boxes
- Inventory will sort itself into tags based on what the user picks for their box

## Clothes and Accessories Rental:

- A similar subscription box but the items in it will need to be returned.
- Clothes and Accessories can be picked for certain occasions based on website tags
- Boxes can be recycled and returned for a discount on the next months box.
- If the rental isn't returned in the alloted time frame, the items price will be charged to the user.

## Social Media Forums:

- Users can post photos of their boxes and stylings to the forums
- Users can submit possible items for inventory and be voted on.
- Users can leave reviews of boxes they have received and people can comment on them.

## Design

- [API design](docs/apis.md)
- [Data model](docs/data-model.md)
- [GHI](docs/ghi.md)
- [Integrations](docs/integrations.md)

# Installation and Testing Guide for Impulse

## Want to test Impulse on your own machine? Want to make your own storefront based on Impulse? Follow these steps!

## Setup Environment:

- This application requires Docker to run locally, if you do not have it installed, please navigate to [Docker.com](https://www.docker.com) and install the version specific to your machine.
  - Note, if you are a Windows user installing Docker for the first time, you will be required to enable Virtualization in your BIOS, the directions for this can be found [here](https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html), via Berkeley EDU.
- Windows users will also be required to install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
  - Step 4 is all that is required for Docker to run our application locally.
- Restarting your machine will be required after these steps for Docker to finish the installation.

# Setup is identical on both Mac and Windows:

- Fork, Clone, and Star the repository from [MEAN Coders](https://gitlab.com/mean-coders/module-three-project)
- Navigate to the root directory of the project in Terminal or Powershell
- Prior to running these commands, make sure to launch Docker.
- On first start,run:
```
  docker volume create postgres-data
  docker volume create pgadmin
  docker-compose up --build
```
- For soft resets:
```
  docker-compose down
  docker-compose up --build
```

Congratulations, you've now installed Impulse on your local machine!


# Unit Tests exist for Impulse and can be enabled by following these steps:

- Navigate to the pgadmin container here, [PgAdmin](http://localhost:8060)
- Login with the supplied username and password on the docker-compose.yaml file under the 'pgadmin' service.
- Once logged in, register the server by right clicking server then Register > Server.
- In the window pop-up, provide a name for the database
- Navigate to the connections tab on top of the pop-up window, Host name/address will be 'postgres'
- Username will be postgres (as we need to be able to provide admin permission)
- Password is supplied in the docker-compose.yaml under the 'postgres' service
- Save the password for ease of access and save the form, the pop-up should disappear.
- Once the server is registered, click the dropdown on servers, then the dropdown for Login/Group Roles
- Right-click products, click properties in the pop-up, navigate to 'Privileges' in the pop-up
- Make sure create databases is toggled on and save.
- Repeat the same steps for subscriptions
- This allows for test-databases to be created in the project


To run tests:

### Set up pgadmin:

- go to [localhost:8060/login](localhost:8060/login) in the browser. Log in with any email and password.
- Click on Add New Server; name it `postgres-data`
- Click on Connection tab. 
  - For Host name and Username: 
    - `postgres`
  - Password: 
    - `test-databases` 
- Click `Save`.
- On the right side, click Servers >> Login/Group Roles
  - Right-click on Products >> Properties. Click on Privileges. On `Create databases?` move the slider right.
  - Right-click on Subscriptions >> Properties. Click on Privileges. On `Create databases?` move the slider right.
  
Then:
- Enter the Docker CLI for the application you would like to test.
- Enter: `python manage.py test`
- This should run the tests for the individual service, repeat the steps in other services to test.
