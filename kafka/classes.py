from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class SitesToPackage(Base):
    __tablename__ = 'sites_to_package'
    id = Column(Integer, primary_key=True,autoincrement=True)
    package_id = Column(Integer)
    site_id = Column(Integer)


class PackagesToUsers(Base):
    __tablename__ = 'packages_to_users'
    id = Column(Integer, primary_key=True,autoincrement=True)
    user_id = Column(Integer)
    package_id = Column(Integer)


class UsagePerSite(Base):
    __tablename__ = 'usage_per_site'
    id = Column(Integer, primary_key=True)
    site_id = Column(Integer)
    time = Column(String)
    storage_gb = Column(Integer)
    disc_cache = Column(Integer)
    disc_a_gb = Column(Integer)
    disc_b_gb = Column(Integer)
    cpu_percent = Column(Integer)
    cpu_tic = Column(Integer)


class Sites(Base):
    __tablename__ = 'sites'
    site_id = Column(Integer, primary_key=True,autoincrement=True)
    
    user_id = Column(Integer)



class Packages(Base):
    __tablename__ = 'packages'
    package_id = Column(Integer, primary_key=True,autoincrement=True)
    cost_per_month = Column(Integer)
    storage_gb = Column(Integer)
    disc_cache = Column(Integer)
    disc_a_gb = Column(Integer)
    disc_b_gb = Column(Integer)
    cpu_percent = Column(Integer)
    cpu_tic = Column(Integer)


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True,autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    address = Column(String)
    phone_number = Column(String)


