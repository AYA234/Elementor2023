from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes import UsagePerSite,Users,Packages,PackagesToUsers,Sites,SitesToPackage
import json
class DataWriting:

    def __init__(self):
        
        self.engine = create_engine('postgresql://developer:41b387c1-2cf9-4436-85fa-7c75093b7d14@test-rds-dev.colcjtm9obot.eu-west-1.rds.amazonaws.com:5432/metrics_dev')
        self.Session = sessionmaker(bind=self.engine)
    
    def create_user(self,data):
        user_id=data.get('user_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        address = data.get('address')
        phone_number = data.get('phone_number')
        if user_id is None:
            return 'cannot create user'

        session = self.Session()
        user = Users(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            phone_number=phone_number
        )
        session.add(user)
        session.commit()
        session.close()

        return 'success'
    def create_usage_per_site(self,data):
         
        id = data.get('id')
        site_id = data.get('site_id')
        time = data.get('time')
        storage_gb = data.get('storage_gb')
        disc_cache = data.get('disc_cache')
        disc_a_gb = data.get('disc_a_gb')
        disc_b_gb = data.get('disc_b_gb')
        cpu_percent = data.get('cpu_percent')
        cpu_tic = data.get('cpu_tic')
        if (

            site_id is None 

        ):
            return  'Missing metric data'

        session = self.Session()
        usage = UsagePerSite(id=id,site_id=site_id, time=time, storage_gb=storage_gb, disc_cache=disc_cache,
                            disc_a_gb=disc_a_gb, disc_b_gb=disc_b_gb, cpu_percent=cpu_percent, cpu_tic=cpu_tic)
        session.add(usage)
        session.commit()
        session.close()

    def create_sites_to_package(self,data):
        package_id = data.get('package_id')
        site_id = data.get('site_id')
        if any(value is None for value in [package_id, site_id]):
            return jsonify({'error': 'Missing sites-to-package data'}), 400

        session = self.Session()
        site_to_package = SitesToPackage(package_id=package_id, site_id=site_id)
        session.add(site_to_package)
        session.commit()
        session.close()

        return 'success'

    def create_site(self,data):

        user_id = data.get('user_id')
        site_id = data.get('site_id')
        if site_id is None or site_id is None:
            return jsonify({'error': 'Missing user_id or site_id'}), 400
        
        session = self.Session()
        site = Sites(user_id=user_id, site_id=site_id)
        session.add(site)
        session.commit()
        session.close()
        
        
    def create_package(self,data):
        cost_per_month = data.get('cost_per_month')
        storage_gb = data.get('storage_gb')
        disc_cache = data.get('disc_cache')
        disc_a_gb = data.get('disc_a_gb')
        disc_b_gb = data.get('disc_b_gb')
        cpu_percent = data.get('cpu_percent')
        cpu_tic = data.get('cpu_tic')
        if (
            cost_per_month is None and
            storage_gb is None and
            disc_cache is None and
            disc_a_gb is None and
            disc_b_gb is None and
            cpu_percent is None and
            cpu_tic is None
        ):
            return 

        session = self.Session()
        package = Packages(
            cost_per_month=cost_per_month,
            storage_gb=storage_gb,
            disc_cache=disc_cache,
            disc_a_gb=disc_a_gb,
            disc_b_gb=disc_b_gb,
            cpu_percent=cpu_percent,
            cpu_tic=cpu_tic
        )
        session.add(package)
        session.commit()
        session.close()

        return 'success'
    
    def create_package_to_user(self,data):
        
        user_id = data.get('user_id')
        package_id = data.get('package_id')
        if user_id is None or package_id is None:
            return {'error': 'Missing package-to-user data'}

        session = self.Session()
        package_to_user = PackagesToUsers(user_id=user_id, package_id=package_id)
        session.add(package_to_user)
        session.commit()
        session.close()

        return{'message': 'Package-to-user created successfully'}





