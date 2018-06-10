"""
API key configuration
"""

def main():
    print("API key configuration")
    key = input("Key : ")
    apikey = open("../api.key","w",encoding="utf8")
    apikey.write(key)
    apikey.close()
    print("Done")

if __name__ == '__main__':
    main()
