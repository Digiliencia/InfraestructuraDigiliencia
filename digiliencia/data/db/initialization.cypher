// 1. Create constraints to ensure uniqueness by identifiers
CREATE CONSTRAINT unique_person_id
FOR (p:Person)
REQUIRE p.id IS UNIQUE;
// Create constraints for Organization (base label for inheritance)
CREATE CONSTRAINT unique_organization_id
FOR (o:Organization)
REQUIRE o.id IS UNIQUE;
CREATE CONSTRAINT unique_organizarion_name
FOR (o:Organization)
REQUIRE o.name IS UNIQUE;

// Create constraints for uniqueness of news: header with date
CREATE CONSTRAINT unique_news_header_date
FOR (n:News)
REQUIRE (n.header, n.date) IS UNIQUE;

// Create constraints for uniqueness of person name
CREATE CONSTRAINT unique_person_name
FOR (p:Person)
REQUIRE p.name IS UNIQUE;

//Crear vectorIndex en noticiasContentEmbedding y noticiasHeaderEmbedding