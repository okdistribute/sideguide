Requires:
* python2.6
* virtualenv
* mongodb
* django


Starting the Dev Server
--------------------------
Activate the virtualenv
<code><pre>$ source oadev/bin/activate
</pre></code>

Set up the script
<code><pre>$ cp runserver.sh.template runserver.sh</pre></code>
Change the details of runserver.sh for your own use. 
(ie, make sure the environment variables point to the right place for you.)

Run the Development Server
<code><pre>$ chmod +x runserver.sh.template <br>$ ./runserver.sh</pre></code>
