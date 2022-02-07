# Lab 2: Web Applications Security

> Igor Mpore
>
> BS19-CS01
>
> i.mpore@innopolis.university

## Part 1: Setting up a Web Application with SSL certificate and a database.

I created a Login and Sign up screens in HTML,CSS and NodeJS to use as my web application to use throughout this lab called WebToy. The project is on my [github](https://github.com/desmigor/Secured_web_app) and here are the two screenshots of the pages.

<img src="/home/migor/Documents/Secured_web_app/images/login.png" style="zoom:50%;" />

<img src="/home/migor/Documents/Secured_web_app/images/signup.png" style="zoom:50%;" />

After this, I created root certificate for my webapp (WebToy) using the following commands.

### Creating SSL Cerficate

1. Creating a root certificate:

```bash
openssl genrsa -des3 -out rootCA.key 4096
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.crt
```

![image-20220131220428131](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220131220428131.png)

![image-20220131220627992](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220131220627992.png)

2. Generating my root certificate

```bash
openssl genrsa -out webtoy.com.key 2048
```

![image-20220131220852203](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220131220852203.png)

3. Creating a Certificate Signing Requests:

```bash
openssl req -key webtoy.com.key -new -out webtoy.com.csr
```

![image-20220131221243065](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220131221243065.png)

4. Creating self signed certificate and lastly I converted the certificate to DER:

```bash
openssl x509 -req -in webtoy.com.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out webtoy.com.crt -days 365 -sha256

openssl x509 -in webtoy.com.crt -outform der -out webtoy.com.der
```

![image-20220131221519698](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220131221519698.png)



### Setting up the database and it's basic authentication.

We'll be using PostgreSQL and PGAdmin for our database. [Link](https://tecadmin.net/how-to-install-postgresql-in-ubuntu-20-04/)

```bash
#installing PostgreSQL
sudo apt install postgresql postgresql-contrib

#Swithing user, connecting to PostgreSQL and checking user name
sudo -u postgres psql
```

![image-20220131224843671](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220131224843671.png)



Now, let's add **a password to "postgres" to secure the database.**

```bash
# Adding password (mypass)
sudo passwd postgres 
```

**Then, let's switch to "postgres" account and also add a password to PostgreSQL**. After, we'll restart the service.

```bash
# Switching to postgress
su - postgres 
# Changing password
psql -c "ALTER USER postgres WITH PASSWORD 'mypass';" 
#Exiting
exit

#Restarting the service
sudo systemctl restart postgresql

```

After installing PGAdmin too, I also added a security layer to the database that requires email and password to login. Refence Tutorial from ([link](https://tecadmin.net/how-to-install-pgadmin4-on-ubuntu-20-04/)):

```bash
sudo /usr/pgadmin4/bin/setup-web.sh
```

![image-20220131234548537](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220131234548537.png)

![image-20220131235302247](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220131235302247.png)

After establishing the database connection to the app, I tested it by inserting a row.

![image-20220201142703784](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220201142703784.png)

![image-20220201142730042](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220201142730042.png)



From this, I can confirm that the connection is correct and everything is fine. After this, we created a docker image for this web app. The first container is for **the database** and the other one is **for the application.** We also have another running container of nginx server proxy. The tutorial used can be found [here](https://dev.to/destrodevshow/docker-201-use-nginx-as-a-proxy-for-nodejs-server-in-2020-practical-guide-57ji)

![image-20220203234056027](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220203234056027.png)

Now it's running on port 80 of nginx specified in the docker_compose.yml.

![image-20220203234839397](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220203234839397.png)



![image-20220203234708660](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220203234708660.png)

## Part 2: Preventing from brute-force attack

1. Screenshot with ab requests before enabling limit_req on nginx

![image-20220204023240361](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220204023240361.png)

2. Screenshot with ab after requests

After enabling the command to limit the number of departures, here's what happens: <u>The failed requests became 920</u>

```bash
limit_req_zone $binary_remote_addr zone=limit:10m rate=50r/s
```

![image-20220204023508201](/home/migor/snap/typora/46/.config/Typora/typora-user-images/image-20220204023508201.png)



## OWASP Top 10 in your own words.

This is a well-know list of vulnerabilities which are collect together each 4 years to help web developers and security experts to make sure they create secured web application. The list is organised by a company called [OWASP](https://owasp.org/www-project-top-ten/#:~:text=The%20OWASP%20Top%2010%20is,security%20risks%20to%20web%20applications.&text=Companies%20should%20adopt%20this%20document,web%20applications%20minimize%20these%20risks.)





