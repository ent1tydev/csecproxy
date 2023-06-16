# CSECProxy ☁️ 
### (This repository no longer works because we no longer have proxy servers.)
A proxy server for Windows supported by the free CSEC community to bypass internet blockages and prevent censorship.

**Launches the built-in Windows 10 proxy server with CSEC Free settings and proxies your traffic through a secure HTTPS connection on CSEC servers.** 
Fixed a connection problem (with the inscription "Connected!" the connection does not occur). Moving from cmd to vbs for 100% connection and other minor bugs.

**The application is fully finalized.**

Attention! main.py it will not run directly as a python file in a Windows environment, since it is designed to be built via pyinstaller and contains sys._MEIPASS modules that are incompatible with direct launch via the console. To run the file, build it via pyinstaller or download the finished release in the releases tab.
