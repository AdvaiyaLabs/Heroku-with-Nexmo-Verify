# Heroku with Nexmo Verify
<img src="https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify/blob/master/docs/image1.png" width=100>

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Introduction

In today’s digital world where data is under constant attack, passwords may get compromised through techniques like phishing, keystroke logging and brute force. In such scenarios, Two-Factor Authentication (2FA) via SMS is an efficient way to verify user access. As every country has its own communication compliance rules and regulations, so implementing 2FA functionality via SMS at a global scale becomes challenging for the developers.

To implement 2FA via SMS on a global scale over Heroku platform successfully, the developer community can use the **Heroku with Nexmo Verify** app that uses Nexmo Messaging APIs for user verification. This app can be deployed and integrated easily with any available programming languages for the phone verification and One-time-password (OTP).

## Use Case

Enable Heroku developer community to implement Two Factor Authentication (2FA) services via SMS using Nexmo messaging APIs, so they can easily deploy and integrate it with any platform (C\#, Java, PHP).

## Prerequisites

-   Heroku subscription

-   Nexmo subscription and corresponding Nexmo API keys (Keys and Secret). To access the API keys, see the appendix section.

-   Make sure the provided information in configuration setting (Nexmo Key, Secret, etc.) are correct.

## Features 

-   Phone number verification using the SMS

-   Easy integration with any application

-   Simple deployment as it requires less configuration

## Steps to deploy Heroku with Nexmo Verify

1.  Login to Heroku platform.

2.  To setup Heroku with Nexmo Verify app, go to GitHub Repository: 

[```https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify.git```](https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify.git)

3.  Click on **Deploy to Heroku** button. This will start the installation on Heroku under your subscription.

4.  Set an application name.

    <img src="https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify/blob/master/docs/image4.png" width=400>

5.  Select a region where the application will deploy. By default, it is United States.

    <img src="https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify/blob/master/docs/image5.png" width=400>

6.  Set the Nexmo application variable to send the SMS as shown below:

    <img src="https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify/blob/master/docs/image6.png" height=400>

    - Extract the API and SECRET key from the Nexmo site. See the Appendix.

    - VERIFY\_DURATION: The sent code will be valid for just some minutes given in the VERIFY\_DURATION variable.

    - Click on **Deploy for Free** button to start the application.

7.  After successfully deploying, it shows two different buttons - **Manage App** and **View**.

8.  Click on **View** and copy the URL for further use.

## Steps to use the Heroku with Nexmo Verify


While developing Heroku application using the above generated URL, you can apply the 2FA functionality.

1.  Use the following URL in your application to send the verification code:

     [```http://<heroku-app-url>/verify?dst=>phone_with_country_code>```](http://&lt;heroku-app-url&gt;/verify?dst=&lt;phone_with_country_code&gt;)

    - Replace the **&lt;heroku-app-url&gt;** with your **Heroku public URL.**

    - **Verify** will return a request id in JSON format and extract that **request id** for further use.

    - **dst** parameter is a destination phone number with country code to send the verification code. Replace the **&lt;phone\_with\_country\_code&gt;** with the destination phone number.

    - This will send the OTP to the respective user.


2.  Submit the received OTP.

3.  To authenticate the **OTP** and **request id,** use the following URL:

    [```http://<heroku-app-url>/validate?code=<Mobile received code>&req_id=<request_id>```](http://&lt;heroku-app-url&gt;/validate?code=&lt;Mobile received code&gt;&req_id=&lt;request_id&gt;)

    - Replace the **&lt;heroku-app-url&gt;** with your **Heroku public URL.**

    - Replace the **&lt;request\_id&gt;** to the request you get in your response.

    - Replace the **&lt;Mobile received code&gt;** with user entered OTP code, which he/she received on his/her phone as SMS.

    - Send request on **validate** end point with code and request id query string.

    - Returns JSON with a message and status (like if it is 0 that means successfully validated).

## Check the status of request


To search requests' status that are terminated, still running or completed, use the following URL:

   [```http://<heroku-app-url>/status? req_id=<request_id>```](http://&lt;heroku-app-url&gt;/status?req_id=&lt;request_id&gt;)

   1.  Replace the **&lt;heroku-app-url&gt;** with your **Heroku public URL.**

   2.  Replace the **&lt;request\_id&gt;** to the request you get in your response.

   3.  Send request on **status** end point with request id query string.

   4.  Return the JSON of status information.

## Steps to update the Heroku with Nexmo Verify app settings


1.  To update the application variables, select Nexmo application from Heroku Dashboard.

    <img src="https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify/blob/master/docs/image7.png" width=400>

2.  Click on **Settings** and then click the **Reveal Config Vars**.

    <img src="https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify/blob/master/docs/image8.png" width=400>

3.  Click on the Edit icon as shown below to update the variables. 
    
	<img src="https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify/blob/master/docs/image9.png" width=400>

4.  On the **Edit config variable**, a popup will be displayed. Update data and click on **Save changes**.

    <img src="https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify/blob/master/docs/image10.png" width=400>

## Appendix


### Nexmo API Keys


-   To access Nexmo keys, go to <https://www.nexmo.com/> and sign-in.

-   On the top right corner, click on the **Api Settings.**

-   Key and Secret will display in the top bar as shown in the below image:

<img src="https://github.com/AdvaiyaLabs/Heroku-with-Nexmo-Verify/blob/master/docs/image11.png">
