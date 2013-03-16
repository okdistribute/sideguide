Requires:
* python2.6+
* virtualenv
* postgresql
* postgis


Prerequisites
-----------------------
Install virtualenv. Use the following command:
<code><pre>$ virtualenv sandbox <br>$ source sandbox/bin/activate
</pre></code>

Install requirements
<code><pre>(sandbox) $ pip install -r requirements.txt
</pre></code>

Start the Dev Server
--------------------------
Set up the script
<code><pre>(sandbox) $ cp runserver.sh.template runserver.sh</pre></code>
Change the details of runserver.sh for your own use. 
(ie, make sure the variables point to the right place for you.)

Run the Development Server
<code><pre>(sandbox) $ chmod +x runserver.sh <br>(sandbox) $ ./runserver.sh</pre></code>
