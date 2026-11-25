# Mission 7 — How computers communicate

## 1. Task / objective
The goal of Mission 7 was to investigate the principles of computer networking and telecommunications. This required analyzing core network classifications (LAN, MAN, WAN), network architecture concepts (DNS, IP addressing, routers, network protocols, packet switching, and client-server systems), executing live terminal network diagnostics (`ping` and `nslookup`) to measure latency and inspect DNS resolution records, and detailing the end-to-end lifecycle of a web request when loading a website in a browser.

## 2. Work completed

### Task 7.1 — Explain network concepts

| Networking Concept | Clear Explanation in My Own Words | Real-World Concrete Example |
| :--- | :--- | :--- |
| **LAN** (Local Area Network) | A computer network confined to a restricted geographic footprint, such as a single residence, university laboratory, or office suite, typically connected via Wi-Fi or Ethernet switches with high throughput and low latency. | The local Wi-Fi network connecting laptops, smartphones, and printers inside my university dormitory or home. |
| **MAN** (Metropolitan Area Network) | A high-bandwidth telecommunications network spanning an entire town, municipality, or large multi-campus educational institution, interconnecting multiple LANs. | A municipal fiber-optic network connecting all public libraries, administrative civic buildings, and police headquarters across a city. |
| **WAN** (Wide Area Network) | A telecommunications network spanning large geographical distances (states, nations, or continents), formed by interconnecting millions of smaller networks via transoceanic fiber cables and satellite relays. | The global Internet, connecting billions of devices across the planet. |
| **DNS** (Domain Name System) | The distributed directory service that translates human-readable domain names (such as `example.com`) into machine-routable numerical IP addresses (such as `172.66.147.243`). | The digital "contacts directory" or "phonebook" of the Internet. |
| **Router** | A specialized network layer hardware appliance that examines incoming data packets and forwards them across interconnected networks toward their destination IP using dynamic routing tables. | The home Wi-Fi gateway device routing traffic between local home devices and the Internet Service Provider's (ISP) central office. |
| **Network Protocol** | An agreed-upon set of standardized rules, message formats, and timing constraints governing how networked devices exchange data reliably without misunderstanding. | **HTTPS** (Hypertext Transfer Protocol Secure) governing secure web traffic, or **TCP/IP** managing packet transmission. |
| **Packet Switching** | The networking paradigm where data is fragmented into small, self-contained chunks called *packets* (each containing source IP, destination IP, payload, and sequence number) routed independently across shared network links. | Streaming a 4K movie where video segments are split into thousands of individual IP packets that take diverse network paths and are reassembled at the receiver. |
| **Client-Server Architecture** | A distributed computing model where service requesters (*clients*, such as a web browser) initiate requests for resources, and dedicated centralized hosts (*servers*) listen for, process, and respond to those requests. | A mobile phone (client) requesting an account balance from a bank's central mainframe server over an API. |

---

### Task 7.2 — Observe network information
To inspect real-world network operations, I executed standard diagnostic commands in the terminal targeting `example.com` (a standardized, privacy-safe domain designated by IANA for documentation and testing).

#### 1. Connectivity and Latency Diagnostics (`ping -c 3 example.com`)
```
PING example.com (172.66.147.243): 56 data bytes
64 bytes from 172.66.147.243: icmp_seq=0 ttl=58 time=55.015 ms
64 bytes from 172.66.147.243: icmp_seq=1 ttl=58 time=14.094 ms
64 bytes from 172.66.147.243: icmp_seq=2 ttl=58 time=48.461 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 14.094/39.190/55.015/17.946 ms
```

#### 2. Domain Name Resolution Diagnostics (`nslookup example.com`)
```
Server:     8.8.8.8
Address:    8.8.8.8#53

Non-authoritative answer:
Name:       example.com
Address:    172.66.147.243
Name:       example.com
Address:    104.20.23.154
```

#### Questions and answers:
- **What is latency, and what was your observed round-trip time?**  
  **Latency** is the time delay required for a data packet to travel from the source host to the destination and return back (Round-Trip Time, RTT). In my test run, the average round-trip latency to `example.com` was **`39.190 ms`** (with a minimum of `14.094 ms` and maximum of `55.015 ms`).
- **What does `0.0% packet loss` indicate?**  
  It indicates that all 3 transmitted ICMP echo request packets successfully reached the destination host, were acknowledged, and returned without any data packets being dropped or discarded along the intervening physical routing path.
- **Why did `nslookup` return multiple IP addresses (`172.66.147.243` and `104.20.23.154`)?**  
  Major public domains utilize DNS Anycast and load balancing across globally distributed Content Delivery Networks (CDNs) or server clusters. Returning multiple IP addresses allows client traffic to be distributed across redundant servers, preventing server overload and ensuring continuous availability if one IP goes offline.
- **What is the meaning of `Server: 8.8.8.8#53`?**  
  `8.8.8.8` is Google's Public DNS resolver, and `#53` denotes standard UDP Port 53, the internationally assigned port number for DNS queries.

---

### Task 7.3 — What happens when you open a website?
When a user enters a URL such as `https://www.example.com` into a web browser address bar and presses Enter, an orchestrated multi-stage sequence unfolds across the network stack in milliseconds:

1. **URL Parsing & Local Cache Inspection**:
   - The browser parses the protocol (`https://`), domain hostname (`www.example.com`), and path.
   - It checks hierarchical local caches to see if the IP address is already known:
     1. Browser DNS cache.
     2. Operating system DNS resolver cache (`/etc/hosts`).
     3. Local router gateway cache.

2. **Recursive DNS Resolution**:
   - If not cached, the OS dispatches a DNS query to the configured recursive DNS resolver (e.g., ISP resolver or `8.8.8.8`).
   - The resolver queries the Root DNS Nameserver (`.`), which directs it to the Top-Level Domain (TLD) Nameserver (`.com`).
   - The `.com` TLD nameserver directs the resolver to the Authoritative Nameserver for `example.com`.
   - The authoritative nameserver returns the host's IP address (e.g. `172.66.147.243`) to the recursive resolver, which caches it and returns it to the client OS.

3. **TCP Three-Way Handshake**:
   - The client browser initiates a reliable Transport Layer connection with the destination server on TCP Port 443:
     - **SYN**: Client sends a SYN (Synchronize) packet with an initial sequence number.
     - **SYN-ACK**: Server acknowledges with a SYN-ACK packet.
     - **ACK**: Client acknowledges with an ACK packet.
   - The full-duplex TCP socket connection is now established.

4. **TLS/SSL Cryptographic Handshake**:
   - Because the protocol is HTTPS, an encrypted TLS session is negotiated:
     - Client and server exchange supported cipher suites and random nonces (ClientHello / ServerHello).
     - The server presents its digital X.509 certificate signed by a trusted Certificate Authority (CA).
     - The client verifies the certificate validity and expiration.
     - Using asymmetric cryptography (e.g., ECDHE), both parties agree on a shared symmetric session encryption key, establishing end-to-end encryption.

5. **HTTP Request Transmission**:
   - The browser formats and transmits an encrypted HTTP GET request:
     ```http
     GET / HTTP/1.1
     Host: www.example.com
     User-Agent: Mozilla/5.0 ...
     Accept: text/html
     ```

6. **Server Processing and HTTP Response**:
   - The remote web server (such as Nginx or Apache) receives the request, routes it through application handlers, and transmits an HTTP response payload:
     ```http
     HTTP/1.1 200 OK
     Content-Type: text/html; charset=UTF-8
     Content-Length: 1256
     
     <!doctype html><html>...</html>
     ```

7. **Browser Rendering Pipeline**:
   - The browser engine parses the incoming HTML byte stream into a **Document Object Model (DOM)** tree.
   - It parses CSS rules into a **CSS Object Model (CSSOM)** tree.
   - Combining DOM and CSSOM, it constructs the **Render Tree**, computes geometrical layout coordinates for all visible elements (Layout/Reflow), and paints colored pixels onto the display surface (Painting & Compositing).

---

## 3. Commands / tools used
- `ping -c 3 example.com` (ICMP network latency diagnostic)
- `nslookup example.com` (DNS name resolution query)
- Terminal and network diagnostic utilities.

## 4. My understanding
Computer networking relies on layered abstractions (the OSI 7-Layer model and TCP/IP stack). Each layer performs an isolated job: physical cables and radio waves transmit electrical signals, the IP layer routes packets across networks, TCP ensures reliable delivery without dropped bytes, TLS encrypts communication against eavesdroppers, and HTTP structures application content.

Without packet switching and DNS, the modern Internet could not scale. Dividing communications into addressed packets routed dynamically prevents single points of failure, while DNS transforms unmemorable numerical IP matrices into human-accessible domain names.

## 5. Difficulties faced
Understanding why `ping` utilizes ICMP (Internet Control Message Protocol) instead of standard TCP or UDP ports.

## 6. How I resolved them
I researched network protocol specifications and discovered that ICMP operates as an auxiliary network-layer protocol designed specifically for diagnostic reporting and error notification, which is why `ping` measures network reachability without establishing a TCP application socket connection.

## 7. Evidence / files
- Real diagnostic logs recorded from `ping` and `nslookup`.
- `mission-07-networking/README.md`.

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Branch: `main`
