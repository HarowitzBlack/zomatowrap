
# zomato wrap : Zomato wrap is an api wrapper.

import requests

credentials = {
                # zomato api key to access taco resturant data
                "API_KEY":"<key>"
}

class ZomatoApi():

    def __init__(self,API_KEY):
        self.API_KEY = API_KEY
        self.base_url = "https://developers.zomato.com/api/v2.1/"
        # the api key is passed in the header of the url
        self.headers = {"user-key":"{}".format(self.API_KEY)}

    def GetCategories(self):
        self.cat_url = self.base_url + "categories"
        #send a GET request
        self.response = requests.get(self.cat_url,headers=self.headers)
        return self.response.json()

    def GetCityDetails(self,location=None,coords=[None,None],max_count=5):
        """
            location    : location name
            coords      : [lat,lon] takes a list -----> optional
            max_count   : number of results to be displayed
        """
        self.location = location
        self.coords = coords
        self.max_count = max_count
        # api request url for cities
        self.city_url = self.base_url + "cities"

        if self.location == None and self.coords == None:
            return "\nError! Both can't be None\n"

        if self.location is None:
            self.params = {
                "count": "{}".format(self.max_count),
                "lat"  : "{}".format(self.coords[0]),
                "lon"  : "{}".format(self.coords[1])
            }
        else:
            self.params = {
                "q" : "{}".format(self.location),
                "count": "{}".format(self.max_count),
            }
        self.response = requests.get(self.city_url,headers=self.headers,params=self.params)
        return self.response.json()

    def GetResturantCollections(self,city_id = 280,max_count = 5):
        # get the ciy_id using GetCityDetails() method. It's tagged as 'id'
        self.city_id, self.max_count = city_id,max_count
        # resturant collection url
        self.res_url = self.base_url + "collections"
        if self.city_id == None and self.max_count == None:
            return "Error! city_id and max_count can't be None"

        self.params = {
            "city_id":"{}".format(self.city_id),
            "count"  :"{}".format(self.max_count)
        }
        self.response = requests.get(self.res_url,headers=self.headers,params=self.params)
        return self.response.json()

    def GetCuisines(self,city_id = 280,max_count = 5):
        self.city_id, self.max_count = city_id,max_count
        # resturant collection url
        self.cuisine_url = self.base_url + "cuisines"
        if self.city_id == None and self.max_count == None:
            return "Error! city_id and max_count can't be None"

        self.params = {
            "city_id":"{}".format(self.city_id),
            "count"  :"{}".format(self.max_count)
        }
        self.response = requests.get(self.cuisine_url,headers=self.headers,params=self.params)
        return self.response.json()


if __name__ == '__main__':
    key = credentials['API_KEY']
    app = ZomatoApi(key)
    v = app.GetCuisines(280,max_count = 3)
    print(v)
