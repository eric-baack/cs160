#!/usr/bin/env python3
"""
customproblem classes
"""

"""
implement a seed bank database
each set of seeds is an accession, which includes collection lat, long, year.
Each accession has taxonomy (genus, species) which has family (family, alternative family)
each accession can be crop (includes breeder, disease resistance) or wild (population size, health)
"""

from abc import ABC, abstractmethod

class accession(ABC):
    """
    Implement superclass accession, which takes latitude, longitude, year
    accessions can be for wild or domesticated lineages
    longitude must be in form xx.xxx between -90 and +90;
    latitude must be in form yy.yyy between -180 and + 180
    Taxonomy is object with genus, species, family.
    Family is in turn object with family, alternative family
    """

    @abstractmethod
    def __init__(self, latitude, longitude, year, genus, species, bot_family, alt_family):
        """ init function for superlcass accession """
        self._latitude = latitude
        self._longitude = longitude
        self._year = year
        self._taxonomy = taxonomy(genus, species, bot_family, alt_family) # make object

    def __eq__(self, other: object):
        """ Compare two accessions """
        accession_ident = True
        if self.year != other.year:
            accession_ident = False
        elif abs(self.latitude - other.latitude) > .01:
            accession_ident = False
        elif abs(self.longitude - other.longitude) > .01:
            accession_ident = False
        elif self.taxonomy != other.taxonomy:
            accession_ident = False
        return accession_ident

    def __str__(self):
        """ str method """
        tax_str = str(self.taxonomy)  # invokes str in taxonomy
        acc_str = f"Year collected {self.year}.  Latitude: {self.latitude}, longitude: {self.longitude}. \n {tax_str}"
        return acc_str

    def get_latitude(self):
        """ getter for latitude"""
        return self._latitude

    def get_longitude(self):
        """getter for longitude"""
        return self._longitude

    def get_year(self):
        """getter for year"""
        return self._year

    def set_year(self, new_year):
        """setter for year"""
        self._year = new_year

    def get_taxonomy(self):
        """ getter for taxonomy"""
        return self._taxonomy
    
    def get_family(self):
        """ getter for family.  Uses taxonomy.get_family"""
        return self._taxonomy.get_family()

    family = property(get_family)

    year = property(get_year, set_year)

    latitude = property(get_latitude)

    longitude = property(get_longitude)

    taxonomy = property(get_taxonomy)

    def location(self):
        """ method location for class accession
        returns latitude and longitude of accession"""
        loc_str = f"{self.latitude}, {self.longitude}"
        return loc_str

    def collection_update(self, new_year):
        """ method collection_update for accession
        replaces existing year with new_year"""
        self.year = new_year

class wild_collection(accession):
    """
    Class wild_accession
    Takes latitude, longitude, year, genus, species, bot_family,
    alt_family, population size, health
    Instance of superclass accession
    """
    def __init__(self, latitude: float, longitude: float, year: int, \
        genus: str, species: str, bot_family: str, alt_family: str, pop_size: int, health: str):
        """ Constructor for wild collection
        Uses superclass accession
        Takes lat, long (floats), year (int), genus (str), species (str),
        bot_family (str), alt_family (str)
        pop_size (int) and health (string)
        """
        super().__init__(latitude, longitude, year, genus, species, bot_family, alt_family)
        self._pop_size = pop_size
        self._health = health

    def get_latitude(self):
        """getter for latitude"""
        return super().get_latitude()

    def get_longitude(self):
        """getter for longitude"""
        return super().get_longitude()

    def get_year(self):
        """getter for year"""
        return super().get_year()

    def get_family(self):
        """ getter for family"""
        return super().get_family()

    def set_year(self, new_year):
        """setter for year"""
        super().set_year(new_year)

    def get_taxonomy(self):
        """getter for taxonomy"""
        return super().get_taxonomy()

    def get_pop_size(self):
        """getter for population size"""
        return self._pop_size

    def get_health(self):
        """getter for health"""
        return self._health

    def __eq__(self, other: object):
        """ Compare two accessions """
        accession_ident = True
        if self.year != other.year:
            accession_ident = False
        elif abs(self.latitude - other.latitude) > .01:
            accession_ident = False
        elif abs(self.longitude - other.longitude) > .01:
            accession_ident = False
        elif self.taxonomy != other.taxonomy:
            accession_ident = False
        return accession_ident


    def __str__(self):
        """ str method for wild """
        acc_str = super().__str__()
        wild_str = f"{acc_str} \n  Population size: {self.pop_size}.  Health: {self.health}."
        return wild_str

    longitude = property(get_longitude)

    latitude = property(get_latitude)

    year = property(get_year, set_year)

    taxonomy = property(get_taxonomy)

    health = property(get_health)

    pop_size = property(get_pop_size)

    family = property(get_family)

    def location(self):
        """ method location for class wild_collection
        returns latitude and longitude of accession"""
        return super().location()

    def collection_update(self, new_year):
        """ method collection_update for wild_collection
        replaces existing year with new_year"""
        super().collection_update(new_year)

class domesticated_collection(accession):
    """
    Class domesticated_collection
    Takes latitude, longitude, year, taxonomy, breeder, disease reisistance
    Instance of superclass accession
    Taxonomy is object (genus, species, family), with family as object
    """
    def __init__(self, latitude: float, longitude: float, year: int, genus: str, species: str, bot_family: str, alt_family: str, breeder: str, disease_resistance: str):
        """ Constructor for domesticated collection
        uses superclass accession
        Takes lat, long (floats), year (int), taxonomy (object, with genus, species, family)
        Breeder (str) and disease_resistance (str)
        """
        super().__init__(latitude, longitude, year, genus, species, bot_family, alt_family)
        self._breeder = breeder
        self._disease_resistance = disease_resistance

    def get_latitude(self):
        """getter for latitude"""
        return super().get_latitude()

    def get_longitude(self):
        """getter for longitude"""
        return super().get_longitude()

    def get_year(self):
        """getter for year"""
        return super().get_year()

    def set_year(self, new_year):
        """setter for year"""
        super().set_year(new_year)
    
    def get_family(self):
        """ getter for family.  Uses taxonomy.get_family"""
        return super().get_family()

    def get_taxonomy(self):
        """getter for taxonomy"""
        return super().get_taxonomy()

    def get_breeder(self):
        """getter for breeder"""
        return self._breeder

    def get_disease_resistance(self):
        """getter for disease resistance"""
        return self._disease_resistance

    longitude = property(get_longitude)

    latitude = property(get_latitude)

    year = property(get_year, set_year)

    taxonomy = property(get_taxonomy)

    breeder = property(get_breeder)

    disease_resistance = property(get_disease_resistance)

    family = property(get_family)

    def location(self):
        """ method location for class domesticated_collection
        returns latitude and longitude of accession"""
        return super().location()

    def collection_update(self, new_year):
        """ method collection_update for domesticated_collection
        replaces existing year with new_year"""
        super().collection_update(new_year)


    def __eq__(self, other: object):
        """ Compare two accessions """
        accession_ident = True
        if self.year != other.year:
            accession_ident = False
        elif abs(self.latitude - other.latitude) > .01:
            accession_ident = False
        elif abs(self.longitude - other.longitude) > .01:
            accession_ident = False
        elif self.taxonomy != other.taxonomy:
            accession_ident = False
        return accession_ident

    def __str__(self):
        """ str method for domesticated accession"""
        acc_str = super().__str__()
        dom_str = f"{acc_str} \n Breeder: {self.breeder}.  Disease resistance: {self.disease_resistance}"
        return dom_str

class taxonomy:
    """ Class taxonomy
    Takes genus (str), species (str) and family (object)
    Stored in wild_collection & domesticated_collection as object
    """

    def __init__(self, genus: str, species: str, bot_family: str, alt_family: str):
        """ Constructor for class taxonomy """
        self._genus = genus
        self._species = species
        self._family = family(bot_family, alt_family) #create family object

    def get_genus(self):
        """getter for genus"""
        return self._genus

    def get_species(self):
        """getter for species"""
        return self._species

    def set_species(self, new_species):
        """setter for species"""
        self._species = new_species

    def get_family(self):
        """getter for family"""
        return self._family

    def __str__(self):
        """str method for taxonomy"""
        fam_str = str(self.family)
        tax_str = f"{self.genus} {self.species} ({fam_str})"
        return tax_str

    def __eq__(self, other):
        """comparison method for taxonomy"""
        tax_ident = True
        if self.family != other.family:
            tax_ident = False
        elif self.genus != other.genus:
            tax_ident = False
        elif self.species != other.species:
            tax_ident = False
        return tax_ident


    species = property(get_species, set_species)

    genus = property(get_genus)

    family = property(get_family)

    def abb_taxonomy(self):
        """ print abbreviated genus / species """
        genus_str = self.genus
        abbrev_str = f"{genus_str[0:1]}. {self.species}"
        return abbrev_str

    def corrrect_species(self, new_species):
        """ update with new species name"""
        self.species = new_species

class family:
    """ Class family
    Takes bot_family (str), alt_family (str)
    Stored as object in taxonomy"""

    def __init__(self, bot_family: str, alt_family: str):
        """Constructor for family"""
        self._bot_family = bot_family
        self._alt_family = alt_family

    def get_bot_family(self):
        """getter for botanic family"""
        return self._bot_family

    def set_bot_family(self, new_family):
        """setter for botanic family"""
        self._bot_family = new_family

    def get_alt_family(self):
        """getter for alt family"""
        return self._alt_family

    def set_alt_family(self, new_family):
        """setter for alt family"""
        self._alt_family = new_family

    bot_family = property(get_bot_family, set_bot_family)

    alt_family = property(get_alt_family, set_alt_family)

    def __str__(self):
        """str method for family"""
        return f"({self._bot_family})"

    def __eq__(self, other):
        """ comparison for family"""
        fam_ident = True
        if self.bot_family != other.bot_family:
            if self.bot_family != other.alt_family:
                fam_ident = False
        return fam_ident

    def update_family(self, new_family):
        """update family with new taxonomic name"""
        self.alt_family = self.bot_family
        self.bot_family = new_family

    def old_nomen(self):
        """report old nomenclature and new nomenclature"""
        nomen_str = f"Old family: {self.alt_family}; current name: {self.bot_family}"
        return nomen_str

def main():
    """Main"""
    Hopi = domesticated_collection(30.45, 151.72, 2013, "Helianthus", "annuus", "Asteraceae", "Compositae", "Hopi tribe", "Downy mildew")
    print(f"Hopi year: {Hopi.year}")
    print(f"Hopi location:  {Hopi.latitude}, {Hopi.longitude}")
    print(f"Hopi taxonomy: {Hopi.taxonomy}")
    NE2182 = wild_collection(45.23, 171.72, 1997, "Helianthus", "annuus", "Asteracaeae", "Compositae", 400, "No fungus")
    print(f"Wild year: {NE2182.year}")
    print(f"Wild location:  {NE2182.latitude}, {NE2182.longitude}")
    print(Hopi)
    print(Hopi.family)
    print(NE2182)
    NE2182.collection_update(2019)
    print(NE2182)
    if NE2182 == NE2182:
        print("Same")
    else:
        print("different")
    taxon1 = taxonomy("Helianthus", "annuus", "Asteraceae", "Compositae")
    print(taxon1.abb_taxonomy())

if __name__ == "__main__":
    main()
