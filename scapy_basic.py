import scapy

ip_packet = IP()


ls(ip_packet) # ls는 IP 클래스에서 가진 멤버들 확인, dir은 메소드들도 모두 확인

'''
version    : BitField (4 bits)                   = 4               (4)
ihl        : BitField (4 bits)                   = None            (None)
tos        : XByteField                          = 0               (0)
len        : ShortField                          = None            (None)
id         : ShortField                          = 1               (1)
flags      : FlagsField (3 bits)                 = <Flag 0 ()>     (<Flag 0 ()>)
frag       : BitField (13 bits)                  = 0               (0)
ttl        : ByteField                           = 64              (64)
proto      : ByteEnumField                       = 0               (0)
chksum     : XShortField                         = None            (None)
src        : SourceIPField                       = '127.0.0.1'     (None)
dst        : DestIPField                         = '127.0.0.1'     (None)
options    : PacketListField                     = []              ([])
'''



ip_packet.version = 4
ip_packet.src = '150.23.27.27'
ip_packet.dst = 'google.com'
ip_packet.ttl = 10



'''
Command	Effect
raw(pkt)	assemble the packet
hexdump(pkt)	have a hexadecimal dump
ls(pkt)	have the list of fields values
pkt.summary()	for a one-line summary
pkt.show()	for a developed view of the packet
pkt.show2()	same as show but on the assembled packet (checksum is calculated, for instance)
pkt.sprintf()	fills a format string with fields values of the packet
pkt.decode_payload_as()	changes the way the payload is decoded
pkt.psdump()	draws a PostScript diagram with explained dissection
pkt.pdfdump()	draws a PDF with explained dissection
pkt.command()	return a Scapy command that can generate the packet

pkt.summary()	displays a list of summaries of each packet
pkt.nsummary()	same as previous, with the packet number
pkt.conversations()	displays a graph of conversations
pkt.show()	displays the preferred representation (usually nsummary())
pkt.filter()	returns a packet list filtered with a lambda function
pkt.hexdump()	returns a hexdump of all packets
pkt.hexraw()	returns a hexdump of the Raw layer of all packets
pkt.padding()	returns a hexdump of packets with padding
pkt.nzpadding()	returns a hexdump of packets with non-zero padding
pkt.plot()	plots a lambda function applied to the packet list
pkt.make table()	displays a table according to a lambda function
'''


ip_packet.summary()
'''
"150.23.27.27 > Net('google.com') ip"
'''

ip_packet.show()
'''
###[ IP ]###
  version= 4
  ihl= None
  tos= 0x0
  len= None
  id= 1
  flags=
  frag= 0
  ttl= 10
  proto= ip
  chksum= None
  src= 150.23.27.27
  dst= Net('google.com')
  \options\
'''

ip_packet.show2()
'''
###[ IP ]###
  version= 4
  ihl= 5
  tos= 0x0
  len= 20
  id= 1
  flags=
  frag= 0
  ttl= 10
  proto= ip
  chksum= 0x8411
  src= 150.23.27.27
  dst= 172.217.25.206
  \options\
'''

ip_packet.display()
'''
###[ IP ]###
  version= 4
  ihl= None
  tos= 0x0
  len= None
  id= 1
  flags=
  frag= 0
  ttl= 10
  proto= ip
  chksum= None
  src= 150.23.27.27
  dst= Net('google.com')
  \options\
>>>
'''

ip_packet.route()
'''
('eno1', '150.23.27.27', '150.23.27.1')
'''

ip_packet.whois()
'''
% The RIPE Database is subject to Terms and Conditions.
% See http://www.ripe.net/db/support/db-terms-conditions.pdf

% Note: this output has been filtered.
%       To receive output for a database update, use the "-B" flag.

% Information related to '172.16.0.0 - 172.31.255.255'

% No abuse contact registered for 172.16.0.0 - 172.31.255.255

inetnum:        172.16.0.0 - 172.31.255.255
netname:        IETF-RESERVED-ADDRESS-BLOCK
descr:          IPv4 address block reserved by the IETF
country:        EU # Country is really world wide
org:            ORG-IANA1-RIPE
admin-c:        IANA1-RIPE
tech-c:         IANA1-RIPE
status:         ALLOCATED UNSPECIFIED
mnt-by:         RIPE-NCC-HM-MNT
created:        2014-11-07T14:27:58Z
last-modified:  2014-11-07T14:38:18Z
source:         RIPE

organisation:   ORG-IANA1-RIPE
org-name:       Internet Assigned Numbers Authority
org-type:       IANA
address:        see http://www.iana.org
admin-c:        IANA1-RIPE
tech-c:         IANA1-RIPE
mnt-ref:        RIPE-NCC-HM-MNT
mnt-by:         RIPE-NCC-HM-MNT
created:        2004-04-17T09:57:29Z
last-modified:  2013-07-22T12:03:42Z
source:         RIPE # Filtered

role:           Internet Assigned Numbers Authority
address:        see http://www.iana.org.
admin-c:        IANA1-RIPE
tech-c:         IANA1-RIPE
nic-hdl:        IANA1-RIPE
mnt-by:         RIPE-NCC-MNT
created:        1970-01-01T00:00:00Z
last-modified:  2001-09-22T09:31:27Z
source:         RIPE # Filtered
% This query was served by the RIPE Database Query Service version 1.92.6 (HEREFORD)

>>>
'''


ip_packet2 = IP(dst="youtube.com")

IP(_) # "_"의미는 가장최근 패킷결과를 의미
#Each packet can be build or dissected (note: in Python _ (underscore) is the latest result):


ping_packet = ip_packet2/ICMP()


'''
send(x, inter=0, loop=0, count=None, verbose=None, realtime=None, return_packets=False, socket=None, *args, **kargs)
    Send packets at layer 3
    send(packets, [inter=0], [loop=0], [count=None], [verbose=conf.verb], [realtime=None], [return_packets=False],  # noqa: E501
         [socket=None]) -> None
(END)
'''


send(ping_packet)
'''
>>> send(ping_packet)
.
Sent 1 packets.
'''

send(ping_packet, iface="eno1")




sendp()
'''
sendp(x, inter=0, loop=0, iface=None, iface_hint=None, count=None, verbose=None, realtime=None, return_packets=False, socket=None, *args, **kargs)
    Send packets at layer 2
    sendp(packets, [inter=0], [loop=0], [iface=None], [iface_hint=None], [count=None], [verbose=conf.verb],  # noqa: E501
          [realtime=None], [return_packets=False], [socket=None]) -> None
'''



'''
add_payload
add_underlayer
aliastypes
answers
build
build_done
build_padding
build_ps
canvas_dump
chksum
class_default_fields
class_default_fields_ref
class_dont_cache
class_fieldtype
class_packetfields
clear_cache
clone_with
command
copy
copy_field_value
copy_fields_dict
decode_payload_as
default_fields
default_payload_class
delfieldval
direction
display
dissect
dissection_done
do_build
do_build_payload
do_build_ps
do_dissect
do_dissect_payload
do_init_cached_fields
do_init_fields
dst
explicit
extract_padding
fields
fields_desc
fieldtype
firstlayer
flags
frag
fragment
from_hexcap
get_field
getfield_and_val
getfieldval
getlayer
guess_payload_class
hashret
haslayer
hide_defaults
hops
id
ihl
init_fields
lastlayer
layers
len
lower_bonds
mysummary
name
options
original
ottl
overload_fields
overloaded_fields
packetfields
payload
payload_guess
pdfdump
post_build
post_dissect
post_dissection
post_transforms
pre_dissect
prepare_cached_fields
proto
psdump
raw_packet_cache
raw_packet_cache_fields
remove_payload
remove_underlayer
route
self_build
sent_time
setfieldval
show
show2
show_indent
show_summary
sniffed_on
sprintf
src
summary
svgdump
time
tos
ttl
underlayer
upper_bonds
version
whois
wirelen
'''