
class UndergroundSystem:

    def __init__(self):
        self.station_avg = {}
        self.traveller = {}

        
    def get_prev_val(self, end, start):
        new_stn = start+':'+end
        if new_stn in self.station_avg:
            return self.station_avg[new_stn]
        else:
            self.station_avg[new_stn] = {'sum':0, "count":0, 'avg':0}
            return self.station_avg[new_stn]
    
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.traveller[id]={"stationName":stationName, "start":t}        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        avg_dict = self.get_prev_val(stationName, self.traveller[id]['stationName'])
        total_time = t - self.traveller[id]['start']
        avg_dict['count']+=1
        avg_dict['sum']+=total_time
        avg_dict['avg']=avg_dict['sum']/avg_dict['count']
        new_stn = self.traveller[id]['stationName']+":"+stationName
        self.station_avg[new_stn] = avg_dict
        self.traveller.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station_avg[startStation+":"+endStation]['avg']


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)