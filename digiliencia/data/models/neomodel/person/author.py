from neomodel import RelationshipFrom, ZeroOrMore

from digiliencia.data.models.neomodel.person.person import Person


class Author(Person):
    """Author node model that extends Person."""

    # Relationships
    wrote = RelationshipFrom("News", "WRITTEN_BY", cardinality=ZeroOrMore)
