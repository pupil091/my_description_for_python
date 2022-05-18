mac = "AAAA:BBBB:CCCC"
print(mac.replace(':', '.'))


config = "switchport trunk allowed vlan 1,3,10,20,30,100"
mazerfacker = config.split()
vlanpidaran = mazerfacker[-1]
result = vlanpidaran.split()
print(result)


vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans.sort()
asd = set(vlans)
result = list(asd)
print(result)


command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
qaw1 = command1.split()
qaw2 = command2.split()
saw1 = qaw1[-1]
saw2 = qaw2[-1]
few1 = saw1.split(",")
few2 = saw2.split(",")
sorted(few1)
sorted(few2)
result = list(set(few1) & set(few2))
print(result)