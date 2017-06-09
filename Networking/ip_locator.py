"""Description from karan/Projects:
    Country from IP Lookup - Enter an IP address and find the country that IP is registered in. Optional: Find the Ip automatically."""
import geoip2.database
import ipgetter

def get_my_ip():
    IP = ipgetter.myip()
    return IP

def get_ip_country(IP):
    reader = geoip2.database.Reader('GeoLite2-Country_20170606/GeoLite2-Country.mmdb') # This is the database method
    response = reader.country(IP)
    country_name = response.country.name
    return country_name


if __name__ == '__main__':
    IP = get_my_ip()
    country = get_ip_country(IP)
    print(country)
