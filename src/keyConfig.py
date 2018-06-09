"""
Configuration de l'API key
"""

print("API key configuration")
key=input("Key : ")
apikey=open("../api.key","w",encoding="utf8")
apikey.write(key)
apikey.close()
