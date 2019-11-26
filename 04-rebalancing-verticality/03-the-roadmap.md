## The Roadmap

What can we replace on the bottom of the infrastructure to change the whole stack on top? And the following tool might be one of the possible solutions to the current mess:

**IPFS (2015)** or the "Interplanetary Filesystem" is a peer-to-peer, decentralized network and protocol for storing and sharing data in a distributed file system.

As a participant in the network, you can attach your own IPFS node to it, which will provide others with the content you are hosting. In 2020, this will be extended by "Filecoin", a crypto-currency that pays the participants for providing online storage for others.

The emergence of IPFS can be seen as a bundling the biggest accomplishments of peer-to-peer software into one new protocol that is so modular and self-describing that it can be updated over time.

Like the early P2P file-sharing, IPFS uses content addressing within the network that makes every file findable, verifiable and stable throughout time. As I mentioned in the intro, content addressing is a cryptographic fingerprint, that is unique to each file content.

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
