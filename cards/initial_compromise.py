initial_compromise = [
    {
        "Title": "MISSING HTTP STRICT TRANSPORT SECURITY (HSTS) PROTECTION",
        "Description": 'By having HTTP to HTTPS redirects, the attackers can "strip" SSL from a session. The attackers need to be on the same network for this to work. So, think coffee shops... evil, coffee shops.',
        "Detection": [
            "Firewall Log Review",
            "NETFLOW, ZEEK/BRO, REAL INTELLIGENCE THREAT ANALYTICS (RITA) ANALYSIS",
        ],
        "Tools": "SSLStrip SSLSplit",
        "Documentation": "https://github.com/droe/ss|split https://github.com/moxie0/ss|strip",
    },
    {
        "Title": "SUPPLY CHAIN ATTACK",
        "Description": "The attackers insert malware in the update process of one of your key enterprise management tools. This gives them direct access to the heart of your infrastructure.",
        "Detection": [
            "Endpoint Security Protection Analysis",
            "Endpoint Analysis",
            "NETFLOW, ZEEK/BRO, REAL INTELLIGENCE THREAT ANALYTICS (RITA) ANALYSIS",
        ],
        "Tools": "SUNBURST SUPERNOVA",
        "Documentation": "https://krebsonsecurity.com/2020/12/solarwinds-hack-could-affect-18k-customers https://www.wired.com/story/russia-solarwinds-hack-roundup",
    },
    {
        "Title": "PHYSICAL ACCESS",
        "Description": "The attackers gain physical access to your organization and use this to pivot to your internal networks.",
        "Detection": ["Physical Security Review", "User Awareness Training"],
        "Tools": "Clipboard Crowbar RFID Badge Cloner Lockpicks Stolen Keys Counterfeit Work ID Brick Ladder",
        "Documentation": "https://youtu.be/rnmcRTnTNC8",
    },
    {
        "Title": "VENDOR PORTAL",
        "Description": "A vendor portal had been added to the network that created a path into your organization, bypassing all security controls. The attackers scanned this system and deployed malware to it.",
        "Detection": ["Shodan Review", "Protocol Analysis", "Site Walkthrough"],
        "Tools": "Error Maliciousness Shodan Nmap Masscan",
        "Documentation": "https://www.dragos.com/blog/industry-news/preventing-initial-access-in-industrial-environments/",
    },
    {
        "Title": "DUAL-HOMED DEVICE",
        "Description": "An operator connected an engineering workstation (EWS) directly to the internet via a secondary network interface. The attackers found that host on Shodan, and they brute force attacked it to gain access.",
        "Detection": [
            "SIEM Log Analysis",
            "Shodan Review",
            "Endpoint Analysis User",
            "Entity Behavior Analytics (UEBA)",
        ],
        "Tools": "Shodan Nmap Masscan Metasploit Crowbar",
        "Documentation": "https://github.com/galkan/crowbar"
    },
    {
        "Title": "INSIDER THREAT",
        "Description": "An internal disgruntled user exfiltrates information from your network.",
        "Detection": ["User and Entity Behavior Analytics", "DLP", "Working with HR"],
        "Tools": "Being considered a Full Time Expenditure (FTE) Long Hours Addiction",
        "Documentation": "https://americanaddictioncenters.org",
        "Image":"https://i.imgur.com/9ynN9si.png"
    },
    {
        "Title": "PASSWORD SPRAY",
        "Description": "The attackers gain access to your internal network by spraying commonly used passwords (like SeasonYear) against your organization.",
        "Detection": [
            "SIEM Log Analysis User",
            "Entity Behavior Analytics",
            "Firewall Log Review",
        ],
        "Tools": "SprayingToolkit FireProx Hydra DomainPasswordSpray",
        "Documentation": "https://github.com/byt3b|33d3r/SprayingToolkit https://github.com/ustayready/fireprox https://github.com/dafthack/DomainPasswordSpray",
        "Image":"https://i.imgur.com/Hqk8iA1.png"
    },
    {
        "Title": "PHISH",
        "Description": "The attackers send a malicious email targeting users. Because users are super easy to attack. Feel free to add a narrative of a CEO getting phished. Or maybe the Help Desk!",
        "Detection": ["Firewall Log Review", "Endpoint Security Protection Analysis"],
        "Tools": "evilginx GoPhish CredSniper",
        "Documentation": "https://www.blackhillsinfosec.com/how-to-phish-for-geniuses https://www.blackhillsinfosec.com/offensive-spf-how-to- automate-anti-phishing-reconnaissance-using-sender-policy-framework",
        "Image":"https://i.imgur.com/CaMqgLf.png"
    },
    {
        "Title": "SOCIAL ENGINEERING",
        "Description": "The attackers use social engineering to trick a user into running malware.",
        "Detection": [
            "Endpoint Security Protection Analysis",
            "User Awareness Training",
        ],
        "Tools": "Phone A goal and a dream of evil People trusting people",
        "Documentation": "https://youtu.be/rnmcRTnTNC8 https://youtu.be/FvhkkwHjUVg",
        "Image":"https://i.imgur.com/xkxTI9r.png"
    },
    {
        "Title": "WEB SERVER COMPROMISE",
        "Description": "The attackers take over an external web server. They use it to pivot to your internal network.",
        "Detection": [
            "Server Analysis SIEM Log Analysis NetFlow",
            "Zeek/Bro",
            "RITA Analysis",
        ],
        "Tools": "Zed Attack Proxy sqlmap Burp Proxy",
        "Documentation": "https://www.zaproxy.org https://portswigger.net/burp https://www.blackhillsinfosec.com/using-simple-burp-macros-to-automate-testing",
        "Image":"https://i.imgur.com/EDrfaFq.png"
    },
]
