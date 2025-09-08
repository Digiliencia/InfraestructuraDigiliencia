from enum import Enum
from typing import Set, Dict, Optional


class RelatedFields:
    class InternetGovernance(str, Enum):
        ONLINE_SURVEILLANCE = "Online Surveillance"
        PRIVACY_FORENSICS = "Privacy Forensics"
        PREVENTING_ONLINE_CRIME = "Preventing Online Crime"
        EXPANDING_ACCESS = "Expanding Access"
        IDENTITY_MANAGEMENT = "Identity Management"
        USER_RIGHTS_AND_CENSORSHIP = "User Rights and Censorship"
        DATA_PROTECTION = "Data Protection"

    class Corruption(str, Enum):
        VICTIMS_AND_HARMS = "Victims and Harms"
        TECH_FOR_INTEGRITY = "Tech for Integrity"
        FAIR_ALLOCATION = "Fair Allocation of Resources and Power"
        INSECURITY_AND_STATE_CAPTURE = "Insecurity and State Capture"
        INTEGRITY_AND_TRUST = "Integrity, Trust and Good Governance"
        EFFECTIVE_LAW_ENFORCEMENT = "Effective Law Enforcement"
        GLOBAL_COLLECTIVE_ACTION = "Global and Collective Action"
        CORRUPT_CAPITAL_FLOWS = "Corrupt Capital Flows"

    class BankingAndCapitalMarkets(str, Enum):
        SUSTAINABILITY_AND_FINANCE = "Sustainability and Finance"
        THE_FINANCIAL_RISK_LANDSCAPE = "The Financial Risk Landscape"
        FINANCIAL_TECHNOLOGY = "Financial Technology"
        BANKING_BUSINESS_MODELS = "Banking Business Models"
        FINANCIAL_TALENT = "Financial Talent"

    class Values(str, Enum):
        TRUST_AS_A_VALUE = "Trust as a Value"
        VALUING_DIGITAL_EQUITY = "Valuing Digital Equity"
        VALUING_THE_ENVIRONMENT = "Valuing the Environment"
        THE_COMMON_GOOD = "The Common Good"
        VALUING_HUMAN_DIGNITY = "Valuing Human Dignity"

    class InternetOfThings(str, Enum):
        WIRELESS_SENSING_AND_LOCALIZATION = "Wireless Sensing and Localization"
        IOT_SECURITY_AND_PRIVACY = "IoT Security and Privacy"
        IOT_IN_NEW_DOMAINS = "IoT in New Domains"
        EDGE_AI = "Edge AI"
        BATTERY_FREE_IOT = "Battery-Free IoT"

    class Geopolitics(str, Enum):
        STRAINED_INSTITUTIONS_AND_ALLIANCES = "Strained Institutions and Alliances"
        MULTIPOLAR_MULTI_CONCEPTUAL = "Multipolar, Multi-Conceptual"
        TECHNOLOGICAL_COMPETITION = "Technological Competition"
        ENVIRONMENTAL_DANGERS = "Environmental Dangers"
        POPULISM_AND_NATIONALISM = "Populism and Nationalism"
        ECONOMIC_SHIFTS = "Economic Shifts"

    class JusticeAndLaw(str, Enum):
        FORENSIC_SCIENCE = "Forensic Science"
        ACCESS_TO_LAW_AND_JUSTICE = "Access to Law and Justice"
        SECURITY_AND_INTELLIGENCE_IN_JUSTICE = "Security and Intelligence in Justice"
        SCIENCE_AND_INNOVATION_IN_JUSTICE = "Science and Innovation in Justice"
        GOVERNANCE_ETHICS_AND_JUSTICE = "Governance, Ethics and Justice"
        HUMAN_DECISION_MAKING_GOVERNANCE = "Human Decision-Making Governance"
        TECHNOLOGY_AND_JUSTICE = "Technology and Justice"

    class GlobalGovernance(str, Enum):
        GEOPOLITICAL_COMPETITION = "Geopolitical Competition"
        DEMANDS_FOR_JUSTICE = "Demands for Justice"
        POLARIZING_NARRATIVES = "Polarizing Narratives"
        TECHNOLOGICAL_INDEPENDENCE = "Technological Independence"
        INSTITUTIONAL_CAPACITY = "Institutional Capacity"

    class DataScience(str, Enum):
        DATA_GENERATION_PROCESSING_AND_CURATION = (
            "Data Generation, Processing, and Curation"
        )
        DATA_LITERACY_AND_EDUCATION = "Data Literacy and Education"
        DATA_GOVERNANCE_AND_SHARING = "Data Governance and Sharing"
        DATA_AND_ALGORITHM_ETHICS = "Data and Algorithm Ethics"
        DATA_COMMUNICATION_AND_VISUALIZATION = "Data Communication and Visualization"
        DATA_ANALYSIS_AND_UNCERTAINTY_ASSESSMENT = (
            "Data Analysis and Uncertainty Assessment"
        )

    class TheDigitalEconomy(str, Enum):
        UNIVERSAL_ADOPTION_OF_AFFORDABLE_DIGITAL_SERVICES = (
            "Universal Adoption of Affordable Digital Services"
        )
        CROSS_BORDER_TRADE_AND_COOPERATION = "Cross-Border Trade and Cooperation"
        TRUST_SECURITY_AND_PROTECTION = "Trust, Security, and Protection"
        STRATEGIC_DEVELOPMENT_OF_NEW_TECHNOLOGIES = (
            "Strategic Development of New Technologies"
        )
        DIGITAL_SKILLS_AND_HUMAN_CAPITAL = "Digital Skills and Human Capital"
        DIGITAL_AND_SUSTAINABILITY_TRANSFORMATION_OF_INDUSTRIES = (
            "Digital and Sustainability Transformation of Industries"
        )

    class AgileGovernance(str, Enum):
        MANAGING_TECHNOLOGYS_IMPACT = "Managing Technology's Impact"
        MANAGING_UNCERTAINTY = "Managing Uncertainty"
        THE_IMPORTANCE_OF_VALUES_IN_GOVERNING = "The Importance of Values in Governing"
        GOVERNING_FOR_THE_ENVIRONMENT = "Governing for the Environment"
        MULTI_STAKEHOLDER_COLLABORATION = "Multi-Stakeholder Collaboration"
        GOVERNING_COMMUNICATION_CHAOS = "Governing Communication Chaos"
        MAKING_MULTILATERALISM_MORE_EFFECTIVE = "Making Multilateralism More Effective"

    class EuropeanUnion(str, Enum):
        THE_EUS_GREEN_TRANSITION = "The EU's Green Transition"
        THE_EUS_GEOPOLITICAL_POSITION = "The EU's Geopolitical Position"
        THE_EUS_DEFENSE_AND_SECURITY_POLICY = "The EU's Defense and Security Policy"
        SOCIAL_INVESTMENT_AND_FISCAL_UNION = "Social Investment and Fiscal Union"
        DEMOCRATIC_PARTICIPATION = "Democratic Participation"
        AI_AND_CHALLENGES_FOR_DEMOCRACY = "AI and Challenges for Democracy"
        MIGRATION_TO_THE_EU = "Migration to the EU"
        STRATEGIC_AUTONOMY_DE_RISKING_AND_TRADE = (
            "Strategic Autonomy, De-risking and Trade"
        )

    class FutureOfConsumption(str, Enum):
        INCLUSIVE_CONSUMPTION = "Inclusive Consumption"
        GOVERNMENT_POLICY_AND_CONSUMPTION = "Government Policy and Consumption"
        CONSUMPTION_AND_EMPOWERED_CONSUMERS = "Consumption and Empowered Consumers"
        CONSUMER_TRUST_AND_TRANSPARENCY = "Consumer Trust and Transparency"
        ENVIRONMENTALLY_SUSTAINABLE_CONSUMERISM = (
            "Environmentally-Sustainable Consumerism"
        )
        CONSUMER_WELL_BEING = "Consumer Well-Being"

    class CorporateGovernance(str, Enum):
        WORKPLACE_CULTURE_AND_INCENTIVES = "Workplace Culture and Incentives"
        PURPOSE_DRIVEN_STRATEGY_AND_CAPITAL_ALLOCATION = (
            "Purpose-Driven Strategy and Capital Allocation"
        )
        TECH_GOVERNANCE = "Tech Governance"
        STAKEHOLDER_ENGAGEMENT_AND_CULTIVATING_TRUST = (
            "Stakeholder Engagement and Cultivating Trust"
        )
        VALUES_ETHICS_AND_INTEGRITY = "Values, Ethics, and Integrity"
        LEGAL_AND_REGULATORY_EVOLUTION = "Legal and Regulatory Evolution"
        INTEGRATED_OVERSIGHT_AND_DISCLOSURE = "Integrated Oversight and Disclosure"
        ENTERPRISE_AND_EMERGING_RISKS = "Enterprise and Emerging Risks"

    class SystematicRacism(str, Enum):
        ACCESS_TO_JUSTICE_AND_MASS_INCARCERATION = (
            "Access to Justice and Mass Incarceration"
        )
        ECONOMIC_OPPORTUNITY = "Economic Opportunity"
        HEALTHCARE_DISPARITIES = "Healthcare Disparities"
        EFFECTIVE_CHANGE = "Effective Change"
        CULTURAL_REINFORCEMENT_OF_RACISM = "Cultural Reinforcement of Racism"
        DEFINING_RACISM = "Defining Racism"
        ACCESS_TO_LEADERSHIP_OPPORTUNITIES = "Access to Leadership Opportunities"

    class Innovation(str, Enum):
        SOCIAL_INNOVATION = "Social Innovation"
        OPEN_INNOVATION = "Open Innovation"
        INNOVATION_ECOSYSTEMS = "Innovation Ecosystems"
        BUSINESS_MODEL_INNOVATION = "Business Model Innovation"
        TECHNOLOGY_INNOVATION = "Technology Innovation"

    class GenderInequality(str, Enum):
        ECONOMIC_OPPORTUNITY_AND_POVERTY = "Economic Opportunity and Poverty"
        GENDER_WAGE_GAPS = "Gender Wage Gaps"
        GENDER_BASED_VIOLENCE = "Gender-Based Violence"
        THE_CARE_CONUNDRUM = "The Care Conundrum"
        WOMEN_IN_CRISES = "Women in Crises"
        POLITICAL_GENDER_INEQUALITY = "Political Gender Inequality"

    class Education(str, Enum):
        CORE_SOFT_SKILLS = "Core Soft Skills"
        EDUCATION_INNOVATION = "Education Innovation"
        LIFELONG_LEARNING_PATHWAYS = "Lifelong Learning Pathways"
        QUALITY_BASIC_EDUCATION = "Quality Basic Education"
        RELEVANT_CONTINUING_EDUCATION = "Relevant Continuing Education"
        DIGITAL_FLUENCY_AND_STEM_SKILLS = "Digital Fluency and STEM Skills"

    class Leadership(str, Enum):
        ADAPTIVE_LEADERSHIP = "Adaptive Leadership"
        TECHNOLOGY_LEADERSHIP = "Technology Leadership"
        RESPONSIBILITY_AND_ACCOUNTABILITY = "Responsibility and Accountability"
        ENTREPRENEURIAL_LEADERSHIP = "Entrepreneurial Leadership"
        SYSTEMS_LEADERSHIP = "Systems Leadership"
        SHAPING_SOCIETIES = "Shaping Societies"

    class YouthPerspectives(str, Enum):
        YOUTH_MIGRATION_AND_GLOBALIZATION = "Youth, Migration, and Globalization"
        FINANCIAL_KNOW_HOW_AND_YOUTH = "Financial Know-How and Youth"
        YOUTH_EDUCATION_SKILLS_AND_EMPLOYMENT = "Youth Education, Skills and Employment"
        ENABLING_LIFELONG_HEALTH_AND_WELL_BEING = (
            "Enabling Lifelong Health and Well-Being"
        )
        YOUTH_ADDRESSING_CLIMATE_CHANGE = "Youth Addressing Climate Change"
        YOUTH_DIGITAL_PARTICIPATION = "Youth Digital Participation"

    class Mobility(str, Enum):
        MORE_SUSTAINABLE_MOBILITY = "More Sustainable Mobility"
        ENERGY_EFFICIENCY_AND_MOBILITY = "Energy Efficiency and Mobility"
        SMARTER_INFRASTRUCTURE_FOR_MOBILITY = "Smarter Infrastructure for Mobility"
        GREATER_MOBILITY_BIGGER_SECURITY_RISKS = (
            "Greater Mobility, Bigger Security Risks"
        )
        TRADE_AND_TRAVEL_BARRIERS_TO_MOBILITY = "Trade and Travel Barriers to Mobility"

    class DigitalIdentity(str, Enum):
        IDENTITY_FRAUD_AND_CYBER_RESILIENCE = "Identity Fraud and Cyber Resilience"
        THE_ECONOMIC_VALUE_OF_DIGITAL_IDENTITY = (
            "The Economic Value of Digital Identity"
        )
        DIGITAL_INCLUSION_AND_OPPORTUNITY = "Digital Inclusion and Opportunity"
        PRIVACY_AGENCY_AND_TRUST = "Privacy, Agency and Trust"
        FROM_SILOS_TO_COLLABORATION = "From Silos to Collaboration"

    class Electricity(str, Enum):
        ELECTRIC_SYSTEM_DECENTRALIZATION_AND_DIGITALIZATION = (
            "Electric System Decentralization and Digitalization"
        )
        UNIVERSAL_EQUITABLE_SUSTAINABLE_ACCESS = (
            "Universal, Equitable, Sustainable Access"
        )
        DEMAND_SIDE_ENGAGEMENT = "Demand Side Engagement"
        NETWORK_MANAGEMENT_AND_INVESTMENT = "Network Management and Investment"
        ENERGY_SECURITY_RELIABILITY_AND_RESILIENCE = (
            "Energy Security, Reliability, and Resilience"
        )
        ENERGY_SECTOR_TRANSFORMATION = "Energy Sector Transformation"
        MARKET_ENVIRONMENT_FOR_THE_ENERGY_TRANSITION = (
            "Market Environment for the Energy Transition"
        )

    class InternationalSecurity(str, Enum):
        CHANGING_POLARITY = "Changing Polarity"
        THE_TRANSFORMATION_OF_WARFARE = "The Transformation of Warfare"
        THE_RISE_OF_NON_STATE_ACTORS = "The Rise of Non-State Actors"
        GEOSTRATEGIC_COMPETITION_AND_SECURITY = "Geostrategic Competition and Security"
        THE_TECHNOLOGICAL_ARMS_RACE = "The Technological Arms Race"
        HYBRID_THREATS = "Hybrid Threats"
        DIFFUSION_OF_POWER = "Diffusion of Power"

    class Infrastructure(str, Enum):
        PRIVATE_CAPITAL_IN_INFRASTRUCTURE = "Private Capital in Infrastructure"
        INFRASTRUCTURE_RESILIENCE = "Infrastructure Resilience"
        INFRASTRUCTURE_AS_A_GEOPOLITICAL_TOOL = "Infrastructure as a Geopolitical Tool"
        THE_RISK_OF_MISMATCHING_RISK = "The Risk of Mismatching Risk"
        BANKABLE_PROJECT_PIPELINES = "Bankable Project Pipelines"
        CORRUPTION_AND_INFRASTRUCTURE = "Corruption and Infrastructure"
        SKILL_BUILDING_FOR_INFRASTRUCTURE = "Skill Building for Infrastructure"
        INFRASTRUCTURE_TECHNOLOGY_AND_INNOVATION = (
            "Infrastructure Technology and Innovation"
        )

    class NuclearSecurity(str, Enum):
        CYBER_THREATS = "Cyber Threats"
        CONFLICT_ZONES_AND_FRAGILE_STATES = "Conflict Zones and Fragile States"
        GEOPOLITICAL_TENSIONS = "Geopolitical Tensions"
        EMERGING_ECONOMIES = "Emerging Economies"
        ENERGY_INDEPENDENCE = "Energy Independence"
        DISRUPTIVE_TECHNOLOGIES = "Disruptive Technologies"

    class DigitalCommunications(str, Enum):
        FUTURE_COMMUNICATION_SYSTEMS = "Future Communication Systems"
        CONNECTIVITY_AND_COVERAGE = "Connectivity and Coverage"
        POLICY_UNCERTAINTY = "Policy Uncertainty"
        SECURE_DATA_TRANSMISSION = "Secure Data Transmission"
        SUSTAINABLE_COMMUNICATION_INFRASTRUCTURE = (
            "Sustainable Communication Infrastructure"
        )
        AN_EXPANDING_INTERNET_OF_THINGS = "An Expanding Internet of Things"

    class TheDigitalTransformationOfBusiness(str, Enum):
        NEW_DIGITAL_BUSINESS_MODELS = "New Digital Business Models"
        NEW_VALUE_AND_MARKETS = "New Value and Markets"
        THE_DIGITAL_ENTERPRISE = "The Digital Enterprise"
        SUCCESSFUL_DIGITAL_TRANSFORMATION = "Successful Digital Transformation"
        LEADING_ON_INCLUSION_SUSTAINABILITY_AND_TRUST = (
            "Leading on Inclusion, Sustainability and Trust"
        )

    class CitiesAndUrbanization(str, Enum):
        URBAN_ENVIRONMENT_AND_RESOURCES = "Urban Environment and Resources"
        URBAN_ECONOMIES = "Urban Economies"
        URBAN_DIPLOMACY = "Urban Diplomacy"
        URBAN_SOCIETY = "Urban Society"
        URBAN_RESILIENCE = "Urban Resilience"
        URBAN_INNOVATION = "Urban Innovation"
        URBAN_INFRASTRUCTURE_AND_SERVICES = "Urban Infrastructure and Services"
        URBAN_GOVERNANCE = "Urban Governance"

    class GlobalRisks(str, Enum):
        ENVIRONMENTAL_COLLAPSE = "Environmental Collapse"
        DIGITAL_POLARIZATION = "Digital Polarization"
        RISING_ECONOMIC_TENSIONS = "Rising Economic Tensions"
        GLOBAL_POWER_SHIFTS = "Global Power Shifts"
        AGEING_POPULATIONS = "Ageing Populations"
        BIOTECH_CHALLENGES = "Biotech Challenges"

    class FourthIndustrialRevolution(str, Enum):
        TECHNOLOGY_INNOVATION = "Technology Innovation"
        FRONTIER_TECHNOLOGIES = "Frontier Technologies"
        ETHICS_AND_IDENTITY = "Ethics and Identity"
        AGILE_TECHNOLOGY_GOVERNANCE = "Agile Technology Governance"
        AGENCY_AND_TRUST = "Agency and Trust"
        DISRUPTING_JOBS_DEMANDING_NEW_SKILLS = "Disrupting Jobs, Demanding New Skills"
        TECHNOLOGY_ACCESS_AND_INCLUSION = "Technology Access and Inclusion"

    class FutureOfWork(str, Enum):
        DIGITAL_WORK_DESIGN = "Digital Work Design"
        NEW_WORK_MODELS = "New Work Models"
        SOCIAL_PROTECTION = "Social Protection"
        RESKILLING = "Reskilling"
        INCLUSIVE_LABOUR_MARKETS = "Inclusive Labour Markets"
        JOB_CREATION_AND_ENTREPRENEURSHIP = "Job Creation and Entrepreneurship"

    class Blockchain(str, Enum):
        BLOCKCHAIN_AND_CRYPTOCLIMATE_IMPACT = (
            "Blockchain and Cryptocurrency Climate Impact"
        )
        BLOCKCHAIN_AND_LEVERAGING_DATA = "Blockchain and Leveraging Data"
        BLOCKCHAIN_POLICY_REGULATION_AND_LAW = "Blockchain Policy, Regulation and Law"
        TOKENIZATION_AND_DIGITAL_ASSETS = "Tokenization and Digital Assets"
        BLOCKCHAIN_SECURITY_AND_INTEROPERABILITY = (
            "Blockchain, Security and Interoperability"
        )
        SMART_CONTRACTS_AND_AUTOMATION = "Smart Contracts and Automation"
        BLOCKCHAIN_AND_DIGITAL_IDENTITY = "Blockchain and Digital Identity"
        DECENTRALIZED_GOVERNANCE_AND_NEW_MODELS = (
            "Decentralized Governance and New Models"
        )

    class SupplyChainAndTransport(str, Enum):
        ARTIFICIAL_INTELLIGENCE_AND_SUPPLY_CHAINS = (
            "Artificial Intelligence and Supply Chains"
        )
        E_COMMERCE_AND_THE_FUTURE_OF_RETAIL = "E-commerce and the Future of Retail"
        PHYSICAL_AND_DIGITAL_INFRASTRUCTURE = "Physical and Digital Infrastructure"
        LABOUR_MARKET_TRENDS_AND_DEMOGRAPHIC_CHANGE = (
            "Labour Market Trends and Demographic Change"
        )
        DECARBONIZING_SUPPLY_CHAINS_LOGISTICS_AND_TRANSPORT = (
            "Decarbonizing Supply Chains, Logistics, and Transport"
        )
        RESILIENCE_AND_ADAPTABILITY = "Resilience and Adaptability"

    class QuantumEconomy(str, Enum):
        A_VIRTUOUS_CYCLE_OF_DISRUPTIVE_INNOVATION = (
            "A Virtuous Cycle of Disruptive Innovation"
        )
        BUILDING_A_SKILLED_QUANTUM_WORKFORCE = "Building a Skilled Quantum Workforce"
        QUANTUM_AND_SUSTAINABLE_DEVELOPMENT = "Quantum and Sustainable Development"
        QUANTUM_POLICY_AND_GOVERNANCE = "Quantum Policy and Governance"
        QUANTUM_TRADE_AND_INVESTMENT = "Quantum, Trade and Investment"
        QUANTUM_AND_INTERNATIONAL_SECURITY = "Quantum and International Security"

    class ArtificialIntelligence(str, Enum):
        GENERATIVE_AI = "Generative AI"
        BIAS_AND_FAIRNESS_IN_AI_ALGORITHMS = "Bias and Fairness in AI Algorithms"
        AI_AND_JOBS = "AI and Jobs"
        CAN_AI_OVERCOME_ITS_LIMITATIONS = "Can AI Overcome its Limitations?"
        GEOPOLITICAL_IMPACTS_OF_AI = "Geopolitical Impacts of AI"
        RESPONSIBLE_AI = "Responsible AI"
        AI_DIVERSITY_AND_INCLUSION_OPERATIONALIZING = (
            "AI, Diversity, and Inclusion Operationalizing"
        )
        AI_FOR_WHAT_PURPOSE = "AI for What Purpose?"

    class PeaceAndResilience(str, Enum):
        GLOBAL_GOVERNANCE_AND_MAINTAINING_PEACE = (
            "Global Governance and Maintaining Peace"
        )
        TRUST_AND_LOCALLY_OWNED_SOLUTIONS = "Trust and Locally-Owned Solutions"
        A_VOICE_FOR_THE_YOUNG = "A Voice for the Young"
        SOCIAL_COHESION_AND_CIVIC_PARTICIPATION = (
            "Social Cohesion and Civic Participation"
        )
        HUMAN_RIGHTS_AND_PEACE = "Human Rights and Peace"
        PEACE_AND_HUMAN_DEVELOPMENT = "Peace and Human Development"
        HUMANITARIAN_ACTION_IN_RESPONSE_TO_CONFLICT = (
            "Humanitarian Action in Response to Conflict"
        )
        INCLUSIVE_PEACE_PROCESSES = "Inclusive Peace Processes"

    class Geoeconomics(str, Enum):
        ECONOMIC_AND_TECHNOLOGICAL_POWER_TRANSITION = (
            "Economic and Technological Power Transition"
        )
        RESILIENCE_AND_SUPPLY_CHAIN_SECURITY = "Resilience and Supply Chain Security"
        ECONOMIC_DECOUPLING_AND_BALKANIZATION = "Economic Decoupling and Balkanization"
        SECURING_ECONOMICS = "Securing Economics"
        TECHNOLOGICAL_CONTAINMENT = "Technological Containment"
        ECONOMIC_COERCION = "Economic Coercion"
        LOCALIZATION_AND_SOVEREIGNTY = "Localization and Sovereignty"

    class Space(str, Enum):
        EDUCATION_AND_RESEARCH = "Education and Research"
        SPACE_SUSTAINABILITY = "Space Sustainability"
        SPACE_SECURITY = "Space Security"
        SPACE_COMMERCIALIZATION = "Space Commercialization"
        SPACE_EXPLORATION = "Space Exploration"
        SPACE_POLICY = "Space Policy"
        SOCIO_ECONOMIC_BENEFITS = "Socio-economic Benefits"
        CLIMATE_AND_NATURE = "Climate and Nature"

    class RetailConsumerGoodsAndLifestyle(str, Enum):
        NEW_PATTERNS_OF_CONSUMPTION = "New Patterns of Consumption"
        INCONSPICUOUS_CONSUMPTION = "Inconspicuous Consumption"
        THE_GLOBAL_LUXURY_MARKET = "The Global Luxury Market"
        GLOBAL_MIDDLE_CLASS_CONSUMERS = "Global Middle Class Consumers"
        ARTISANAL_PRODUCTION = "Artisanal Production"

    class IllicitEconomy(str, Enum):
        CYBERCRIME = "Cybercrime"
        CYBERCRIME_AND_CONNECTIVITY = "Cybercrime and Connectivity"
        CORRUPTION_AND_IMPINITY = "Corruption and Impunity"
        CRIME_AND_THE_ENVIRONMENT = "Crime and the Environment"
        VIOLENCE_AND_INSTABILITY = "Violence and Instability"
        ILLICIT_TRADE_AND_FINANCIAL_FLOW = "Illicit Trade and Financial Flow"
        HUMAN_MOBILITY_AND_EXPLOITATION = "Human Mobility and Exploitation"

    class AgricultureAndFoodSecurity(str, Enum):
        PRECISION_AGRICULTURE_AND_SMART_FARMING = (
            "Precision Agriculture and Smart Farming"
        )
        AGRICULTURAL_IOT_SYSTEMS = "Agricultural IoT Systems"
        GENETIC_AND_BIOLOGICAL_DATA = "Genetic and Biological Data"
        AGRICULTURAL_INFRASTRUCTURE = "Agricultural Infrastructure"

    class HealthAndLifeSciences(str, Enum):
        HEALTH_DATA_AND_ELECTRONIC_RECORDS = "Health Data and Electronic Records"
        BIOMEDICAL_DEVICES = "Biomedical Devices"
        GENOMIC_DATA = "Genomic Data"
        TELEMEDICINE_SECURITY_AND_TRUST = "Telemedicine Security and Trust"
        AI_IN_DIAGNOSTICS = "AI in Diagnostics"
        HOSPITAL_INFRASTRUCTURE = "Hospital Infrastructure"

    class ManufacturingAndIndustry40(str, Enum):
        SMART_FACTORY_AND_INDUSTRIAL_IOT = "Smart Factory and Industrial IoT"
        OT_IT_INTEGRATION = "OT/IT Integration"
        DIGITAL_TWINS_AND_DATA_INTEGRITY = "Digital Twins and Data Integrity"
        ADDITIVE_MANUFACTURING = "Additive Manufacturing"
        INDUSTRIAL_SYSTEMS = "Industrial Systems"

    class EnvironmentAndClimateAction(str, Enum):
        ENVIRONMENTAL_MONITORING_SYSTEMS = "Environmental Monitoring Systems"
        CLIMATE_MODELS = "Climate Models"
        NATURAL_RESOURCE_INFRASTRUCTURE = "Natural Resource Infrastructure"
        CLIMATE_TECH = "Climate Tech"
        ENVIRONMENTAL_ACTIVISM_AND_ONLINE_SURVEILLANCE = (
            "Environmental Activism and Online Surveillance"
        )

    class TransportationAndLogistics(str, Enum):
        AUTONOMOUS_VEHICLES = "Autonomous Vehicles"
        SMART_TRAFFIC_MANAGEMENT_SYSTEMS = "Smart Traffic Management Systems"
        AVIATION_AND_MARITIME = "Aviation and Maritime"
        SUPPLY_CHAIN = "Supply Chain"
        RAIL_AND_PUBLIC_TRANSIT = "Rail and Public Transit"

    class EnergyAndUtilities(str, Enum):
        SMART_GRIDS_AND_CRITICAL_INFRASTRUCTURE = (
            "Smart Grids and Critical Infrastructure"
        )
        RENEWABLE_ENERGY_SYSTEMS = "Renewable Energy Systems"
        SECURING_DIGITAL_OIL_GAS_OPERATIONS = "Securing Digital Oil & Gas Operations"
        ENERGY_STORAGE = "Energy Storage"
        IOT_SENSORS_IN_UTILITIES = "IoT Sensors in Utilities"

    class EducationSystems(str, Enum):
        EDTECH_PLATFORMS = "EdTech Platforms"
        STUDENT_DATA_PRIVACY = "Student Data Privacy"
        DIGITAL_INFRASTRUCTURE_IN_SCHOOLS = "Digital Infrastructure in Schools"
        CYBER_LITERACY_AND_SECURITY_AWARENESS = "Cyber Literacy and Security Awareness"
        REMOTE_LEARNING_PLATFORMS = "Remote Learning Platforms"

    class TourismAndHospitality(str, Enum):
        GUEST_DATA_AND_PAYMENT_SYSTEMS = "Guest Data and Payment Systems"
        IOT_IN_SMART_HOTELS = "IoT in Smart Hotels"
        AIRLINE_AND_BOOKING_SYSTEMS = "Airline and Booking Systems"
        CYBERCRIME_IN_THE_TRAVEL_INDUSTRY = "Cybercrime in the Travel Industry"
        CRISIS_RESPONSE_IN_CYBERATTACKS_ON_TOURISM = (
            "Crisis Response in Cyberattacks on Tourism"
        )

    class HumanitarianAndDevelopmentAid(str, Enum):
        PROTECTING_BENEFICIARY_DATA = "Protecting Beneficiary Data"
        CYBERSECURITY_IN_NGO_AND_UN_SYSTEMS = "Cybersecurity in NGO and UN Systems"
        INFORMATION_INTEGRITY_IN_CRISIS_ZONES = "Information Integrity in Crisis Zones"
        MOBILE_PAYMENTS_AND_AID_SECURITY = "Mobile Payments and Aid Security"
        CONFLICT_SENSITIVE_CYBER_OPERATIONS = "Conflict-Sensitive Cyber Operations"

    class SportsAndEntertainment(str, Enum):
        SECURING_MAJOR_EVENT_INFRASTRUCTURE = "Securing Major Event Infrastructure"
        ONLINE_PIRACY_AND_IP_PROTECTION = "Online Piracy and IP Protection"
        PLAYER_DATA_AND_BIOMETRIC_PRIVACY = "Player Data and Biometric Privacy"
        ESPORTS_PLATFORMS = "Esports Platforms"
        TICKETING_FRAUD_AND_DIGITAL_SCALPING = "Ticketing Fraud and Digital Scalping"

    class CultureAndHeritage(str, Enum):
        DIGITAL_ARCHIVES = "Digital Archives"
        VIRTUAL_MUSEUMS_AND_COLLECTIONS = "Virtual Museums and Collections"
        CULTURAL_INSTITUTIONS = "Cultural Institutions"
        DATA_ETHICS_IN_CULTURAL_ANALYTICS = "Data Ethics in Cultural Analytics"
        HERITAGE_IN_CONFLICT_ZONES = "Heritage in Conflict Zones"

    class SmallAndMediumEnterprises(str, Enum):
        AFFORDABLE_CYBERSECURITY_SOLUTIONS = "Affordable Cybersecurity Solutions"
        CYBER_INSURANCE_FOR_SMEs = "Cyber Insurance for SMEs"
        AWARENESS_AND_CAPACITY_BUILDING = "Awareness and Capacity Building"
        THREATS_TO_DIGITAL_ENTREPRENEURS = "Threats to Digital Entrepreneurs"
        DATA_PROTECTION_FOR_CUSTOMER_CENTRIC_BUSINESSES = (
            "Data Protection for Customer-Centric Businesses"
        )

# --- Utilidades de agregación y validación ---

# Recolecta todas las subclases Enum declaradas dentro de RelatedFields
_RELATED_FIELD_ENUM_CLASSES = [
    getattr(RelatedFields, attr)
    for attr in dir(RelatedFields)
    if isinstance(getattr(RelatedFields, attr), type)
    and issubclass(getattr(RelatedFields, attr), Enum)
]

# Mapa categoría -> set de valores
RELATED_FIELD_VALUES_BY_CATEGORY: Dict[str, Set[str]] = {
    cls.__name__: {member.value for member in cls} for cls in _RELATED_FIELD_ENUM_CLASSES
}

# Set global con todos los valores permitidos
RELATED_FIELD_VALUES: Set[str] = set().union(*RELATED_FIELD_VALUES_BY_CATEGORY.values())

def is_valid_related_field(value: str) -> bool:
    """Devuelve True si el valor está en alguno de los enums de RelatedFields."""
    return value in RELATED_FIELD_VALUES

def all_related_field_values() -> Set[str]:
    """Retorna el set de todos los valores de campos relacionados."""
    return RELATED_FIELD_VALUES

def related_field_category(value: str) -> Optional[str]:
    """Devuelve el nombre de la categoría (enum interno) a la que pertenece el valor, o None."""
    for category, values in RELATED_FIELD_VALUES_BY_CATEGORY.items():
        if value in values:
            return category
    return None

__all__ = [
    "RelatedFields",
    "RELATED_FIELD_VALUES_BY_CATEGORY",
    "RELATED_FIELD_VALUES",
    "is_valid_related_field",
    "all_related_field_values",
    "related_field_category",
]

