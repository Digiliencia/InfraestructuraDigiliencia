// 1. Create constraints to ensure uniqueness by identifiers
CREATE CONSTRAINT FOR (p:Person) REQUIRE p.id IS UNIQUE;
// Create constraints for Organization (base label for inheritance)
CREATE CONSTRAINT FOR (o:Organization) REQUIRE o.id IS UNIQUE;
CREATE CONSTRAINT FOR (o:Organization) REQUIRE o.name IS UNIQUE;

// Ensure PublicOrganization and NewsAgency inherit from Organization
CREATE CONSTRAINT FOR (po:PublicOrganization) REQUIRE (po:Organization);
CREATE CONSTRAINT FOR (na:NewsAgency) REQUIRE (na:Organization);
