# ArtnetSender
A program to send artnet from a computer recieving artnet, to a server. 
The server recieving data has to turn of the firewall, hehe. Still working on this problem.  

Using the stupidArtnet library. 
Install with pip install stupidartnet. 
Info about stupidArtnet: https://github.com/cpvalente/stupidArtnet

I used QLC (Quick Light Controller pluss) as a lightcontroller on my computer.
Link: https://www.qlcplus.org/

This is still in work. The program is meant to be used as a sender in a raspberry pi which is connected to a grandMA 2/3, to send Artnet to a server.
The server hosts a website that changes color based on the rgb values that grandMA 2/3 sends. 


update(06.03.2023):
Follow this instruction on the computer that is hosting the server, to prevent a turning of the firewall.
https://lexisnexis.custhelp.com/app/answers/answer_view/a_id/1081611/~/adding-exceptions-to-the-windows-firewall
Anyone who knows which port you are using, are able to connect to the computer, which is not good hehe. :)
But it is better then to turn of the firewall. 
