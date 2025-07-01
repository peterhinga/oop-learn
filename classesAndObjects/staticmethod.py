class MetertoKm:

    @staticmethod
    def metertokm(m): # 1 meter == 0.001km
        meter = m
        result = meter / 1000
        return f"{meter} meters to kilometers is {result}"
    
    @staticmethod
    def kmtometer(km):
        km = km
        result = km * 1000
        return f"{km} kilometers to meters is {result}"
    
m = MetertoKm.metertokm(1000)
kM = MetertoKm.kmtometer(1000)

print(m)
print(kM)