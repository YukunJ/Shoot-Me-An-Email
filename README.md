<img src="img/email.png" alt="Logo" height="150">

<a href="https://github.com/YukunJ/Shoot-Me-An-Email"><img src="https://img.shields.io/badge/Language-Python-green.svg"/></a>

-----------------

## Shoot Me An Email

This is a small Python toy email notifier using **Gmail** and **SMTP** (Simple Mail Transfer Protocol). This is done in 30 minutes and not intended to be used for serious purposes, though it works just fine.

### Story Background

In early March, I went to Jersey City to in-person visit a few potential apartments I want to lease after graduation.

Leasing agents told me, given the 60-day move-out notice policy, lease for June will mostly be available and listed on website by end of March. Given the anticipated hot market by that time, I was advised to check the website for new listing on a regular basis.

I thought to myself: Oh, I could probably write a program to crawl for new lease listing and notify me via email.

However, after I've written the email notification component, I found that different apartment websites' HTMLs all differ dramatically. So I just gave up: I'd better just refresh the web page every few hours.

This leaves the email notifier component alone.

### How to Use It?

To use this python script to send emails, you first need an gmail account. You can go to Google website for registration, and enable two-factor authentication to retrieve an `app password`. We will use this password to login.

For safety concern, this script reads your mail server address and password from environment variables. You should do:

```console
$ export HOST_ADDR=your-email@gmail.com
$ export HOST_PWD=your-app-password
```

After this, to send an email to your friends is as easy as follows:

```python
from emailer import Emailer

if __name__ == "__main__":
    # initiate an Emailer using your email account and password
    my_emailer = Emailer()
    # add subscribers to broadcast list
    my_emailer.add_subscriber("jason@gmail.com")
    my_emailer.add_subscriber("tommy@gmail.com")
    # broadcast email, both Jason and Tommy get it
    my_emailer.broadcast_email("This is a broadcast email")
    # invididual email, only Mary gets it
    my_emailer.individual_email("mary@gmail.com", "This is an individual email")
```

The full script is only **40** lines of simple code and can be found [here](src/emailer.py) for reference.




