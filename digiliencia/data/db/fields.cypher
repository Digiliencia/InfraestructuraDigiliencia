// Internet Governance
MERGE (f1:Field {name: "Internet Governance", description: ""})
MERGE
  (s1:Field
    {
      name: "Online Surveillance",
      description:
        "Monitoring internet activities for security or regulatory purposes, often balancing privacy concerns and state control."
    })
MERGE (s1)-[:SUBFIELD_OF]->(f1)
MERGE
  (s2:Field
    {
      name: "Privacy Forensics",
      description:
        "Techniques to investigate and analyze digital privacy breaches, ensuring compliance with data protection laws."
    })
MERGE (s2)-[:SUBFIELD_OF]->(f1)
MERGE
  (s3:Field
    {
      name: "Preventing Online Crime",
      description:
        "Strategies to combat cybercrime, including fraud, hacking, and exploitation, through legislation and technology."
    })
MERGE (s3)-[:SUBFIELD_OF]->(f1)
MERGE
  (s4:Field
    {
      name: "Expanding Access",
      description:
        "Efforts to bridge the digital divide by improving internet affordability, infrastructure, and literacy."
    })
MERGE (s4)-[:SUBFIELD_OF]->(f1)
MERGE
  (s5:Field
    {
      name: "Identity Management",
      description:
        "Systems for securely verifying and managing digital identities to prevent fraud and protect user data."
    })
MERGE (s5)-[:SUBFIELD_OF]->(f1)
MERGE
  (s6:Field
    {
      name: "User Rights and Censorship",
      description:
        "Debates over freedom of expression, content moderation, and government restrictions on online platforms."
    })
MERGE (s6)-[:SUBFIELD_OF]->(f1)
MERGE
  (s7:Field
    {
      name: "Data Protection",
      description:
        "Frameworks to safeguard personal data from misuse, emphasizing consent, encryption, and regulatory compliance."
    })
MERGE (s7)-[:SUBFIELD_OF]->(f1)

// Corruption
MERGE (f2:Field {name: "Corruption", description: ""})
MERGE
  (s8:Field
    {
      name: "Victims and Harms",
      description:
        "Impact of corruption on individuals, communities, and institutions, including economic inequality and loss of trust."
    })
MERGE (s8)-[:SUBFIELD_OF]->(f2)
MERGE
  (s9:Field
    {
      name: "Tech for Integrity",
      description:
        "Using digital tools like blockchain and AI to enhance transparency and accountability in governance."
    })
MERGE (s9)-[:SUBFIELD_OF]->(f2)
MERGE
  (s10:Field
    {
      name: "Fair Allocation of Resources and Power",
      description:
        "Addressing systemic inequities in how resources and decision-making authority are distributed."
    })
MERGE (s10)-[:SUBFIELD_OF]->(f2)
MERGE
  (s11:Field
    {
      name: "Insecurity and State Capture",
      description:
        "Corruption undermining state institutions, leading to instability and weakened public services."
    })
MERGE (s11)-[:SUBFIELD_OF]->(f2)
MERGE
  (s12:Field
    {
      name: "Integrity, Trust and Good Governance",
      description:
        "Building ethical systems to restore public confidence in political and administrative processes."
    })
MERGE (s12)-[:SUBFIELD_OF]->(f2)
MERGE
  (s13:Field
    {
      name: "Effective Law Enforcement",
      description:
        "Combating corruption through robust legal frameworks, investigations, and international cooperation."
    })
MERGE (s13)-[:SUBFIELD_OF]->(f2)
MERGE
  (s14:Field
    {
      name: "Global and Collective Action",
      description:
        "Multilateral efforts to address cross-border corruption, such as anti-bribery treaties and financial transparency initiatives."
    })
MERGE (s14)-[:SUBFIELD_OF]->(f2)
MERGE
  (s15:Field
    {
      name: "Corrupt Capital Flows",
      description:
        "Illicit financial movements that exploit weak regulations, often hiding in offshore accounts or shell companies."
    })
MERGE (s15)-[:SUBFIELD_OF]->(f2)

// Banking and Capital Markets
MERGE (f3:Field {name: "Banking and Capital Markets", description: ""})
MERGE
  (s16:Field
    {
      name: "Sustainability and Finance",
      description:
        "Aligning financial practices with environmental and social goals, such as green investments and ESG criteria."
    })
MERGE (s16)-[:SUBFIELD_OF]->(f3)
MERGE
  (s17:Field
    {
      name: "The Financial Risk Landscape",
      description:
        "Assessing evolving risks like cyberattacks, market volatility, and regulatory changes in banking."
    })
MERGE (s17)-[:SUBFIELD_OF]->(f3)
MERGE
  (s18:Field
    {
      name: "Financial Technology",
      description:
        "Innovations like mobile payments, robo-advisors, and blockchain reshaping traditional financial services."
    })
MERGE (s18)-[:SUBFIELD_OF]->(f3)
MERGE
  (s19:Field
    {
      name: "Banking Business Models",
      description:
        "Adapting revenue strategies, including digital banking and subscription-based services."
    })
MERGE (s19)-[:SUBFIELD_OF]->(f3)
MERGE
  (s20:Field
    {
      name: "Financial Talent",
      description:
        "Addressing skill gaps in finance, particularly in AI, cybersecurity, and sustainable investing."
    })
MERGE (s20)-[:SUBFIELD_OF]->(f3)

// [Repeat the structure for f4 to f53 below]

// Values
MERGE (f4:Field {name: "Values", description: ""})
MERGE
  (s21:Field
    {
      name: "Trust as a Value",
      description:
        "Foundational principle for collaboration, requiring transparency and accountability in institutions."
    })
MERGE (s21)-[:SUBFIELD_OF]->(f4)
MERGE
  (s22:Field
    {
      name: "Valuing Digital Equity",
      description:
        "Ensuring fair access to technology and preventing marginalization of underserved communities."
    })
MERGE (s22)-[:SUBFIELD_OF]->(f4)
MERGE
  (s23:Field
    {
      name: "Valuing the Environment",
      description:
        "Prioritizing ecological sustainability in policy and business decisions."
    })
MERGE (s23)-[:SUBFIELD_OF]->(f4)
MERGE
  (s24:Field
    {
      name: "The Common Good",
      description:
        "Promoting societal welfare through inclusive policies and shared resources."
    })
MERGE (s24)-[:SUBFIELD_OF]->(f4)
MERGE
  (s25:Field
    {
      name: "Valuing Human Dignity",
      description:
        "Respecting individual rights and ethical treatment in governance and technology design."
    })
MERGE (s25)-[:SUBFIELD_OF]->(f4)

// Internet of Things (IoT)
MERGE (f5:Field {name: "Internet of Things (IoT)", description: ""})
MERGE
  (s26:Field
    {
      name: "Wireless Sensing and Localization",
      description:
        "Using sensors to track and monitor physical environments, such as smart cities or industrial systems."
    })
MERGE (s26)-[:SUBFIELD_OF]->(f5)
MERGE
  (s27:Field
    {
      name: "IoT Security and Privacy",
      description:
        "Protecting connected devices from breaches and unauthorized data access."
    })
MERGE (s27)-[:SUBFIELD_OF]->(f5)
MERGE
  (s28:Field
    {
      name: "IoT in New Domains",
      description:
        "Expanding IoT applications in healthcare, agriculture, and logistics."
    })
MERGE (s28)-[:SUBFIELD_OF]->(f5)
MERGE
  (s29:Field
    {
      name: "Edge AI",
      description:
        "Processing AI algorithms locally on devices to reduce latency and improve efficiency."
    })
MERGE (s29)-[:SUBFIELD_OF]->(f5)
MERGE
  (s30:Field
    {
      name: "Battery-Free IoT",
      description:
        "Energy-harvesting technologies enabling self-powered, sustainable IoT networks."
    })
MERGE (s30)-[:SUBFIELD_OF]->(f5)

// Geopolitics
MERGE (f6:Field {name: "Geopolitics", description: ""})
MERGE
  (s31:Field
    {
      name: "Strained Institutions and Alliances",
      description:
        "Erosion of trust in international organizations due to competing national interests."
    })
MERGE (s31)-[:SUBFIELD_OF]->(f6)
MERGE
  (s32:Field
    {
      name: "Multipolar, Multi-Conceptual",
      description:
        "Rise of diverse global powers and ideologies reshaping international relations."
    })
MERGE (s32)-[:SUBFIELD_OF]->(f6)
MERGE
  (s33:Field
    {
      name: "Technological Competition",
      description:
        "Rivalry in AI, quantum computing, and semiconductors as a driver of geopolitical tension."
    })
MERGE (s33)-[:SUBFIELD_OF]->(f6)
MERGE
  (s34:Field
    {
      name: "Environmental Dangers",
      description:
        "Cross-border challenges like climate change exacerbating resource conflicts."
    })
MERGE (s34)-[:SUBFIELD_OF]->(f6)
MERGE
  (s35:Field
    {
      name: "Populism and Nationalism",
      description:
        "Political movements prioritizing national identity over global cooperation."
    })
MERGE (s35)-[:SUBFIELD_OF]->(f6)
MERGE
  (s36:Field
    {
      name: "Economic Shifts",
      description:
        "Redistribution of economic power toward emerging markets and away from traditional Western dominance."
    })
MERGE (s36)-[:SUBFIELD_OF]->(f6)

// Justice and Law
MERGE (f7:Field {name: "Justice and Law", description: ""})
MERGE
  (s37:Field
    {
      name: "Forensic Science",
      description:
        "Using technology and scientific methods to investigate crimes and support legal proceedings."
    })
MERGE (s37)-[:SUBFIELD_OF]->(f7)
MERGE
  (s38:Field
    {
      name: "Access to Law and Justice",
      description:
        "Ensuring marginalized groups can navigate legal systems and seek redress."
    })
MERGE (s38)-[:SUBFIELD_OF]->(f7)
MERGE
  (s39:Field
    {
      name: "Security and Intelligence in Justice",
      description:
        "Balancing surveillance and civil liberties in law enforcement."
    })
MERGE (s39)-[:SUBFIELD_OF]->(f7)
MERGE
  (s40:Field
    {
      name: "Science and Innovation in Justice",
      description:
        "Leveraging AI and data analytics to improve court efficiency and fairness."
    })
MERGE (s40)-[:SUBFIELD_OF]->(f7)
MERGE
  (s41:Field
    {
      name: "Governance, Ethics and Justice",
      description:
        "Ethical frameworks for policymaking and addressing systemic biases in legal systems."
    })
MERGE (s41)-[:SUBFIELD_OF]->(f7)
MERGE
  (s42:Field
    {
      name: "Human Decision-Making Governance",
      description:
        "Combining AI tools with human judgment in judicial and regulatory contexts."
    })
MERGE (s42)-[:SUBFIELD_OF]->(f7)
MERGE
  (s43:Field
    {
      name: "Technology and Justice",
      description:
        "Digital platforms for dispute resolution, virtual courts, and legal tech innovation."
    })
MERGE (s43)-[:SUBFIELD_OF]->(f7)

// Global Governance
MERGE (f8:Field {name: "Global Governance", description: ""})
MERGE
  (s44:Field
    {
      name: "Geopolitical Competition",
      description:
        "Struggles for influence among states in multilateral institutions and trade agreements."
    })
MERGE (s44)-[:SUBFIELD_OF]->(f8)
MERGE
  (s45:Field
    {
      name: "Demands for Justice",
      description:
        "Calls for equitable solutions to global issues like climate reparations or refugee crises."
    })
MERGE (s45)-[:SUBFIELD_OF]->(f8)
MERGE
  (s46:Field
    {
      name: "Polarizing Narratives",
      description:
        "Misinformation and propaganda deepening ideological divides in international discourse."
    })
MERGE (s46)-[:SUBFIELD_OF]->(f8)
MERGE
  (s47:Field
    {
      name: "Technological Independence",
      description:
        "Nations striving for self-reliance in critical technologies to avoid foreign dependence."
    })
MERGE (s47)-[:SUBFIELD_OF]->(f8)
MERGE
  (s48:Field
    {
      name: "Institutional Capacity",
      description:
        "Strengthening international bodies to address transnational challenges effectively."
    })
MERGE (s48)-[:SUBFIELD_OF]->(f8)

// Data Science
MERGE (f9:Field {name: "Data Science", description: ""})
MERGE
  (s49:Field
    {
      name: "Data Generation, Processing, and Curation",
      description:
        "Managing data lifecycles from collection to storage, ensuring quality and relevance."
    })
MERGE (s49)-[:SUBFIELD_OF]->(f9)
MERGE
  (s50:Field
    {
      name: "Data Literacy and Education",
      description:
        "Teaching individuals and organizations to interpret and use data responsibly."
    })
MERGE (s50)-[:SUBFIELD_OF]->(f9)
MERGE
  (s51:Field
    {
      name: "Data Governance and Sharing",
      description:
        "Frameworks for ethical data use, balancing openness with privacy and security."
    })
MERGE (s51)-[:SUBFIELD_OF]->(f9)
MERGE
  (s52:Field
    {
      name: "Data and Algorithm Ethics",
      description:
        "Addressing biases in datasets and algorithms to prevent discriminatory outcomes."
    })
MERGE (s52)-[:SUBFIELD_OF]->(f9)
MERGE
  (s53:Field
    {
      name: "Data Communication and Visualization",
      description:
        "Presenting complex data insights through accessible charts, dashboards, and narratives."
    })
MERGE (s53)-[:SUBFIELD_OF]->(f9)
MERGE
  (s54:Field
    {
      name: "Data Analysis and Uncertainty Assessment",
      description:
        "Quantifying risks and uncertainties in data-driven decision-making."
    })
MERGE (s54)-[:SUBFIELD_OF]->(f9)

// The Digital Economy
MERGE (f10:Field {name: "The Digital Economy", description: ""})
MERGE
  (s55:Field
    {
      name: "Universal Adoption of Affordable Digital Services",
      description:
        "Expanding access to low-cost internet, cloud services, and digital tools globally."
    })
MERGE (s55)-[:SUBFIELD_OF]->(f10)
MERGE
  (s56:Field
    {
      name: "Cross-Border Trade and Cooperation",
      description:
        "Facilitating international e-commerce while navigating data localization laws."
    })
MERGE (s56)-[:SUBFIELD_OF]->(f10)
MERGE
  (s57:Field
    {
      name: "Trust, Security, and Protection",
      description:
        "Building consumer confidence through cybersecurity and data privacy measures."
    })
MERGE (s57)-[:SUBFIELD_OF]->(f10)
MERGE
  (s58:Field
    {
      name: "Strategic Development of New Technologies",
      description:
        "Prioritizing R&D in AI, blockchain, and IoT to drive economic growth."
    })
MERGE (s58)-[:SUBFIELD_OF]->(f10)
MERGE
  (s59:Field
    {
      name: "Digital Skills and Human Capital",
      description:
        "Upskilling workers for roles in tech-driven industries and remote work environments."
    })
MERGE (s59)-[:SUBFIELD_OF]->(f10)
MERGE
  (s60:Field
    {
      name: "Digital and Sustainability Transformation of Industries",
      description:
        "Using digital tools to reduce carbon footprints in manufacturing, energy, and logistics."
    })
MERGE (s60)-[:SUBFIELD_OF]->(f10)

// Agile Governance
MERGE (f11:Field {name: "Agile Governance", description: ""})
MERGE
  (s61:Field
    {
      name: "Managing Technology's Impact",
      description:
        "Adapting policies to address rapid tech changes like AI and biotech."
    })
MERGE (s61)-[:SUBFIELD_OF]->(f11)
MERGE
  (s62:Field
    {
      name: "Managing Uncertainty",
      description:
        "Creating flexible systems to respond to crises, such as pandemics or cyberattacks."
    })
MERGE (s62)-[:SUBFIELD_OF]->(f11)
MERGE
  (s63:Field
    {
      name: "The Importance of Values in Governing",
      description:
        "Embedding ethics, equity, and sustainability into decision-making."
    })
MERGE (s63)-[:SUBFIELD_OF]->(f11)
MERGE
  (s64:Field
    {
      name: "Governing for the Environment",
      description:
        "Policy frameworks to align economic growth with climate action."
    })
MERGE (s64)-[:SUBFIELD_OF]->(f11)
MERGE
  (s65:Field
    {
      name: "Multi-Stakeholder Collaboration",
      description:
        "Involving governments, businesses, and civil society in solving complex challenges."
    })
MERGE (s65)-[:SUBFIELD_OF]->(f11)
MERGE
  (s66:Field
    {
      name: "Governing Communication Chaos",
      description:
        "Regulating misinformation and ensuring reliable information flows in digital spaces."
    })
MERGE (s66)-[:SUBFIELD_OF]->(f11)
MERGE
  (s67:Field
    {
      name: "Making Multilateralism More Effective",
      description:
        "Reforming international institutions to address 21st-century challenges."
    })
MERGE (s67)-[:SUBFIELD_OF]->(f11)

// European Union
MERGE (f12:Field {name: "European Union", description: ""})
MERGE
  (s68:Field
    {
      name: "The EU's Green Transition",
      description:
        "Policies to achieve carbon neutrality, such as renewable energy investments and circular economy initiatives."
    })
MERGE (s68)-[:SUBFIELD_OF]->(f12)
MERGE
  (s69:Field
    {
      name: "The EU's Geopolitical Position",
      description:
        "Balancing relations with the US, China, and Russia amid shifting global power dynamics."
    })
MERGE (s69)-[:SUBFIELD_OF]->(f12)
MERGE
  (s70:Field
    {
      name: "The EU's Defense and Security Policy",
      description:
        "Strengthening collective defense and cybersecurity capabilities."
    })
MERGE (s70)-[:SUBFIELD_OF]->(f12)
MERGE
  (s71:Field
    {
      name: "Social Investment and Fiscal Union",
      description:
        "Addressing economic disparities among member states through shared fiscal policies."
    })
MERGE (s71)-[:SUBFIELD_OF]->(f12)
MERGE
  (s72:Field
    {
      name: "Democratic Participation",
      description:
        "Enhancing citizen engagement in EU governance through digital tools and reforms."
    })
MERGE (s72)-[:SUBFIELD_OF]->(f12)
MERGE
  (s73:Field
    {
      name: "AI and Challenges for Democracy",
      description:
        "Regulating AI to prevent election interference and protect democratic processes."
    })
MERGE (s73)-[:SUBFIELD_OF]->(f12)
MERGE
  (s74:Field
    {
      name: "Migration to the EU",
      description:
        "Managing refugee flows and integration while addressing political tensions."
    })
MERGE (s74)-[:SUBFIELD_OF]->(f12)
MERGE
  (s75:Field
    {
      name: "Strategic Autonomy, De-risking and Trade",
      description:
        "Reducing reliance on external powers for critical technologies and energy."
    })
MERGE (s75)-[:SUBFIELD_OF]->(f12)

// Future of Consumption
MERGE (f13:Field {name: "Future of Consumption", description: ""})
MERGE
  (s76:Field
    {
      name: "Inclusive Consumption",
      description:
        "Designing products and services accessible to diverse socioeconomic groups."
    })
MERGE (s76)-[:SUBFIELD_OF]->(f13)
MERGE
  (s77:Field
    {
      name: "Government Policy and Consumption",
      description:
        "Using taxation, subsidies, and regulations to shape sustainable consumption patterns."
    })
MERGE (s77)-[:SUBFIELD_OF]->(f13)
MERGE
  (s78:Field
    {
      name: "Consumption and Empowered Consumers",
      description:
        "Enabling informed choices through transparency in product sourcing and environmental impact."
    })
MERGE (s78)-[:SUBFIELD_OF]->(f13)
MERGE
  (s79:Field
    {
      name: "Consumer Trust and Transparency",
      description:
        "Building loyalty via ethical business practices and clear communication."
    })
MERGE (s79)-[:SUBFIELD_OF]->(f13)
MERGE
  (s80:Field
    {
      name: "Environmentally-Sustainable Consumerism",
      description:
        "Promoting eco-friendly products and circular economy models."
    })
MERGE (s80)-[:SUBFIELD_OF]->(f13)
MERGE
  (s81:Field
    {
      name: "Consumer Well-Being",
      description:
        "Prioritizing health, safety, and mental health in product design and marketing."
    })
MERGE (s81)-[:SUBFIELD_OF]->(f13)

// Corporate Governance
MERGE (f14:Field {name: "Corporate Governance", description: ""})
MERGE
  (s82:Field
    {
      name: "Workplace Culture and Incentives",
      description:
        "Fostering ethical behavior and innovation through leadership and reward systems."
    })
MERGE (s82)-[:SUBFIELD_OF]->(f14)
MERGE
  (s83:Field
    {
      name: "Purpose-Driven Strategy and Capital Allocation",
      description:
        "Aligning business goals with social and environmental impact."
    })
MERGE (s83)-[:SUBFIELD_OF]->(f14)
MERGE
  (s84:Field
    {
      name: "Tech Governance",
      description:
        "Overseeing the ethical use of AI, data analytics, and automation in operations."
    })
MERGE (s84)-[:SUBFIELD_OF]->(f14)
MERGE
  (s85:Field
    {
      name: "Stakeholder Engagement and Cultivating Trust",
      description:
        "Balancing shareholder interests with community and environmental responsibilities."
    })
MERGE (s85)-[:SUBFIELD_OF]->(f14)
MERGE
  (s86:Field
    {
      name: "Values, Ethics, and Integrity",
      description:
        "Embedding ethical standards into corporate decision-making and supply chains."
    })
MERGE (s86)-[:SUBFIELD_OF]->(f14)
MERGE
  (s87:Field
    {
      name: "Legal and Regulatory Evolution",
      description:
        "Adapting to new laws on data privacy, antitrust, and sustainability."
    })
MERGE (s87)-[:SUBFIELD_OF]->(f14)
MERGE
  (s88:Field
    {
      name: "Integrated Oversight and Disclosure",
      description:
        "Ensuring transparency in financial reporting and risk management."
    })
MERGE (s88)-[:SUBFIELD_OF]->(f14)
MERGE
  (s89:Field
    {
      name: "Enterprise and Emerging Risks",
      description:
        "Addressing cybersecurity, climate change, and geopolitical risks in strategic planning."
    })
MERGE (s89)-[:SUBFIELD_OF]->(f14)

// Systematic Racism
MERGE (f15:Field {name: "Systematic Racism", description: ""})
MERGE
  (s90:Field
    {
      name: "Access to Justice and Mass Incarceration",
      description:
        "Disproportionate impacts of legal systems on racial minorities and advocacy for reform."
    })
MERGE (s90)-[:SUBFIELD_OF]->(f15)
MERGE
  (s91:Field
    {
      name: "Economic Opportunity",
      description:
        "Addressing wage gaps, employment discrimination, and wealth disparities."
    })
MERGE (s91)-[:SUBFIELD_OF]->(f15)
MERGE
  (s92:Field
    {
      name: "Healthcare Disparities",
      description:
        "Unequal access to medical care and outcomes due to systemic biases."
    })
MERGE (s92)-[:SUBFIELD_OF]->(f15)
MERGE
  (s93:Field
    {
      name: "Effective Change",
      description:
        "Strategies for dismantling discriminatory policies and promoting equity."
    })
MERGE (s93)-[:SUBFIELD_OF]->(f15)
MERGE
  (s94:Field
    {
      name: "Cultural Reinforcement of Racism",
      description:
        "Media, education, and institutions perpetuating racial stereotypes."
    })
MERGE (s94)-[:SUBFIELD_OF]->(f15)
MERGE
  (s95:Field
    {
      name: "Defining Racism",
      description:
        "Understanding structural racism beyond individual prejudice."
    })
MERGE (s95)-[:SUBFIELD_OF]->(f15)
MERGE
  (s96:Field
    {
      name: "Access to Leadership Opportunities",
      description:
        "Breaking barriers for underrepresented groups in politics, business, and academia."
    })
MERGE (s96)-[:SUBFIELD_OF]->(f15)

// Innovation
MERGE (f16:Field {name: "Innovation", description: ""})
MERGE
  (s97:Field
    {
      name: "Social Innovation",
      description:
        "Solving societal challenges through new ideas in education, healthcare, and community development."
    })
MERGE (s97)-[:SUBFIELD_OF]->(f16)
MERGE
  (s98:Field
    {
      name: "Open Innovation",
      description:
        "Collaborating across sectors to accelerate R&D and knowledge sharing."
    })
MERGE (s98)-[:SUBFIELD_OF]->(f16)
MERGE
  (s99:Field
    {
      name: "Innovation Ecosystems",
      description:
        "Building networks of startups, investors, and policymakers to foster entrepreneurship."
    })
MERGE (s99)-[:SUBFIELD_OF]->(f16)
MERGE
  (s100:Field
    {
      name: "Business Model Innovation",
      description:
        "Creating new revenue streams and value propositions in digital markets."
    })
MERGE (s100)-[:SUBFIELD_OF]->(f16)
MERGE
  (s101:Field
    {
      name: "Technology Innovation",
      description:
        "Advancing cutting-edge solutions in AI, quantum computing, and biotech."
    })
MERGE (s101)-[:SUBFIELD_OF]->(f16)

// Gender Inequality
MERGE (f17:Field {name: "Gender Inequality", description: ""})
MERGE
  (s102:Field
    {
      name: "Economic Opportunity and Poverty",
      description:
        "Addressing barriers to education, employment, and financial inclusion for women."
    })
MERGE (s102)-[:SUBFIELD_OF]->(f17)
MERGE
  (s103:Field
    {
      name: "Gender Wage Gaps",
      description:
        "Persistent disparities in pay between men and women for equal work."
    })
MERGE (s103)-[:SUBFIELD_OF]->(f17)
MERGE
  (s104:Field
    {
      name: "Gender-Based Violence",
      description:
        "Combating harassment, domestic abuse, and systemic discrimination."
    })
MERGE (s104)-[:SUBFIELD_OF]->(f17)
MERGE
  (s105:Field
    {
      name: "The Care Conundrum",
      description:
        "Unpaid caregiving responsibilities disproportionately affecting women's careers."
    })
MERGE (s105)-[:SUBFIELD_OF]->(f17)
MERGE
  (s106:Field
    {
      name: "Women in Crises",
      description:
        "Impact of conflict, climate disasters, and economic downturns on women's rights."
    })
MERGE (s106)-[:SUBFIELD_OF]->(f17)
MERGE
  (s107:Field
    {
      name: "Political Gender Inequality",
      description:
        "Underrepresentation of women in leadership and policymaking roles."
    })
MERGE (s107)-[:SUBFIELD_OF]->(f17)

// Education
MERGE (f18:Field {name: "Education", description: ""})
MERGE
  (s108:Field
    {
      name: "Core Soft Skills",
      description:
        "Teaching critical thinking, communication, and emotional intelligence for modern challenges."
    })
MERGE (s108)-[:SUBFIELD_OF]->(f18)
MERGE
  (s109:Field
    {
      name: "Education Innovation",
      description:
        "Leveraging edtech, gamification, and personalized learning tools."
    })
MERGE (s109)-[:SUBFIELD_OF]->(f18)
MERGE
  (s110:Field
    {
      name: "Lifelong Learning Pathways",
      description:
        "Creating accessible training programs for career transitions and upskilling."
    })
MERGE (s110)-[:SUBFIELD_OF]->(f18)
MERGE
  (s111:Field
    {
      name: "Quality Basic Education",
      description:
        "Ensuring foundational literacy, numeracy, and digital skills for all children."
    })
MERGE (s111)-[:SUBFIELD_OF]->(f18)
MERGE
  (s112:Field
    {
      name: "Relevant Continuing Education",
      description: "Aligning adult education with evolving job market demands."
    })
MERGE (s112)-[:SUBFIELD_OF]->(f18)
MERGE
  (s113:Field
    {
      name: "Digital Fluency and STEM Skills",
      description:
        "Preparing students for tech-driven careers through coding, AI literacy, and science education."
    })
MERGE (s113)-[:SUBFIELD_OF]->(f18)

// Leadership
MERGE (f19:Field {name: "Leadership", description: ""})
MERGE
  (s114:Field
    {
      name: "Adaptive Leadership",
      description:
        "Navigating change through flexibility, empathy, and crisis management."
    })
MERGE (s114)-[:SUBFIELD_OF]->(f19)
MERGE
  (s115:Field
    {
      name: "Technology Leadership",
      description:
        "Guiding organizations through digital transformation and ethical AI adoption."
    })
MERGE (s115)-[:SUBFIELD_OF]->(f19)
MERGE
  (s116:Field
    {
      name: "Responsibility and Accountability",
      description:
        "Holding leaders accountable for ethical decisions and stakeholder impact."
    })
MERGE (s116)-[:SUBFIELD_OF]->(f19)
MERGE
  (s117:Field
    {
      name: "Entrepreneurial Leadership",
      description:
        "Fostering innovation and risk-taking in startups and established firms."
    })
MERGE (s117)-[:SUBFIELD_OF]->(f19)
MERGE
  (s118:Field
    {
      name: "Systems Leadership",
      description:
        "Addressing interconnected challenges through holistic, cross-sector collaboration."
    })
MERGE (s118)-[:SUBFIELD_OF]->(f19)
MERGE
  (s119:Field
    {
      name: "Shaping Societies",
      description:
        "Influencing cultural, political, and economic systems for inclusive progress."
    })
MERGE (s119)-[:SUBFIELD_OF]->(f19)

// Youth Perspectives
MERGE (f20:Field {name: "Youth Perspectives", description: ""})
MERGE
  (s120:Field
    {
      name: "Youth, Migration, and Globalization",
      description:
        "Young people's roles in addressing displacement, cultural exchange, and global citizenship."
    })
MERGE (s120)-[:SUBFIELD_OF]->(f20)
MERGE
  (s121:Field
    {
      name: "Financial Know-How and Youth",
      description:
        "Promoting financial literacy and access to banking for younger generations."
    })
MERGE (s121)-[:SUBFIELD_OF]->(f20)
MERGE
  (s122:Field
    {
      name: "Youth Education, Skills and Employment",
      description:
        "Bridging gaps between education systems and job market needs."
    })
MERGE (s122)-[:SUBFIELD_OF]->(f20)
MERGE
  (s123:Field
    {
      name: "Enabling Lifelong Health and Well-Being",
      description:
        "Mental health support and physical wellness programs for youth."
    })
MERGE (s123)-[:SUBFIELD_OF]->(f20)
MERGE
  (s124:Field
    {
      name: "Youth Addressing Climate Change",
      description:
        "Engaging young activists in sustainability and climate policy."
    })
MERGE (s124)-[:SUBFIELD_OF]->(f20)
MERGE
  (s125:Field
    {
      name: "Youth Digital Participation",
      description:
        "Ensuring youth voices in shaping tech policies and online spaces."
    })
MERGE (s125)-[:SUBFIELD_OF]->(f20)

// Mobility
MERGE (f21:Field {name: "Mobility", description: ""})
MERGE
  (s126:Field
    {
      name: "More Sustainable Mobility",
      description:
        "Promoting electric vehicles, public transit, and bike-sharing to reduce emissions."
    })
MERGE (s126)-[:SUBFIELD_OF]->(f21)
MERGE
  (s127:Field
    {
      name: "Energy Efficiency and Mobility",
      description:
        "Optimizing transport systems to minimize energy consumption."
    })
MERGE (s127)-[:SUBFIELD_OF]->(f21)
MERGE
  (s128:Field
    {
      name: "Smarter Infrastructure for Mobility",
      description:
        "Using IoT and AI to manage traffic and improve urban transportation."
    })
MERGE (s128)-[:SUBFIELD_OF]->(f21)
MERGE
  (s129:Field
    {
      name: "Greater Mobility, Bigger Security Risks",
      description:
        "Balancing convenience with cybersecurity in connected vehicles and transit systems."
    })
MERGE (s129)-[:SUBFIELD_OF]->(f21)
MERGE
  (s130:Field
    {
      name: "Trade and Travel Barriers to Mobility",
      description:
        "Addressing visa restrictions, tariffs, and pandemic-related movement controls."
    })
MERGE (s130)-[:SUBFIELD_OF]->(f21)

// Digital Identity
MERGE (f22:Field {name: "Digital Identity", description: ""})
MERGE
  (s131:Field
    {
      name: "Identity Fraud and Cyber Resilience",
      description:
        "Combating identity theft and strengthening authentication methods."
    })
MERGE (s131)-[:SUBFIELD_OF]->(f22)
MERGE
  (s132:Field
    {
      name: "The Economic Value of Digital Identity",
      description:
        "Leveraging identity systems for financial inclusion and service access."
    })
MERGE (s132)-[:SUBFIELD_OF]->(f22)
MERGE
  (s133:Field
    {
      name: "Digital Inclusion and Opportunity",
      description:
        "Ensuring marginalized groups can participate in the digital economy."
    })
MERGE (s133)-[:SUBFIELD_OF]->(f22)
MERGE
  (s134:Field
    {
      name: "Privacy, Agency and Trust",
      description:
        "Empowering users to control their data and digital personas."
    })
MERGE (s134)-[:SUBFIELD_OF]->(f22)
MERGE
  (s135:Field
    {
      name: "From Silos to Collaboration",
      description:
        "Integrating identity systems across sectors for seamless verification."
    })
MERGE (s135)-[:SUBFIELD_OF]->(f22)

// Electricity
MERGE (f23:Field {name: "Electricity", description: ""})
MERGE
  (s136:Field
    {
      name: "Electric System Decentralization and Digitalization",
      description:
        "Transitioning to smart grids and distributed energy resources like solar panels."
    })
MERGE (s136)-[:SUBFIELD_OF]->(f23)
MERGE
  (s137:Field
    {
      name: "Universal, Equitable, Sustainable Access",
      description:
        "Expanding electricity access while reducing environmental harm."
    })
MERGE (s137)-[:SUBFIELD_OF]->(f23)
MERGE
  (s138:Field
    {
      name: "Demand Side Engagement",
      description:
        "Encouraging consumers to shift energy use for grid stability."
    })
MERGE (s138)-[:SUBFIELD_OF]->(f23)
MERGE
  (s139:Field
    {
      name: "Network Management and Investment",
      description:
        "Modernizing infrastructure to handle renewable energy integration."
    })
MERGE (s139)-[:SUBFIELD_OF]->(f23)
MERGE
  (s140:Field
    {
      name: "Energy Security, Reliability, and Resilience",
      description:
        "Protecting grids from cyberattacks, natural disasters, and supply disruptions."
    })
MERGE (s140)-[:SUBFIELD_OF]->(f23)
MERGE
  (s141:Field
    {
      name: "Energy Sector Transformation",
      description:
        "Moving from fossil fuels to renewables and storage solutions."
    })
MERGE (s141)-[:SUBFIELD_OF]->(f23)
MERGE
  (s142:Field
    {
      name: "Market Environment for the Energy Transition",
      description:
        "Policy reforms to incentivize clean energy investment and innovation."
    })
MERGE (s142)-[:SUBFIELD_OF]->(f23)

// International Security
MERGE (f24:Field {name: "International Security", description: ""})
MERGE
  (s143:Field
    {
      name: "Changing Polarity",
      description:
        "Shift from US-dominated unipolarity to multipolar power struggles."
    })
MERGE (s143)-[:SUBFIELD_OF]->(f24)
MERGE
  (s144:Field
    {
      name: "The Transformation of Warfare",
      description:
        "Emergence of cyberwarfare, drones, and AI-driven military strategies."
    })
MERGE (s144)-[:SUBFIELD_OF]->(f24)
MERGE
  (s145:Field
    {
      name: "The Rise of Non-State Actors",
      description:
        "Increased influence of terrorist groups, NGOs, and corporations in global security."
    })
MERGE (s145)-[:SUBFIELD_OF]->(f24)
MERGE
  (s146:Field
    {
      name: "Geostrategic Competition and Security",
      description:
        "Tensions between major powers over territorial claims and military dominance."
    })
MERGE (s146)-[:SUBFIELD_OF]->(f24)
MERGE
  (s147:Field
    {
      name: "The Technological Arms Race",
      description:
        "Race to develop advanced weapons like hypersonic missiles and AI-driven defense systems."
    })
MERGE (s147)-[:SUBFIELD_OF]->(f24)
MERGE
  (s148:Field
    {
      name: "Hybrid Threats",
      description:
        "Combining conventional warfare, cyberattacks, and disinformation campaigns."
    })
MERGE (s148)-[:SUBFIELD_OF]->(f24)
MERGE
  (s149:Field
    {
      name: "Diffusion of Power",
      description:
        "Decentralization of military and economic influence among states and non-state entities."
    })
MERGE (s149)-[:SUBFIELD_OF]->(f24)

// Infrastructure
MERGE (f25:Field {name: "Infrastructure", description: ""})
MERGE
  (s150:Field
    {
      name: "Private Capital in Infrastructure",
      description:
        "Encouraging private investment in public projects through PPPs and bonds."
    })
MERGE (s150)-[:SUBFIELD_OF]->(f25)
MERGE
  (s151:Field
    {
      name: "Infrastructure Resilience",
      description:
        "Designing systems to withstand climate change, cyberattacks, and disasters."
    })
MERGE (s151)-[:SUBFIELD_OF]->(f25)
MERGE
  (s152:Field
    {
      name: "Infrastructure as a Geopolitical Tool",
      description:
        "Using projects like China's Belt and Road Initiative to expand global influence."
    })
MERGE (s152)-[:SUBFIELD_OF]->(f25)
MERGE
  (s153:Field
    {
      name: "The Risk of Mismatching Risk",
      description:
        "Aligning funding timelines with long-term infrastructure maintenance needs."
    })
MERGE (s153)-[:SUBFIELD_OF]->(f25)
MERGE
  (s154:Field
    {
      name: "Bankable Project Pipelines",
      description:
        "Developing feasible, profitable projects to attract investors."
    })
MERGE (s154)-[:SUBFIELD_OF]->(f25)
MERGE
  (s155:Field
    {
      name: "Corruption and Infrastructure",
      description: "Addressing graft in procurement and construction processes."
    })
MERGE (s155)-[:SUBFIELD_OF]->(f25)
MERGE
  (s156:Field
    {
      name: "Skill Building for Infrastructure",
      description:
        "Training workers for roles in smart cities, renewable energy, and digital networks."
    })
MERGE (s156)-[:SUBFIELD_OF]->(f25)
MERGE
  (s157:Field
    {
      name: "Infrastructure Technology and Innovation",
      description:
        "Adopting 5G, AI, and green materials to modernize infrastructure."
    })
MERGE (s157)-[:SUBFIELD_OF]->(f25)

// Nuclear Security
MERGE (f26:Field {name: "Nuclear Security", description: ""})
MERGE
  (s158:Field
    {
      name: "Cyber Threats",
      description:
        "Protecting nuclear facilities and command systems from hacking and sabotage."
    })
MERGE (s158)-[:SUBFIELD_OF]->(f26)
MERGE
  (s159:Field
    {
      name: "Conflict Zones and Fragile States",
      description:
        "Risks of nuclear materials falling into unstable regions or terrorist hands."
    })
MERGE (s159)-[:SUBFIELD_OF]->(f26)
MERGE
  (s160:Field
    {
      name: "Geopolitical Tensions",
      description:
        "Arms races and proliferation risks due to strained international relations."
    })
MERGE (s160)-[:SUBFIELD_OF]->(f26)
MERGE
  (s161:Field
    {
      name: "Emerging Economies",
      description:
        "Balancing civilian nuclear energy development with non-proliferation goals."
    })
MERGE (s161)-[:SUBFIELD_OF]->(f26)
MERGE
  (s162:Field
    {
      name: "Energy Independence",
      description:
        "Using nuclear power to reduce reliance on fossil fuel imports."
    })
MERGE (s162)-[:SUBFIELD_OF]->(f26)
MERGE
  (s163:Field
    {
      name: "Disruptive Technologies",
      description:
        "Implications of AI and quantum computing on nuclear deterrence and security."
    })
MERGE (s163)-[:SUBFIELD_OF]->(f26)

// Digital Communications
MERGE (f27:Field {name: "Digital Communications", description: ""})
MERGE
  (s164:Field
    {
      name: "Future Communication Systems",
      description:
        "Advancements in 6G, satellite internet, and quantum communication."
    })
MERGE (s164)-[:SUBFIELD_OF]->(f27)
MERGE
  (s165:Field
    {
      name: "Connectivity and Coverage",
      description:
        "Expanding global internet access, particularly in rural and conflict zones."
    })
MERGE (s165)-[:SUBFIELD_OF]->(f27)
MERGE
  (s166:Field
    {
      name: "Policy Uncertainty",
      description:
        "Challenges in regulating emerging tech like AI-driven content moderation."
    })
MERGE (s166)-[:SUBFIELD_OF]->(f27)
MERGE
  (s167:Field
    {
      name: "Secure Data Transmission",
      description:
        "Encryption and quantum-resistant methods to protect sensitive communications."
    })
MERGE (s167)-[:SUBFIELD_OF]->(f27)
MERGE
  (s168:Field
    {
      name: "Sustainable Communication Infrastructure",
      description: "Reducing energy consumption of data centers and networks."
    })
MERGE (s168)-[:SUBFIELD_OF]->(f27)
MERGE
  (s169:Field
    {
      name: "An Expanding Internet of Things",
      description:
        "Integrating IoT devices into communication networks for smart environments."
    })
MERGE (s169)-[:SUBFIELD_OF]->(f27)

// The Digital Transformation of Business
MERGE
  (f28:Field {name: "The Digital Transformation of Business", description: ""})
MERGE
  (s170:Field
    {
      name: "New Digital Business Models",
      description:
        "Reimagining revenue streams through subscription services, platform economies, and AI-driven personalization."
    })
MERGE (s170)-[:SUBFIELD_OF]->(f28)
MERGE
  (s171:Field
    {
      name: "New Value and Markets",
      description:
        "Creating opportunities in virtual reality, digital twins, and decentralized finance."
    })
MERGE (s171)-[:SUBFIELD_OF]->(f28)
MERGE
  (s172:Field
    {
      name: "The Digital Enterprise",
      description:
        "Integrating cloud computing, automation, and data analytics into core operations."
    })
MERGE (s172)-[:SUBFIELD_OF]->(f28)
MERGE
  (s173:Field
    {
      name: "Successful Digital Transformation",
      description:
        "Cultural change, leadership buy-in, and employee upskilling as key success factors."
    })
MERGE (s173)-[:SUBFIELD_OF]->(f28)
MERGE
  (s174:Field
    {
      name: "Leading on Inclusion, Sustainability and Trust",
      description:
        "Embedding ethical practices into digital strategies to build consumer confidence."
    })
MERGE (s174)-[:SUBFIELD_OF]->(f28)

// Cities and Urbanization
MERGE (f29:Field {name: "Cities and Urbanization", description: ""})
MERGE
  (s175:Field
    {
      name: "Urban Environment and Resources",
      description:
        "Managing pollution, waste, and green spaces in densely populated areas."
    })
MERGE (s175)-[:SUBFIELD_OF]->(f29)
MERGE
  (s176:Field
    {
      name: "Urban Economies",
      description:
        "Fostering innovation hubs, inclusive job markets, and affordable housing."
    })
MERGE (s176)-[:SUBFIELD_OF]->(f29)
MERGE
  (s177:Field
    {
      name: "Urban Diplomacy",
      description:
        "Cities engaging in international partnerships to address climate change and migration."
    })
MERGE (s177)-[:SUBFIELD_OF]->(f29)
MERGE
  (s178:Field
    {
      name: "Urban Society",
      description:
        "Addressing inequality, cultural integration, and community resilience."
    })
MERGE (s178)-[:SUBFIELD_OF]->(f29)
MERGE
  (s179:Field
    {
      name: "Urban Resilience",
      description:
        "Preparing cities for climate disasters, pandemics, and economic shocks."
    })
MERGE (s179)-[:SUBFIELD_OF]->(f29)
MERGE
  (s180:Field
    {
      name: "Urban Innovation",
      description:
        "Using smart city technologies for traffic, energy, and public service management."
    })
MERGE (s180)-[:SUBFIELD_OF]->(f29)
MERGE
  (s181:Field
    {
      name: "Urban Infrastructure and Services",
      description:
        "Modernizing transportation, utilities, and healthcare systems for growing populations."
    })
MERGE (s181)-[:SUBFIELD_OF]->(f29)
MERGE
  (s182:Field
    {
      name: "Urban Governance",
      description:
        "Balancing local autonomy with national policies in metropolitan planning."
    })
MERGE (s182)-[:SUBFIELD_OF]->(f29)

// Global Risks
MERGE (f30:Field {name: "Global Risks", description: ""})
MERGE
  (s183:Field
    {
      name: "Environmental Collapse",
      description:
        "Threats from biodiversity loss, deforestation, and climate tipping points."
    })
MERGE (s183)-[:SUBFIELD_OF]->(f30)
MERGE
  (s184:Field
    {
      name: "Digital Polarization",
      description:
        "Echo chambers and misinformation deepening societal divides."
    })
MERGE (s184)-[:SUBFIELD_OF]->(f30)
MERGE
  (s185:Field
    {
      name: "Rising Economic Tensions",
      description:
        "Trade wars, inflation, and debt crises destabilizing global markets."
    })
MERGE (s185)-[:SUBFIELD_OF]->(f30)
MERGE
  (s186:Field
    {
      name: "Global Power Shifts",
      description:
        "Emergence of new alliances and conflicts as China and others gain influence."
    })
MERGE (s186)-[:SUBFIELD_OF]->(f30)
MERGE
  (s187:Field
    {
      name: "Ageing Populations",
      description:
        "Economic and healthcare challenges from declining birth rates in developed nations."
    })
MERGE (s187)-[:SUBFIELD_OF]->(f30)
MERGE
  (s188:Field
    {
      name: "Biotech Challenges",
      description:
        "Ethical dilemmas in gene editing, synthetic biology, and pandemic preparedness."
    })
MERGE (s188)-[:SUBFIELD_OF]->(f30)

// Fourth Industrial Revolution
MERGE (f31:Field {name: "Fourth Industrial Revolution", description: ""})
MERGE
  (s189:Field
    {
      name: "Industry Technology Innovation",
      description:
        "Convergence of AI, robotics, IoT, and biotech driving unprecedented change."
    })
MERGE (s189)-[:SUBFIELD_OF]->(f31)
MERGE
  (s190:Field
    {
      name: "Frontier Technologies",
      description:
        "Exploring quantum computing, brain-computer interfaces, and advanced materials."
    })
MERGE (s190)-[:SUBFIELD_OF]->(f31)
MERGE
  (s191:Field
    {
      name: "Ethics and Identity",
      description:
        "Debating AI consciousness, digital rights, and human-machine integration."
    })
MERGE (s191)-[:SUBFIELD_OF]->(f31)
MERGE
  (s192:Field
    {
      name: "Agile Technology Governance",
      description:
        "Regulatory frameworks that adapt to rapid tech advancements."
    })
MERGE (s192)-[:SUBFIELD_OF]->(f31)
MERGE
  (s193:Field
    {
      name: "Agency and Trust",
      description: "Ensuring humans retain control over autonomous systems."
    })
MERGE (s193)-[:SUBFIELD_OF]->(f31)
MERGE
  (s194:Field
    {
      name: "Disrupting Jobs, Demanding New Skills",
      description:
        "Automation reshaping labor markets and requiring lifelong learning."
    })
MERGE (s194)-[:SUBFIELD_OF]->(f31)
MERGE
  (s195:Field
    {
      name: "Technology Access and Inclusion",
      description:
        "Bridging gaps in internet access, education, and innovation opportunities."
    })
MERGE (s195)-[:SUBFIELD_OF]->(f31)

// Future of Work
MERGE (f32:Field {name: "Future of Work", description: ""})
MERGE
  (s196:Field
    {
      name: "Digital Work Design",
      description:
        "Redefining roles with AI, automation, and remote collaboration tools."
    })
MERGE (s196)-[:SUBFIELD_OF]->(f32)
MERGE
  (s197:Field
    {
      name: "New Work Models",
      description:
        "Hybrid work, gig economy platforms, and decentralized autonomous organizations (DAOs)."
    })
MERGE (s197)-[:SUBFIELD_OF]->(f32)
MERGE
  (s198:Field
    {
      name: "Social Protection",
      description:
        "Updating unemployment benefits, healthcare, and pensions for non-traditional workers."
    })
MERGE (s198)-[:SUBFIELD_OF]->(f32)
MERGE
  (s199:Field
    {
      name: "Reskilling",
      description:
        "Training programs to transition workers into tech and green economy roles."
    })
MERGE (s199)-[:SUBFIELD_OF]->(f32)
MERGE
  (s200:Field
    {
      name: "Inclusive Labour Markets",
      description:
        "Removing barriers for women, disabled individuals, and migrants."
    })
MERGE (s200)-[:SUBFIELD_OF]->(f32)
MERGE
  (s201:Field
    {
      name: "Job Creation and Entrepreneurship",
      description:
        "Supporting startups and innovation to offset automation-driven job losses."
    })
MERGE (s201)-[:SUBFIELD_OF]->(f32)

// Blockchain
MERGE (f33:Field {name: "Blockchain", description: ""})
MERGE
  (s202:Field
    {
      name: "Blockchain and Cryptocurrency Climate Impact",
      description:
        "Addressing energy consumption of PoW systems and promoting eco-friendly alternatives."
    })
MERGE (s202)-[:SUBFIELD_OF]->(f33)
MERGE
  (s203:Field
    {
      name: "Blockchain and Leveraging Data",
      description:
        "Using decentralized ledgers for secure, transparent data sharing in supply chains."
    })
MERGE (s203)-[:SUBFIELD_OF]->(f33)
MERGE
  (s204:Field
    {
      name: "Blockchain Policy, Regulation and Law",
      description:
        "Balancing innovation with anti-money laundering (AML) and consumer protection laws."
    })
MERGE (s204)-[:SUBFIELD_OF]->(f33)
MERGE
  (s205:Field
    {
      name: "Tokenization and Digital Assets",
      description:
        "Representing real-world assets like real estate or art as blockchain tokens."
    })
MERGE (s205)-[:SUBFIELD_OF]->(f33)
MERGE
  (s206:Field
    {
      name: "Blockchain, Security and Interoperability",
      description:
        "Improving cross-platform compatibility and defending against smart contract vulnerabilities."
    })
MERGE (s206)-[:SUBFIELD_OF]->(f33)
MERGE
  (s207:Field
    {
      name: "Smart Contracts and Automation",
      description:
        "Self-executing agreements reducing reliance on intermediaries."
    })
MERGE (s207)-[:SUBFIELD_OF]->(f33)
MERGE
  (s208:Field
    {
      name: "Blockchain and Digital Identity",
      description:
        "Decentralized ID systems giving users control over personal data."
    })
MERGE (s208)-[:SUBFIELD_OF]->(f33)
MERGE
  (s209:Field
    {
      name: "Decentralized Governance and New Models",
      description:
        "DAOs enabling community-driven decision-making without central authorities."
    })
MERGE (s209)-[:SUBFIELD_OF]->(f33)

// Supply Chain and Transport
MERGE (f34:Field {name: "Supply Chain and Transport", description: ""})
MERGE
  (s210:Field
    {
      name: "Artificial Intelligence and Supply Chains",
      description:
        "Optimizing logistics with predictive analytics, demand forecasting, and autonomous vehicles."
    })
MERGE (s210)-[:SUBFIELD_OF]->(f34)
MERGE
  (s211:Field
    {
      name: "E-commerce and the Future of Retail",
      description:
        "Shift to online shopping and its impact on warehousing, delivery, and employment."
    })
MERGE (s211)-[:SUBFIELD_OF]->(f34)
MERGE
  (s212:Field
    {
      name: "Physical and Digital Infrastructure",
      description:
        "Integrating IoT, 5G, and automation into ports, roads, and warehouses."
    })
MERGE (s212)-[:SUBFIELD_OF]->(f34)
MERGE
  (s213:Field
    {
      name: "Labour Market Trends and Demographic Change",
      description:
        "Addressing labor shortages in logistics due to aging populations and automation."
    })
MERGE (s213)-[:SUBFIELD_OF]->(f34)
MERGE
  (s214:Field
    {
      name: "Decarbonizing Supply Chains, Logistics, and Transport",
      description:
        "Reducing emissions through electric fleets, green fuels, and circular supply models."
    })
MERGE (s214)-[:SUBFIELD_OF]->(f34)
MERGE
  (s215:Field
    {
      name: "Resilience and Adaptability",
      description:
        "Mitigating risks from geopolitical tensions, pandemics, and climate disruptions."
    })
MERGE (s215)-[:SUBFIELD_OF]->(f34)

// Quantum Economy
MERGE (f35:Field {name: "Quantum Economy", description: ""})
MERGE
  (s216:Field
    {
      name: "A Virtuous Cycle of Disruptive Innovation",
      description:
        "Quantum computing advancing fields like cryptography, materials science, and drug discovery."
    })
MERGE (s216)-[:SUBFIELD_OF]->(f35)
MERGE
  (s217:Field
    {
      name: "Building a Skilled Quantum Workforce",
      description:
        "Training physicists, engineers, and programmers for quantum research and applications."
    })
MERGE (s217)-[:SUBFIELD_OF]->(f35)
MERGE
  (s218:Field
    {
      name: "Quantum and Sustainable Development",
      description:
        "Using quantum simulations to optimize energy grids and climate models."
    })
MERGE (s218)-[:SUBFIELD_OF]->(f35)
MERGE
  (s219:Field
    {
      name: "Quantum Policy and Governance",
      description:
        "International collaboration to regulate quantum tech and prevent monopolies."
    })
MERGE (s219)-[:SUBFIELD_OF]->(f35)
MERGE
  (s220:Field
    {
      name: "Quantum, Trade and Investment",
      description:
        "Competing to dominate quantum patents, talent, and commercialization."
    })
MERGE (s220)-[:SUBFIELD_OF]->(f35)
MERGE
  (s221:Field
    {
      name: "Quantum and International Security",
      description:
        "Addressing risks of quantum decryption breaking traditional encryption standards."
    })
MERGE (s221)-[:SUBFIELD_OF]->(f35)

// Artificial Intelligence
MERGE (f36:Field {name: "Artificial Intelligence", description: ""})
MERGE
  (s222:Field
    {
      name: "Generative AI",
      description:
        "Creating text, images, and code using models like GPT and diffusion networks."
    })
MERGE (s222)-[:SUBFIELD_OF]->(f36)
MERGE
  (s223:Field
    {
      name: "Bias and Fairness in AI Algorithms",
      description:
        "Mitigating discriminatory outcomes in hiring, lending, and criminal justice systems."
    })
MERGE (s223)-[:SUBFIELD_OF]->(f36)
MERGE
  (s224:Field
    {
      name: "AI and Jobs",
      description:
        "Automating tasks while creating new roles in AI oversight and development."
    })
MERGE (s224)-[:SUBFIELD_OF]->(f36)
MERGE
  (s225:Field
    {
      name: "Can AI Overcome its Limitations?",
      description:
        "Debating AI's ability to achieve true understanding or creativity."
    })
MERGE (s225)-[:SUBFIELD_OF]->(f36)
MERGE
  (s226:Field
    {
      name: "Geopolitical Impacts of AI",
      description:
        "AI arms races, surveillance tools, and economic competitiveness."
    })
MERGE (s226)-[:SUBFIELD_OF]->(f36)
MERGE
  (s227:Field
    {
      name: "Responsible AI",
      description:
        "Frameworks for transparency, accountability, and ethical deployment."
    })
MERGE (s227)-[:SUBFIELD_OF]->(f36)
MERGE
  (s228:Field
    {
      name: "AI, Diversity, and Inclusion Operationalizing",
      description:
        "Ensuring diverse voices shape AI development to avoid exclusionary outcomes."
    })
MERGE (s228)-[:SUBFIELD_OF]->(f36)
MERGE
  (s229:Field
    {
      name: "AI for What Purpose?",
      description:
        "Aligning AI goals with societal values rather than profit or control."
    })
MERGE (s229)-[:SUBFIELD_OF]->(f36)

// Peace and Resilience
MERGE (f37:Field {name: "Peace and Resilience", description: ""})
MERGE
  (s230:Field
    {
      name: "Global Governance and Maintaining Peace",
      description:
        "Strengthening institutions like the UN to prevent conflicts and mediate disputes."
    })
MERGE (s230)-[:SUBFIELD_OF]->(f37)
MERGE
  (s231:Field
    {
      name: "Trust and Locally-Owned Solutions",
      description:
        "Empowering communities to design peacebuilding initiatives tailored to their contexts."
    })
MERGE (s231)-[:SUBFIELD_OF]->(f37)
MERGE
  (s232:Field
    {
      name: "A Voice for the Young",
      description:
        "Involving youth in peace processes and post-conflict reconstruction."
    })
MERGE (s232)-[:SUBFIELD_OF]->(f37)
MERGE
  (s233:Field
    {
      name: "Social Cohesion and Civic Participation",
      description: "Fostering dialogue and inclusion to heal divided societies."
    })
MERGE (s233)-[:SUBFIELD_OF]->(f37)
MERGE
  (s234:Field
    {
      name: "Human Rights and Peace",
      description:
        "Linking peace efforts to justice, equality, and protection of marginalized groups."
    })
MERGE (s234)-[:SUBFIELD_OF]->(f37)
MERGE
  (s235:Field
    {
      name: "Peace and Human Development",
      description:
        "Linking peacebuilding to poverty reduction, education, and healthcare access."
    })
MERGE (s235)-[:SUBFIELD_OF]->(f37)
MERGE
  (s236:Field
    {
      name: "Humanitarian Action in Response to Conflict",
      description:
        "Providing aid while navigating political and security challenges."
    })
MERGE (s236)-[:SUBFIELD_OF]->(f37)
MERGE
  (s237:Field
    {
      name: "Inclusive Peace Processes",
      description:
        "Ensuring women, minorities, and displaced persons participate in negotiations."
    })
MERGE (s237)-[:SUBFIELD_OF]->(f37)

// Geoeconomics
MERGE (f38:Field {name: "Geoeconomics", description: ""})
MERGE
  (s238:Field
    {
      name: "Economic and Technological Power Transition",
      description:
        "Shifting dominance from Western economies to emerging markets like Asia."
    })
MERGE (s238)-[:SUBFIELD_OF]->(f38)
MERGE
  (s239:Field
    {
      name: "Resilience and Supply Chain Security",
      description:
        "Diversifying manufacturing to reduce reliance on single-source suppliers."
    })
MERGE (s239)-[:SUBFIELD_OF]->(f38)
MERGE
  (s240:Field
    {
      name: "Economic Decoupling and Balkanization",
      description:
        "Fragmentation of global trade due to geopolitical rivalries and sanctions."
    })
MERGE (s240)-[:SUBFIELD_OF]->(f38)
MERGE
  (s241:Field
    {
      name: "Securing Economics",
      description:
        "Protecting critical industries from foreign interference and cyberattacks."
    })
MERGE (s241)-[:SUBFIELD_OF]->(f38)
MERGE
  (s242:Field
    {
      name: "Technological Containment",
      description:
        "Restricting access to advanced tech (e.g., semiconductors) to limit rivals' growth."
    })
MERGE (s242)-[:SUBFIELD_OF]->(f38)
MERGE
  (s243:Field
    {
      name: "Economic Coercion",
      description:
        "Using trade, tariffs, and aid as leverage in international relations."
    })
MERGE (s243)-[:SUBFIELD_OF]->(f38)
MERGE
  (s244:Field
    {
      name: "Localization and Sovereignty",
      description:
        "Prioritizing domestic production and data storage to reduce foreign dependencies."
    })
MERGE (s244)-[:SUBFIELD_OF]->(f38)

// Space
MERGE (f39:Field {name: "Space", description: ""})
MERGE
  (s246:Field
    {
      name: "Education and Research",
      description:
        "Collaborating on space science to advance knowledge in physics, astronomy, and planetary defense."
    })
MERGE (s246)-[:SUBFIELD_OF]->(f39)
MERGE
  (s247:Field
    {
      name: "Space Sustainability",
      description:
        "Addressing orbital debris and regulating satellite mega-constellations."
    })
MERGE (s247)-[:SUBFIELD_OF]->(f39)
MERGE
  (s248:Field
    {
      name: "Space Security",
      description:
        "Preventing weaponization of space and establishing norms for responsible behavior."
    })
MERGE (s248)-[:SUBFIELD_OF]->(f39)
MERGE
  (s249:Field
    {
      name: "Space Commercialization",
      description:
        "Private sector ventures in satellite internet, mining, and tourism."
    })
MERGE (s249)-[:SUBFIELD_OF]->(f39)
MERGE
  (s250:Field
    {
      name: "Space Exploration",
      description:
        "Missions to the Moon, Mars, and beyond for scientific discovery and resource assessment."
    })
MERGE (s250)-[:SUBFIELD_OF]->(f39)
MERGE
  (s251:Field
    {
      name: "Space Policy",
      description:
        "International agreements governing space activities, such as the Artemis Accords."
    })
MERGE (s251)-[:SUBFIELD_OF]->(f39)
MERGE
  (s252:Field
    {
      name: "Socio-economic Benefits",
      description:
        "Spin-off technologies improving Earth-based industries like agriculture and healthcare."
    })
MERGE (s252)-[:SUBFIELD_OF]->(f39)
MERGE
  (s253:Field
    {
      name: "Climate and Nature",
      description:
        "Using satellite data to monitor deforestation, ice melt, and natural disasters."
    })
MERGE (s253)-[:SUBFIELD_OF]->(f39)

// Retail, Consumer Goods and Lifestyle
MERGE
  (f40:Field {name: "Retail, Consumer Goods and Lifestyle", description: ""})
MERGE
  (s254:Field
    {
      name: "New Patterns of Consumption",
      description:
        "Shift toward experiential spending, rental models, and conscious consumerism."
    })
MERGE (s254)-[:SUBFIELD_OF]->(f40)
MERGE
  (s255:Field
    {
      name: "Inconspicuous Consumption",
      description:
        "Preference for minimalist, sustainable products over status-driven purchases."
    })
MERGE (s255)-[:SUBFIELD_OF]->(f40)
MERGE
  (s256:Field
    {
      name: "The Global Luxury Market",
      description:
        "Resilience of high-end fashion, watches, and art amid economic fluctuations."
    })
MERGE (s256)-[:SUBFIELD_OF]->(f40)
MERGE
  (s257:Field
    {
      name: "Global Middle Class Consumers",
      description:
        "Growing demand for quality goods and services in emerging markets."
    })
MERGE (s257)-[:SUBFIELD_OF]->(f40)
MERGE
  (s258:Field
    {
      name: "Artisanal Production",
      description:
        "Revival of handmade, locally sourced products in response to mass manufacturing."
    })
MERGE (s258)-[:SUBFIELD_OF]->(f40)

// Illicit Economy
MERGE (f41:Field {name: "Illicit Economy", description: ""})
MERGE
  (s259:Field
    {
      name: "Cybercrime",
      description:
        "Online fraud, ransomware, and phishing schemes exploiting digital vulnerabilities."
    })
MERGE (s259)-[:SUBFIELD_OF]->(f41)
MERGE
  (s260:Field
    {
      name: "Cybercrime and Connectivity",
      description:
        "Expanding attack surfaces due to IoT proliferation and weak device security."
    })
MERGE (s260)-[:SUBFIELD_OF]->(f41)
MERGE
  (s261:Field
    {
      name: "Corruption and Impunity",
      description:
        "Bribery and embezzlement undermining justice systems and anti-crime efforts."
    })
MERGE (s261)-[:SUBFIELD_OF]->(f41)
MERGE
  (s262:Field
    {
      name: "Crime and the Environment",
      description:
        "Illegal logging, fishing, and wildlife trafficking depleting natural resources."
    })
MERGE (s262)-[:SUBFIELD_OF]->(f41)
MERGE
  (s263:Field
    {
      name: "Violence and Instability",
      description:
        "Criminal networks fueling conflict, trafficking, and organized violence."
    })
MERGE (s263)-[:SUBFIELD_OF]->(f41)
MERGE
  (s264:Field
    {
      name: "Illicit Trade and Financial Flow",
      description:
        "Smuggling, counterfeiting, and money laundering evading customs and sanctions."
    })
MERGE (s264)-[:SUBFIELD_OF]->(f41)
MERGE
  (s265:Field
    {
      name: "Human Mobility and Exploitation",
      description:
        "Forced labor, human trafficking, and exploitation in migration routes."
    })
MERGE (s265)-[:SUBFIELD_OF]->(f41)

// Agriculture and Food Security
MERGE (f42:Field {name: "Agriculture and Food Security", description: ""})
MERGE
  (s266:Field
    {
      name: "Precision Agriculture and Smart Farming",
      description:
        "Using drones, sensors, and AI to optimize crop yields and resource use."
    })
MERGE (s266)-[:SUBFIELD_OF]->(f42)
MERGE
  (s267:Field
    {
      name: "Agricultural IoT Systems",
      description:
        "Monitoring soil health, livestock, and weather via connected devices."
    })
MERGE (s267)-[:SUBFIELD_OF]->(f42)
MERGE
  (s268:Field
    {
      name: "Genetic and Biological Data",
      description:
        "Advancing crop resilience and nutrition through genomic research."
    })
MERGE (s268)-[:SUBFIELD_OF]->(f42)
MERGE
  (s269:Field
    {
      name: "Agricultural Infrastructure",
      description:
        "Modernizing storage, irrigation, and supply chains to reduce waste."
    })
MERGE (s269)-[:SUBFIELD_OF]->(f42)

// Health and Life Sciences
MERGE (f43:Field {name: "Health and Life Sciences", description: ""})
MERGE
  (s270:Field
    {
      name: "Health Data and Electronic Records",
      description:
        "Digitizing patient information for better care coordination and research."
    })
MERGE (s270)-[:SUBFIELD_OF]->(f43)
MERGE
  (s271:Field
    {
      name: "Biomedical Devices",
      description:
        "Wearables and implants improving diagnostics, treatment, and chronic disease management."
    })
MERGE (s271)-[:SUBFIELD_OF]->(f43)
MERGE
  (s272:Field
    {
      name: "Genomic Data",
      description:
        "Personalized medicine based on genetic profiling and CRISPR editing."
    })
MERGE (s272)-[:SUBFIELD_OF]->(f43)
MERGE
  (s273:Field
    {
      name: "Telemedicine Security and Trust",
      description:
        "Protecting patient privacy while expanding remote healthcare access."
    })
MERGE (s273)-[:SUBFIELD_OF]->(f43)
MERGE
  (s274:Field
    {
      name: "AI in Diagnostics",
      description:
        "Machine learning models detecting diseases like cancer earlier and more accurately."
    })
MERGE (s274)-[:SUBFIELD_OF]->(f43)
MERGE
  (s275:Field
    {
      name: "Hospital Infrastructure",
      description:
        "Upgrading facilities with IoT, cybersecurity, and energy-efficient systems."
    })
MERGE (s275)-[:SUBFIELD_OF]->(f43)

// Manufacturing and Industry 4.0
MERGE (f44:Field {name: "Manufacturing and Industry 4.0", description: ""})
MERGE
  (s276:Field
    {
      name: "Smart Factory and Industrial IoT",
      description:
        "Automating production with connected machines and real-time analytics."
    })
MERGE (s276)-[:SUBFIELD_OF]->(f44)
MERGE
  (s277:Field
    {
      name: "OT/IT Integration",
      description:
        "Converging operational technology with IT systems for improved efficiency."
    })
MERGE (s277)-[:SUBFIELD_OF]->(f44)
MERGE
  (s278:Field
    {
      name: "Digital Twins and Data Integrity",
      description:
        "Virtual replicas of physical systems for simulation and troubleshooting."
    })
MERGE (s278)-[:SUBFIELD_OF]->(f44)
MERGE
  (s279:Field
    {
      name: "Additive Manufacturing",
      description:
        "3D printing enabling on-demand production and reduced material waste."
    })
MERGE (s279)-[:SUBFIELD_OF]->(f44)
MERGE
  (s280:Field
    {
      name: "Industrial Systems",
      description:
        "Modernizing legacy manufacturing with AI, robotics, and edge computing."
    })
MERGE (s280)-[:SUBFIELD_OF]->(f44)

// Environment and Climate Action
MERGE (f45:Field {name: "Environment and Climate Action", description: ""})
MERGE
  (s281:Field
    {
      name: "Environmental Monitoring Systems",
      description:
        "Using satellites and sensors to track air quality, deforestation, and emissions."
    })
MERGE (s281)-[:SUBFIELD_OF]->(f45)
MERGE
  (s282:Field
    {
      name: "Climate Models",
      description:
        "AI-driven simulations predicting climate impacts and policy effectiveness."
    })
MERGE (s282)-[:SUBFIELD_OF]->(f45)
MERGE
  (s283:Field
    {
      name: "Natural Resource Infrastructure",
      description:
        "Sustainable management of water, minerals, and forests through tech-enabled monitoring."
    })
MERGE (s283)-[:SUBFIELD_OF]->(f45)
MERGE
  (s284:Field
    {
      name: "Climate Tech",
      description:
        "Innovations in carbon capture, renewable energy, and green hydrogen."
    })
MERGE (s284)-[:SUBFIELD_OF]->(f45)
MERGE
  (s285:Field
    {
      name: "Environmental Activism and Online Surveillance",
      description:
        "Balancing digital tools for advocacy with risks to activists' privacy and safety."
    })
MERGE (s285)-[:SUBFIELD_OF]->(f45)

// Transportation and Logistics
MERGE (f46:Field {name: "Transportation and Logistics", description: ""})
MERGE
  (s286:Field
    {
      name: "Autonomous Vehicles",
      description:
        "Self-driving cars, trucks, and drones reshaping freight and passenger transport."
    })
MERGE (s286)-[:SUBFIELD_OF]->(f46)
MERGE
  (s287:Field
    {
      name: "Smart Traffic Management Systems",
      description:
        "AI optimizing traffic flow and reducing congestion in cities."
    })
MERGE (s287)-[:SUBFIELD_OF]->(f46)
MERGE
  (s288:Field
    {
      name: "Aviation and Maritime",
      description:
        "Decarbonizing airlines and shipping through alternative fuels and electrification."
    })
MERGE (s288)-[:SUBFIELD_OF]->(f46)
MERGE
  (s289:Field
    {
      name: "Supply Chain",
      description:
        "Streamlining logistics with blockchain, AI, and IoT for transparency and efficiency."
    })
MERGE (s289)-[:SUBFIELD_OF]->(f46)
MERGE
  (s290:Field
    {
      name: "Rail and Public Transit",
      description:
        "Investing in high-speed rail and electric buses for sustainable urban mobility."
    })
MERGE (s290)-[:SUBFIELD_OF]->(f46)

// Energy and Utilities
MERGE (f47:Field {name: "Energy and Utilities", description: ""})
MERGE
  (s291:Field
    {
      name: "Smart Grids and Critical Infrastructure",
      description:
        "Modernizing power grids with IoT, AI, and cybersecurity measures."
    })
MERGE (s291)-[:SUBFIELD_OF]->(f47)
MERGE
  (s292:Field
    {
      name: "Renewable Energy Systems",
      description:
        "Scaling solar, wind, and geothermal energy to replace fossil fuels."
    })
MERGE (s292)-[:SUBFIELD_OF]->(f47)
MERGE
  (s293:Field
    {
      name: "Securing Digital Oil & Gas Operations",
      description:
        "Protecting legacy infrastructure from cyberattacks during energy transitions."
    })
MERGE (s293)-[:SUBFIELD_OF]->(f47)
MERGE
  (s294:Field
    {
      name: "Energy Storage",
      description:
        "Advancements in batteries and grid-scale storage to stabilize renewables."
    })
MERGE (s294)-[:SUBFIELD_OF]->(f47)
MERGE
  (s295:Field
    {
      name: "IoT Sensors in Utilities",
      description:
        "Monitoring water, gas, and electricity usage for efficiency and leak detection."
    })
MERGE (s295)-[:SUBFIELD_OF]->(f47)

// Education Systems
MERGE (f48:Field {name: "Education Systems", description: ""})
MERGE
  (s296:Field
    {
      name: "EdTech Platforms",
      description:
        "Digital tools like LMS and AI tutors personalizing learning experiences."
    })
MERGE (s296)-[:SUBFIELD_OF]->(f48)
MERGE
  (s297:Field
    {
      name: "Student Data Privacy",
      description:
        "Safeguarding information collected by educational apps and online platforms."
    })
MERGE (s297)-[:SUBFIELD_OF]->(f48)
MERGE
  (s298:Field
    {
      name: "Digital Infrastructure in Schools",
      description:
        "Providing devices, broadband, and training for equitable access."
    })
MERGE (s298)-[:SUBFIELD_OF]->(f48)
MERGE
  (s299:Field
    {
      name: "Cyber Literacy and Security Awareness",
      description:
        "Teaching safe online practices and digital citizenship from an early age."
    })
MERGE (s299)-[:SUBFIELD_OF]->(f48)
MERGE
  (s300:Field
    {
      name: "Remote Learning Platforms",
      description:
        "Ensuring continuity of education during crises through virtual classrooms."
    })
MERGE (s300)-[:SUBFIELD_OF]->(f48)

// Tourism and Hospitality
MERGE (f49:Field {name: "Tourism and Hospitality", description: ""})
MERGE
  (s301:Field
    {
      name: "Guest Data and Payment Systems",
      description:
        "Securing personal information and transactions in hotels and travel booking."
    })
MERGE (s301)-[:SUBFIELD_OF]->(f49)
MERGE
  (s302:Field
    {
      name: "IoT in Smart Hotels",
      description:
        "Automating check-ins, energy management, and guest services via connected devices."
    })
MERGE (s302)-[:SUBFIELD_OF]->(f49)
MERGE
  (s303:Field
    {
      name: "Airline and Booking Systems",
      description:
        "Efficient reservation platforms and biometric airport security."
    })
MERGE (s303)-[:SUBFIELD_OF]->(f49)
MERGE
  (s304:Field
    {
      name: "Cybercrime in the Travel Industry",
      description:
        "Phishing, fake websites, and ransomware targeting travelers and providers."
    })
MERGE (s304)-[:SUBFIELD_OF]->(f49)
MERGE
  (s305:Field
    {
      name: "Crisis Response in Cyberattacks on Tourism",
      description:
        "Plans to mitigate service disruptions and protect customer data."
    })
MERGE (s305)-[:SUBFIELD_OF]->(f49)

// Humanitarian and Development Aid
MERGE (f50:Field {name: "Humanitarian and Development Aid", description: ""})
MERGE
  (s306:Field
    {
      name: "Protecting Beneficiary Data",
      description:
        "Ensuring privacy of aid recipients in conflict zones and refugee camps."
    })
MERGE (s306)-[:SUBFIELD_OF]->(f50)
MERGE
  (s307:Field
    {
      name: "Cybersecurity in NGO and UN Systems",
      description:
        "Defending against attacks disrupting humanitarian operations."
    })
MERGE (s307)-[:SUBFIELD_OF]->(f50)
MERGE
  (s308:Field
    {
      name: "Information Integrity in Crisis Zones",
      description: "Countering misinformation during disasters and conflicts."
    })
MERGE (s308)-[:SUBFIELD_OF]->(f50)
MERGE
  (s309:Field
    {
      name: "Mobile Payments and Aid Security",
      description:
        "Using digital currencies to distribute aid securely and transparently."
    })
MERGE (s309)-[:SUBFIELD_OF]->(f50)
MERGE
  (s310:Field
    {
      name: "Conflict-Sensitive Cyber Operations",
      description:
        "Avoiding digital collateral damage in humanitarian tech deployments."
    })
MERGE (s310)-[:SUBFIELD_OF]->(f50)

// Sports and Entertainment
MERGE (f51:Field {name: "Sports and Entertainment", description: ""})
MERGE
  (s311:Field
    {
      name: "Securing Major Event Infrastructure",
      description:
        "Cybersecurity for stadiums, ticketing, and broadcast systems during events."
    })
MERGE (s311)-[:SUBFIELD_OF]->(f51)
MERGE
  (s312:Field
    {
      name: "Online Piracy and IP Protection",
      description:
        "Combating illegal streaming and distribution of sports and entertainment content."
    })
MERGE (s312)-[:SUBFIELD_OF]->(f51)
MERGE
  (s313:Field
    {
      name: "Player Data and Biometric Privacy",
      description: "Ethical use of athlete health and performance data."
    })
MERGE (s313)-[:SUBFIELD_OF]->(f51)
MERGE
  (s314:Field
    {
      name: "Esports Platforms",
      description:
        "Regulating competitive gaming for fairness, security, and inclusivity."
    })
MERGE (s314)-[:SUBFIELD_OF]->(f51)
MERGE
  (s315:Field
    {
      name: "Ticketing Fraud and Digital Scalping",
      description:
        "Using blockchain and AI to prevent bot-driven ticket hoarding."
    })
MERGE (s315)-[:SUBFIELD_OF]->(f51)

// Culture and Heritage
MERGE (f52:Field {name: "Culture and Heritage", description: ""})
MERGE
  (s316:Field
    {
      name: "Digital Archives",
      description:
        "Preserving historical records, languages, and artifacts in digital formats."
    })
MERGE (s316)-[:SUBFIELD_OF]->(f52)
MERGE
  (s317:Field
    {
      name: "Virtual Museums and Collections",
      description:
        "3D scans and VR tours making cultural heritage accessible globally."
    })
MERGE (s317)-[:SUBFIELD_OF]->(f52)
MERGE
  (s318:Field
    {
      name: "Cultural Institutions",
      description:
        "Modernizing museums, libraries, and theaters with interactive tech."
    })
MERGE (s318)-[:SUBFIELD_OF]->(f52)
MERGE
  (s319:Field
    {
      name: "Data Ethics in Cultural Analytics",
      description:
        "Using AI to study cultural trends without reinforcing biases."
    })
MERGE (s319)-[:SUBFIELD_OF]->(f52)
MERGE
  (s320:Field
    {
      name: "Heritage in Conflict Zones",
      description: "Protecting monuments and traditions from war and looting."
    })
MERGE (s320)-[:SUBFIELD_OF]->(f52)

// Small and Medium Enterprises (SMEs)
MERGE (f53:Field {name: "Small and Medium Enterprises (SMEs)", description: ""})
MERGE
  (s321:Field
    {
      name: "Affordable Cybersecurity Solutions",
      description:
        "Cost-effective tools to protect SMEs from ransomware and data breaches."
    })
MERGE (s321)-[:SUBFIELD_OF]->(f53)
MERGE
  (s322:Field
    {
      name: "Cyber Insurance for SMEs",
      description:
        "Coverage for financial losses from cyberattacks and recovery costs."
    })
MERGE (s322)-[:SUBFIELD_OF]->(f53)
MERGE
  (s323:Field
    {
      name: "Awareness and Capacity Building",
      description:
        "Training programs to improve digital security practices among small businesses."
    })
MERGE (s323)-[:SUBFIELD_OF]->(f53)
MERGE
  (s324:Field
    {
      name: "Threats to Digital Entrepreneurs",
      description:
        "Challenges from big tech monopolies, regulatory burdens, and cybercrime."
    })
MERGE (s324)-[:SUBFIELD_OF]->(f53)
MERGE
  (s325:Field
    {
      name: "Data Protection for Customer-Centric Businesses",
      description: "Helping SMEs comply with GDPR and other privacy laws."
    })
MERGE (s325)-[:SUBFIELD_OF]->(f53)