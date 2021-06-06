# pingOS
Small Python utility that pings a specific IP address and parses its TTL to determine what operating system it has.

Every OS has a different TTL for their ICMP packets, so we can use that value to determine the host's operating system.
<br>
But that value can be changed so this method of judgment <b>is not necessarily accurate</b>.
