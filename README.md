# ephemeral

.tech
------
ephemeral is a simple python webapp written in flask.

.purpose
--------
Share little text snippets across devices on the same network. for example, with your roommates who are likely on the same wifi. 

The webapp uses the client ip to store the text snippet, in the most common scenario the router has a public static ip and devices in the network are connected via the router. They have unique local ips but have the same public ip. ephemeral uses the public ip as a primary key to store the data.

.disclaimer/limitations
-----------------------
If a user has dynamic ip, this app will work as long as the ip is not renewed. Please note, your ip can be assigned to another user who will be able to read the text you shared. It is not recommended you use ephemeral to share any sensitive information.

The demo hosted on pythonanywhere.com doesn't support ipv6.

.features
---------
- no registration
- minimal and light
- no unique url to send to the receiver

.enhancements
-------------
- [ ] add disclaimer notice
- [ ] use an actual database to persist data
- [ ] auto-save periodically
- [ ] textpad expires after a designated timeperiod

.contribute
------------
feel free to send PRs or fork away.

.license
--------
MIT 
