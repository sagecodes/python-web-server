# import sys module for functions to manipulate python runtime environment
import sys

# Import classes from alchemy. Use with mapper code
from sqlalchemy import
Column, ForeignKey, Integer, String

# Import declarative base use for configuration and class code
from sqlalchemy.ext.declarative import
declarative_base

# import relationship in order to create foreign key relationship
from sqlalchemy.orm import relationship

# import create engine class to be used at the end of the file
from sqlalchemy import create_engine

# Make instance of declarative base class. Name it Base for short
Base = declarative_base()
#### insert at end of file ######

# Create instance of creat eengine class and point to database used.
engine = create_engine(
	'sqlite:///restaurantmenu.db')

# goes into database and adds classes we create.
Base.metadata.create_all(engine)