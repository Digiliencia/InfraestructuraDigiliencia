// 1. Create constraints
CREATE CONSTRAINT unique_topic_name
FOR (t:Topic)
REQUIRE t.name IS UNIQUE;

CREATE CONSTRAINT unique_field_name
FOR (f:Field)
REQUIRE f.name IS UNIQUE;

CREATE CONSTRAINT unique_person_id
FOR (p:Person)
REQUIRE p.id IS UNIQUE;

// Create constraints for Organization (base label for inheritance)
CREATE CONSTRAINT unique_organization_id
FOR (o:Organization)
REQUIRE o.id IS UNIQUE;

CREATE CONSTRAINT unique_organization_name
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

CREATE CONSTRAINT unique_topic_name
FOR (t:Topic)
REQUIRE t.name IS UNIQUE;

CREATE CONSTRAINT require_person_name
FOR (p:Person)
REQUIRE p.name IS NOT NULL;uniqueness by identifiers (and force NOT NULL)

CREATE CONSTRAINT require_topic_name
FOR (t:Topic)
REQUIRE t.name IS NOT NULL;

CREATE CONSTRAINT require_person_name
FOR (p:Person)
REQUIRE p.name IS NOT NULL;

CREATE CONSTRAINT require_person_id
FOR (p:Person)
REQUIRE p.id IS NOT NULL;

CREATE CONSTRAINT require_organization_id
FOR (o:Organization)
REQUIRE o.id IS NOT NULL;

CREATE CONSTRAINT require_organization_name
FOR (o:Organization)
REQUIRE o.name IS NOT NULL;

CREATE CONSTRAINT require_news_header
FOR (n:News)
REQUIRE n.header IS NOT NULL;

CREATE CONSTRAINT require_news_date
FOR (n:News)
REQUIRE n.date IS NOT NULL;

CREATE CONSTRAINT require_topic_name
FOR (t:Topic)
REQUIRE t.name IS NOT NULL;

CREATE CONSTRAINT require_field_name
FOR (f:Field)
REQUIRE f.name IS NOT NULL;

CREATE CONSTRAINT require_field_description
FOR (f:Field)
REQUIRE f.description IS NOT NULL;