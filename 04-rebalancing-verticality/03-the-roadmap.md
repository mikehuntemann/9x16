## The Roadmap

What can we replace on the bottom of the infrastructure to change the whole stack on top? And the following tool might be one of the possible solutions to the current mess:

**IPFS (2015)** or the "Interplanetary Filesystem" is a peer-to-peer, decentralized network and protocol for storing and sharing data in a distributed file system.

The emergence of IPFS can be seen as a bundling the biggest accomplishments of peer-to-peer software into one new protocol that is so modular and self-describing that it can be updated over time.

Like the early P2P file-sharing, IPFS uses content addressing within the network that makes every file findable, verifiable and stable throughout time. Like I already mentioned in the intro, content addressing is a cryptographic fingerprint, that is unique to each file content.

For example, a text file with "hello" in it will result in a completely different fingerprint than "Hello". And it abstracts the length of the content, so the fingerprint is always the same, no matter what content is in it. "This is a sentence." or a whole page of this will always lead to a unique 46 character content identifier:

- "hello" == QmWfVY9y3xjsixTgbd9AorQxH7VtMpzfx2HaWtsoUYecaX
- "Hello" == QmZbj5ruYneZb8FuR9wnLqJCpCXMQudhSdWhdhp5U1oPWJ
- "This is a sentence." == Qmbs5ssWcKLYDEvM8zpidqYk5S3ahHPfNLqP6z7LttNhJS

A neat side-effect is that the network doesn't have to handle redundant copies and makes this approach very efficient. This is all true for pictures and videos, documents – basically everything you throw at it. But the file is not always distributed as a whole, it gets split into 256 kB chunks of data if it is bigger than that.

If that is the case, the network splits the file into its chunks and links the different parts of the file together like this:

// Add IPFS Screenshot here from Video File Upload (Nov 26, 18:16)

The result is then again, one single content identifier build out of multiple identifiers, a simple tree, like a folder on our local filesystem.

But what can happen is "deducing": Let's say you make a copy of the file and apply minor changes to it. Most of the content will stay the same, therefore the content within the chunks can be the same. In this case it is possible that both of the files will share the same chunks with each other build different images. Everything is a set of one that can be combined through the different IDs.

> “Imagine, if I store this article on IPFS, and it’s each letter in chunked and has a unique CID, then this whole article can be constructed by just a combination of alphabets(capital and small), number and some special characters. We will only store every alphabet, number, and character only ONCE and rearrange it according to the Links in the data structure. This is powerful stuff…” – [Vaibhav Saini](https://web.archive.org/web/20190816194557/https://hackernoon.com/understanding-ipfs-in-depth-1-5-a-beginner-to-advanced-guide-e937675a8c8a)

This is the real atomization and fragmentation I am talking about which almost sounds like the [Library of Babel](https://web.archive.org/web/20190826061822/https://en.m.wikipedia.org/wiki/The_Library_of_Babel).
Ultimately, this is the "Move to the Ocean".  





Enabling the distributed web
https://medium.com/textileio/enabling-the-distributed-web-abf7ab33b638
Whoever controls the location serves what the people are going to see.

Websites became less important on mobile, instead we get these little packages of pre-structured data that fill the design preset within the app, e.g. a tweet, or a post. > and this is all json, a data format which is commonly used within server-client communication.

Most of the internet dies within a 100 days, except the seemingly stable internet platforms.

This whole process abstracts the filesystem from the user.
“We traded convenience for control.”

Content addressing changes the “where” to “what”.
So how does it work? You create a unique, content-based fingerprint of your file. And this concept isn’t new. I used it as a child, 15 years ago, while I was participating in peer-to-peer file sharing.
Different protocol now but functions similar: you ask the network for the content ID and the network will find other people that have that identical piece of content. Now, you are downloading the file from multiple people in parallel instead of one single distributor of the content and authority.

peer-to-peer is inevitable because it will be the most cost-efficient variant of information exchange:
p2p: costs = (filesize / customer) x cost-per-byte
CDNs: costs = filesize x customer x cost-per-byte   

But there will be hybrids for sure.


CIDs are stable and don’t change over time. (Persistent data structure https://en.wikipedia.org/wiki/Persistent_data_structure)
This way you can implement files into your project and become part of preserving the data over time. This way, if I find something valuable on the web or in my media archeological project, collaborators or other people can help to keep the project itself, or assets of it alive. > you can not duplicate the files the network! There are no identical duplicates.

In the end, we dont need huge databases as a single point of authority or failure to mange and distribute the data. We can do It on our own.

https://hackernoon.com/a-beginners-guide-to-ipfs-20673fedd3f


1 picture to chunks of raw data, which get through a hash function, which then turn into a collection of CIDs that are then hashed together for the “base CID”, which is the file with all of its components.

You can also link your data (IPLD)
DAGs are simple link-based graphs > like a tree, a erected acyclic graph (like my knowledge graph)
https://en.wikipedia.org/wiki/Directed_acyclic_graph

Every 12 hours you have to tell the network, that you can provide the CID or you are out of the peer list

https://youtu.be/fLUq0RkiTBA?t=3440
“Pinning is local, I pin to my machine”
“Deleting is local”, “once you send it, its gone.”
