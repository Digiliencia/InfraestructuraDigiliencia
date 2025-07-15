// Match existing organization node
MATCH (o:Organization {name: "INCIBE"})

// Create topics and their relationships to the organization
CREATE
  (adware:Topic
    {
      name: "Adware",
      definition:
        "Software or program that displays some kind of unwanted or misleading advertising from websites or with the installation of some program. Their aim is to obtain some economic benefit or even to store private information.",
      url: "https://www.incibe.es/aprendeciberseguridad/adware"
    })-
    [:SOURCE]->
  (o),
  (botnet:Topic
    {
      name: "Botnet",
      definition:
        "A collection of computers, called bots, infected with a type of malware that are remotely controlled by an attacker and can be used together to perform malicious activities.",
      url: "https://www.incibe.es/aprendeciberseguridad/botnet"
    })-
    [:SOURCE]->
  (o),
  (cyberbullying:Topic
    {
      name: "Cyberbullying",
      definition:
        "Type of harassment in which digital media are used to harm the victim, consciously and repeatedly over time.",
      url: "https://www.incibe.es/aprendeciberseguridad/cyberbullying"
    })-
    [:SOURCE]->
  (o),
  (cybersquatting:Topic
    {
      name: "Cybersquatting",
      definition:
        "Domain name hijacking consists of registering a specific domain name that mimics a legitimate one, later using it for fraudulent purposes.",
      url: "https://www.incibe.es/aprendeciberseguridad/cybersquatting"
    })-
    [:SOURCE]->
  (o),
  (deepfake:Topic
    {
      name: "Deepfake",
      definition:
        "Videos and other media manipulated to make users believe that they see a certain person, whether anonymous or a public figure, making statements or performing actions that never happened. To create such videos, tools or programmes equipped with artificial intelligence technology are used that allow the exchange of faces in images and the modification of the voice.",
      url: "https://www.incibe.es/aprendeciberseguridad/deepfakes"
    })-
    [:SOURCE]->
  (o),
  (defacement:Topic
    {
      name: "Defacement",
      definition:
        "A type of attack against a website, in which the appearance of some of its pages is modified in order to carry out some type of fraudulent or vandalistic action.",
      url: "https://www.incibe.es/aprendeciberseguridad/defacement"
    })-
    [:SOURCE]->
  (o),
  (grooming:Topic
    {
      name: "Grooming",
      definition:
        "A practice in which an adult impersonates a minor on the Internet or attempts to establish contact with children and adolescents in order to establish a relationship of trust, moving on to emotional control and, finally, to blackmail for sexual purposes.",
      url: "https://www.incibe.es/aprendeciberseguridad/grooming"
    })-
    [:SOURCE]->
  (o),
  (jailbreaking:Topic
    {
      name: "Jailbreaking",
      definition:
        "A process that removes the limitations imposed by Apple on an iOS device. Once ‘unlocked’ it will be possible, for example, to install third-party apps that are not on the AppStore.",
      url: "https://www.incibe.es/aprendeciberseguridad/jailbreaking-rooting"
    })-
    [:SOURCE]->
  (o),
  (malvertising:Topic
    {
      name: "Malvertising",
      definition:
        "A technique that consists of manipulating online advertisements with the aim of infecting devices. Thus, when the user accesses one of these advertisements, he or she installs malicious software without being aware of it.",
      url: "https://www.incibe.es/aprendeciberseguridad/malvertising"
    })-
    [:SOURCE]->
  (o),
  (malware:Topic
    {
      name: "Malware",
      definition:
        "A computer program (software) whose main characteristic is that it runs without the knowledge or authorisation of the owner or user of the infected computer and performs functions on the system that are harmful to the user and/or the system.",
      url: "https://www.incibe.es/aprendeciberseguridad/malware"
    })-
    [:SOURCE]->
  (o),
  (maninthemiddle:Topic
    {
      name: "Man-in-the-middle",
      definition:
        "Is the interception of communication between a sender and a receiver, which can eavesdrop or modify the information for malicious purposes.",
      url: "https://www.incibe.es/aprendeciberseguridad/man-in-the-middle"
    })-
    [:SOURCE]->
  (o),
  (pentesting:Topic
    {
      name: "Pentesting",
      definition:
        "Also known as penetration testing, it consists of simulating an attack on a software or hardware system to identify vulnerabilities and prevent external attacks.",
      url: "https://www.incibe.es/aprendeciberseguridad/pentesting"
    })-
    [:SOURCE]->
  (o),
  (phishing:Topic
    {
      name: "Phishing",
      definition:
        "A technique in which a cybercriminal sends an email to a user while pretending to be a legitimate entity (such as a social network, bank, or public institution) with the goal of stealing private information, making an unauthorized charge, or infecting the device.",
      url: "https://www.incibe.es/aprendeciberseguridad/phishing"
    })-
    [:SOURCE]->
  (o),
  (pretexting:Topic
    {
      name: "Pretexting",
      definition:
        "It is the foundation of any social engineering attack. It consists of creating and developing a fictitious scenario or story, where the attacker will try to make the victim share information that they would not normally disclose.",
      url: "https://www.incibe.es/aprendeciberseguridad/pretexting"
    })-
    [:SOURCE]->
  (o),
  (ransomware:Topic
    {
      name: "Ransomware",
      definition:
        "Malware that takes complete control of the computer by locking or encrypting the user's information and then demanding money in exchange for unlocking or decrypting the files on the device.",
      url: "https://www.incibe.es/aprendeciberseguridad/ransomware"
    })-
    [:SOURCE]->
  (o),
  (rooting:Topic
    {
      name: "Rooting",
      definition:
        "A process to gain root access to the device, i.e. to obtain ‘superuser’ or administrator permissions to access the system without any kind of restriction. It will be possible, for example, to give administrator permissions to an application, which will allow it to uninstall other apps or remove permissions.",
      url: "https://www.incibe.es/aprendeciberseguridad/jailbreaking-rooting"
    })-
    [:SOURCE]->
  (o),
  (sexting:Topic
    {
      name: "Sexting",
      definition:
        "The risky practice of sending self-produced photographs or videos with sexual connotations via mobile phone or other internet-connected device.",
      url: "https://www.incibe.es/aprendeciberseguridad/sexting"
    })-
    [:SOURCE]->
  (o),
  (sextorsion:Topic
    {
      name: "Sextorsion",
      definition:
        "A form of blackmail in which the attacker threatens the victim to carry out a specific action in order to prevent the public release of sexually explicit images or videos that the victim has previously sent.",
      url: "https://www.incibe.es/aprendeciberseguridad/sextorsion"
    })-
    [:SOURCE]->
  (o),
  (smishing:Topic
    {
      name: "Smishing",
      definition:
        "A technique that consists of a cybercriminal sending an SMS to a user pretending to be a legitimate entity - social network, bank, public institution, etc. -with the aim of stealing private information or making a financial charge. Usually the message invites the user to call a premium rate number or access a link to a fake website under a pretext.",
      url: "https://www.incibe.es/aprendeciberseguridad/smishing"
    })-
    [:SOURCE]->
  (o),
  (socialengineering:Topic
    {
      name: "Social engineering",
      definition:
        "Technique used by cybercriminals to gain the user's trust and get them to do something under their manipulation and deception, such as running a malicious programme, providing their private passwords or buying from fraudulent websites.",
      url: "https://www.incibe.es/aprendeciberseguridad/social-engineering"
    })-
    [:SOURCE]->
  (o),
  (spearphishing:Topic
    {
      name: "Spear phishing",
      definition:
        "A targeted phishing scheme, in which the attackers attempt, via an email, to obtain confidential information from the victim.",
      url: "https://www.incibe.es/aprendeciberseguridad/spear-phishing"
    })-
    [:SOURCE]->
  (o),
  (spyware:Topic
    {
      name: "Spyware",
      definition:
        "Type of malware that collects information from a computer and then sends it to a remote entity without the computer owner's knowledge or consent.",
      url: "https://www.incibe.es/aprendeciberseguridad/spyware"
    })-
    [:SOURCE]->
  (o),
  (typosquatting:Topic
    {
      name: "Typosquatting",
      definition:
        "A phenomenon whereby a user ends up on a website that is not the one they were looking for by mistakenly mistyping the URL in their browser. Cybercriminals often take advantage of this situation to take the user to a malicious website by reserving domains similar to legitimate ones.",
      url: "https://www.incibe.es/aprendeciberseguridad/typosquatting"
    })-
    [:SOURCE]->
  (o),
  (vishing:Topic
    {
      name: "Vishing",
      definition:
        "Social engineering scam by telephone in which, through a phone call, the identity of a company, organisation or trusted person is impersonated in order to obtain personal and sensitive information from the victim.",
      url: "https://www.incibe.es/aprendeciberseguridad/vishing"
    })-
    [:SOURCE]->
  (o),
  (vulnerability:Topic
    {
      name: "Vulnerability",
      definition:
        "Technical failure or deficiency in a programme that may allow a non-legitimate user to access information or carry out unauthorised operations remotely.",
      url: "https://www.incibe.es/aprendeciberseguridad/vulnerabilidad"
    })-
    [:SOURCE]->
  (o),
  (warshipping:Topic
    {
      name: "Warshipping",
      definition:
        "Type of attack, in which a package is sent to a company, which includes electronic devices inside, and after connecting them to a computer in the organisation, information could be stolen.",
      url: "https://www.incibe.es/aprendeciberseguridad/warshipping"
    })-
    [:SOURCE]->
  (o)