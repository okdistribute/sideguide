Requires:
* python2.6
* virtualenv
* mongodb


Prerequisites
-----------------------
Activate the virtualenv
<code><pre>$ virtualenv oadev <br>$ source oadev/bin/activate
</pre></code>

Install requirements
<code><pre>(oadev) $ pip install -r requirements.txt
</pre></code>

Setup Database
---------------------
Make sure mongodb is running locally 
<code><pre>$ mongo</pre></code>

Create the tables
<code><pre>$ python manage.py syncdb</pre></code>

Load test data
<code><pre>$ python manage.py runscript populate\_db</pre></code>

Start the Dev Server
--------------------------
Set up the script
<code><pre>(oadev) $ cp runserver.sh.template runserver.sh</pre></code>
Change the details of runserver.sh for your own use. 
(ie, make sure the environment variables point to the right place for you.)

Run the Development Server
<code><pre>(oadev) $ chmod +x runserver.sh <br>(oadev) $ ./runserver.sh</pre></code>
