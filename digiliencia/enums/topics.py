from enum import Enum


class Topics(str, Enum):
    """Enumeración de tópicos disponibles (refleja los creados vía Cypher)."""

    ADWARE = "Adware"
    BOTNET = "Botnet"
    CYBERBULLYING = "Cyberbullying"
    CYBERSQUATTING = "Cybersquatting"
    DEEPFAKE = "Deepfake"
    DEFACEMENT = "Defacement"
    GROOMING = "Grooming"
    JAILBREAKING = "Jailbreaking"
    MALVERTISING = "Malvertising"
    MALWARE = "Malware"
    MAN_IN_THE_MIDDLE = "Man-in-the-middle"
    PENTESTING = "Pentesting"
    PHISHING = "Phishing"
    PRETEXTING = "Pretexting"
    RANSOMWARE = "Ransomware"
    ROOTING = "Rooting"
    SEXTING = "Sexting"
    SEXTORSION = "Sextorsion"
    SMISHING = "Smishing"
    SOCIAL_ENGINEERING = "Social engineering"
    SPEAR_PHISHING = "Spear phishing"
    SPYWARE = "Spyware"
    TYPOSQUATTING = "Typosquatting"
    VISHING = "Vishing"
    VULNERABILITY = "Vulnerability"
    WARSHIPPING = "Warshipping"

# Conjunto precomputado para validaciones O(1)
TOPIC_VALUES: set[str] = {t.value for t in Topics}

def is_valid_topic(value: str) -> bool:
    """Devuelve True si el valor está en la enumeración Topics."""
    return value in TOPIC_VALUES

