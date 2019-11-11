## 计算概论作业5（2019/10/8）  
#### 1.北京大学某单位的某台机器IP地址为162.105.80.160，子网掩码为255.255.255.192，问：该单位的网络号(网络+子网)是多少？该单位理论上可容纳多少主机？北大可以有多少个这样的子网（假定北大全部是162.105网段）？
该单位的网络号为 162.105.80.128 。  
理论上，该单位可以容纳 2^6-2=62 台主机。  
北大可以有1024个这样的子网。
#### 2.解释：TCP协议建立连接为什么设计为三步握手？
TCP三步握手的设计，旨在实现**可靠的**（也就是说，确保可收到）的**全双工**通信。  

* 第一步和第二步中服务端向客户端发送ACK的部分建立了从客户端到服务器传输数据的可靠连接；
* 第二步中服务端向客户端发送的SYN部分和第三步建立了从服务器到客户端传输数据的可靠连接；
* 三次握手的可靠程度可以达到可接受的水准，因此其具有合理性；
* 三次握手也具有必要性，它可以防止由网络因素导致的一些问题。假如只进行两步握手，某次客户端发出连接请求，而由于网络原因服务端并没有收到，客户端会重新发送了连接请求，完成通信。如果此时服务端收到客户端第一次发出的连接请求，将看作是一次新的连接请求，进行第二步握手，建立连接。然而此时并不会有任何数据被传送，于是该连接就会称为死连接，导致资源浪费。

#### 3.有哪些恶意软件，如何防范恶意软件？
恶意软件包括计算机病毒、蠕虫、木马、间谍软件、广告软件等。
防范恶意软件的措施包括但不限于以下几点：  

* 不下载、打开来源不明的文件或应用程序，如不可信网站上的可执行文件、不明邮件附件等
* 不以过高权限的账户操作计算机，合理设置组策略，防止可执行文件的权限过大
* 安装安全防护软件，及时安装安全更新
* 定期运行安全扫描，U盘等存储介质在打开前亦需进行安全扫描
* 不随便暴露个人信息

